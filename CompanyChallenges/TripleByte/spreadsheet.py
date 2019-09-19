

class Spreadsheet:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        
        self.sheet = []
        for i in range(0,row):
            temp = []
            for j in range(0,col):
                temp.append("")
            self.sheet.append(temp)


    def update(self, row, col, val):
        self.sheet[row][col] = val        

    def __str__(self):
        
        return_str = ""
        for row in self.sheet:
            return_str += "|".join(row) + "\n"

        return return_str

    # 1. Longest val in col
    #2. Curr val_len = longest_val_len -> extend
    def longest_in_col(self):
        hash_map = dict()
        for i in range(0,len(self.sheet)):
            for j in range(0,len(self.sheet[0])):
                if j not in hash_map:
                    hash_map[j] = len(self.sheet[i][j])
                else:
                    curr_max = hash_map[j]
                    if curr_max < len(self.sheet[i][j]):
                        hash_map[j] = len(self.sheet[i][j])

        return hash_map

    def make_pretty(self):
        hash_map = self.longest_in_col()
        for i in range()





s = Spreadsheet(4,3)
s.update(0,0,"bob")
s.update(0,1,"10")
s.update(0,2,"foo")
s.update(1,0,"alice")
s.update(1,1,"5")