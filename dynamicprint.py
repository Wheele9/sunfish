import re, sys
import time
import random
from colorama import Fore, Style

class multiPrinter:
    def __init__(self):
        self.formerText = ''
        self.nextText= ''

    def moveup(self, lines):
        for i in range(lines):
            ## Move cursor up
            sys.stdout.write("\x1b[A")
            
    def addEmptyLine(self, height=1 ):
        self.nextText += '\n'*height

    def addLine(self,*lines, color = 'default', style = 'normal'):
        bigline = ""
        for line in lines:
            bigline += str(line)
        line = bigline
        ### Adding stlye changing ANSI sequences
        if style.upper() == "BRIGHT":
            self.nextText += Style.BRIGHT
        if style.upper() == "DIM":
            self.nextText += Style.DIM

        ### Adding color changing ANSI sequences
        if color.upper() == 'DEFAULT':
            self.nextText += (line)
        elif color.upper() == 'BLACK':
            self.nextText += (Fore.BLACK+line)
        elif color.upper() == 'RED':
            self.nextText += (Fore.RED + line)
        elif color.upper() == 'GREEN':
            self.nextText += (Fore.GREEN + line)
        elif color.upper() == 'YELLOW':
            self.nextText += (Fore.YELLOW + line)
        elif color.upper() == 'BLUE':
            self.nextText += (Fore.BLUE +line)
        elif color.upper() == 'MAGENTA':
            self.nextText += (Fore.MAGENTA +line)
        elif color.upper() == 'CYAN':
            self.nextText += (Fore.CYAN + line)
        elif color.upper() == 'WHITE':
            self.nextText += (Fore.WHITE + line)
        else :
            raise ValueError('The color {} is not available.'.format(color))

        ### Reset style and color changes, add newline char
        self.nextText += Style.RESET_ALL + '\n'

    def update(self):
        # Clear previous text by overwritig non-spaces with spaces
        self.moveup(self.formerText.count("\n"))
        sys.stdout.write(re.sub(r"[^\s]", " ", self.formerText))

        lines2goUp =       self.formerText.count("\n")
        self.moveup(lines2goUp)
        # Print new text
        sys.stdout.write(self.nextText)
        print ( self.formerText.count("\n"))
        print ( self.nextText.count("\n"))
        self.formerText = self.nextText
        self.nextText = ""

if __name__ =="__main__":

    printer = multiPrinter()
    printer.addLine("kecske", color ='red')
    printer.addLine("oroszlan", color='green')
    printer.update()
    time.sleep(2)
    printer.addLine("tigris", color='blue')
    printer.addLine("marha")
    printer.addLine("kutya", color='yellow')
    printer.update()
    time.sleep(2)
    printer.addLine("macska", color='MAGENTA' , style ='bright')
    printer.addLine("borju", color='green', style ='dim')
    printer.update()
