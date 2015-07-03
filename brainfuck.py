#!/usr/bin/python
import sys

# bf_chars = ['.', ',', '[', ']', '<', '>', '+', '-']

def interpret(code):
    code = list(code)
    
    cells = [0]
    dataptr = 0
    i = 0
    
    # main loop
    while i < len(code):
        command = code[i]
        
        if command == ">":
            dataptr += 1
            if dataptr == len(cells): 
                cells.append(0)
        if command == "<":
            dataptr = 0 if dataptr <= 0 else dataptr - 1
            
        if command == "+":
            cells[dataptr] = cells[dataptr] + 1 if cells[dataptr] < 255 else 0
        if command == "-":
            cells[dataptr] = cells[dataptr] - 1 if cells[dataptr] > 0 else 255
        
        if command == ".": print chr(cells[dataptr]),
        if command == ",": cells[dataptr] = ord(raw_input()[0])
    
        i+= 1
    
    
    
# should print "Hello World!"
interpret('++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.')