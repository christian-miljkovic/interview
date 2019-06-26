# Class for Dynamic Array

class DynamicArray:

    def __init__(self):
        self.list = [None] * 10
        self.capacity = 10
        self.currentIndex = 0
    
    def append(self, value):
        if(value == None):
            return
        if(self.currentIndex == 0):
            self.list[0] = value
            self.currentIndex += 1
        else:
            if(self.currentIndex == self.capacity):
                self.list[0] = value
                self.currentIndex = 1
            else:
                self.list[self.currentIndex] = value
                self.currentIndex += 1

    def resize(self):
        newBuffer = [None] * len(self.list)
        self.currentIndex = len(self.list)
        self.list.extend(newBuffer)
        self.capacity = len(self.list)

if __name__ == '__main__':
    testArray = DynamicArray()
    print(testArray.list)

    for i in range(0,10):
        testArray.append(i)
    print(testArray.list)

    testArray.append(-1)
    print(testArray.list)
    testArray.resize()
    print(testArray.list)

    for i in range(10,20):
        testArray.append(i)

    print(testArray.list)
    testArray.resize()
    print(testArray.list)

        