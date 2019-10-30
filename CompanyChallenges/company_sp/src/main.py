# import socket library
import socket
import sys
import collections

class Cursor(object):

  def __init__(self, screen):
    self.top_pad = 0
    self.left_pad = 0
    self.color = '#0000ff'
    self.pixel_size = {'width':8, 'height':14}
    # 2D array representing screen
    self.screen = screen
    self.pos = {'row':0, 'col':0}
    self.at_end = True
    

  def move(self, command):
    
    if command == 'right':
      self.move_right()
    elif command == 'left':
      self.move_left()
    elif command == 'up':
      self.move_up()
    elif command == 'down':
      self.move_down()


  def move_up(self):
    curr_row = self.pos['row']
    curr_col = self.pos['col']
    
    if curr_row - 1 >= 0:
      if curr_col - 1 == 0:        
        self.pos['col'] = len(self.screen[curr_row - 1]) - 1
      
      self.pos['row'] -= 1

  def move_down(self):
    curr_row = self.pos['row']
    curr_col = self.pos['col']
    
    if curr_row + 1 < len(self.screen):
      if curr_col > len(self.screen[curr_row + 1]):        
        self.pos['col'] = len(self.screen[curr_row + 1]) - 1
      
      self.pos['row'] += 1

  def move_right(self):
    curr_row= self.pos['row']
    curr_col = self.pos['col']

    if curr_row < len(self.screen) and curr_col < len(self.screen[curr_row]) - 1:
      self.pos['col'] += 1
    else:
      self.move_down()

  def move_left(self):
    curr_row = self.pos['row']
    curr_col = self.pos['col']

    if curr_row < len(self.screen) and curr_col - 1 >= 0:
      self.pos['col'] -= 1
    elif curr_row - 1 >= 0:
      self.pos['row'] -= 1
      self.pos['col'] = len(self.screen[curr_row - 1]) - 1

  def flatten_position(self):
    return (len(self.screen[0]) * self.pos['row'] + self.pos['col']) - 1


  def pos_to_command(self):
    
    top_pad = self.pos['row'] * self.pixel_size['height']
    left_pad = self.pos['col'] * self.pixel_size['width']
    
    return 'rect,{},{},8,14,#FF0000\n'.format(left_pad, top_pad)


class TextEditor(object):

  def __init__(self):    
    self.screen = [[""]]
    self.arr = []
    self.screen_width = 800
    self.screen_height = 600
    self.cursor = Cursor(self.screen)
    self.update_cursor = True
    self.commands = {'return':'\n', 'space': ' '}

  
  def perform_command(self, command):
    if type(command).__name__ == 'key':
      if command.value in ['left','right','up','down']:        
        self.cursor.move(command.value)
        self.update_cursor = False
      else:
        self.generic_key_down(command.value)
    elif type(command).__name__ == 'window':
      self.screen_width = command.width
      self.screen_height = command.height      



  def generic_key_down(self, value):
    insert_value = value
    if value in self.commands:
      insert_value = self.commands[value]
    
    index = self.cursor.flatten_position()
    
    if index < len(self.arr) - 1:
      self.arr.insert(index, insert_value)
    else:
      self.arr.append(insert_value)


  def array_to_screen(self):
    row = 0
    cursor_commands = []
    wrap_count = 0
    
    for index, char in enumerate(self.arr):
      print(wrap_count * 8, self.screen_width)
      if 'backspac' in char:
        if len(self.screen[row]) == 1:
          if row != 0:
            del self.screen[row]
            
            cursor_commands.append('up')
            row -= 1          
        else:
          self.screen[row].pop()
          cursor_commands.append('left')
        del self.arr[index]
        if index - 1 >= 0:
          del self.arr[index-1]   
        wrap_count -= 1     
               
      elif char == '\n' or wrap_count * 8 >= self.screen_width:
        self.screen.append([''])
        cursor_commands.append('down')
        row += 1
        wrap_count = 0

      else:
        self.screen[row].append(char)
        cursor_commands.append('right')
        wrap_count += 1
      
      
    
    if self.update_cursor:
      self.cursor.screen = self.screen
      for cursor_mov in cursor_commands:
        self.cursor.move(cursor_mov)

  def render(self):

    if self.cursor.pos['row'] == len(self.screen)-1 and self.cursor.pos['col'] == len(self.screen[-1])-1:
      self.update_cursor = True

    self.screen = [[""]]  
    self.array_to_screen()
    

    text_on_screen = 'clear\n'
    top_pad = 0
    left_pad = 0
    
    for row in self.screen:      
      text = ''.join(row)
      text_on_screen += 'text,0,{},#000000,{}\n'.format(top_pad, text)
      top_pad += 14

    
    text_on_screen += self.cursor.pos_to_command()
    
    return text_on_screen

def parse_data(data):

  parsed_data = data.strip('\n').lower().split(',')
  
  if len(parsed_data) == 2 and 'keydown' == parsed_data[0]:    
      Key = collections.namedtuple('key', ['value'])
      return Key(parsed_data[1])
    
  elif len(parsed_data) == 3 and 'resize' in parsed_data[0]:
      Window = collections.namedtuple('window', ['width','height'])        
      return Window(int(parsed_data[1]), int(parsed_data[2]))      

# Create a socket for the server on localhost
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',5005)
client_socket.connect(server_address)
text_editor = TextEditor()

while True:
    data = client_socket.recv(16)
    command = parse_data(data)
    
    if command:
      text_editor.perform_command(command)
    client_socket.send(text_editor.render())



