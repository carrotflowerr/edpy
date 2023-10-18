#
import os

def main():
    q=0
    while q == 0:
        mode=input('>')
        if mode == 'i': write()
        if mode == 'p': print_file()
        if mode == '!': command()
        if mode == 'cl': clear()
        if mode == 'q': q=1
        #else: print('?')
        # jank?
def write():    
    while True:
        #print('insert\n')
        current_line = input('')
        if current_line == '.':
            break
        with open('out.txt', 'a') as file:
            file.write(str(current_line)+"\n")
            
def clear():
    with open('out.txt', 'w') as file:
        file.write("")
    # This is bad.
    
    
def print_file():
    os.system("cat out.txt")

def command():
    q=0
    while q == 0:
        command = str(input('!'))
        if command == 'q':break
        os.system(command)

main()