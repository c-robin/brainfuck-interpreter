#!/usr/bin/python
import sys


class BrainfuckSyntaxException(Exception):
    pass

# bf_chars = ['.', ',', '[', ']', '<', '>', '+', '-']
# Cells have a cize of 8-bits so 255
CELL_SIZE =  255

def matching_brackets(code):
    matching = {}
    stack = []
    i = 0
    for pos, cmd in enumerate(code):
        if cmd == "[":
            stack.append(pos);
        elif cmd == "]":
            if len(stack) == 0:
                raise BrainfuckSyntaxException("Missing [ for a ]")
            prevpos = stack.pop()
            matching[prevpos] = pos
            matching[pos] = prevpos
    if len(stack) != 0:
        raise BrainfuckSyntaxException("Missing ] for a [")
    return matching

def interpret(code):
    code = list(code)
    
    cells = [0]
    dataptr = 0
    i = 0
    matching = matching_brackets(code)
    
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
            cells[dataptr] = cells[dataptr] + 1 if cells[dataptr] < CELL_SIZE else 0
        if command == "-":
            cells[dataptr] = cells[dataptr] - 1 if cells[dataptr] > 0 else CELL_SIZE
        
        if command == ".": print chr(cells[dataptr]),
        if command == ",": cells[dataptr] = ord(raw_input()[0])
        
        if command == "[" and cells[dataptr] == 0:
            i = matching[i]       
        if command == "]" and cells[dataptr] != 0:
            i = matching[i] 
        
        i+= 1
    
    
    
# should print "Hello World!"
interpret('++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.')
# ToLower
interpret('+[ >,>++++[<++++++++>-]<.<]')