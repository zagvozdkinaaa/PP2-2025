class stringHandler:
    def __init__(self):
        self.text=""
    def getString(self):
        self.text=input()
    def printString(self):
        print (self.text.upper())

handler = stringHandler()
handler.getString()
handler.printString()