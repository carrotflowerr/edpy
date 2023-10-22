import os

input_lines = []
# this is our buffer (highly cringe)
filename = 'out.txt'

def main():
    global lines
    global filename
    lines = []
    
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.strip())
    #print(lines)   
    q = 0
    while q == 0:
        mode = input('>')
        if mode == 'i': insert()
        if mode == 'w': write()
        if mode == 'p': print_file()
        if mode == 'd': deleteLine() # d:{line_number}
        if mode == '!': command()
        if mode == 'f': name_file()
        if mode == 'cl': clear()
        if mode == 'q': q = 1


def name_file():
    global filename
    print("Current file:",filename)
    new_file_name = str(input("Filename:"))
    filename = new_file_name

def insert():
    global input_lines 
    while True:
        current_line = input('')
        if current_line == '.':
            break
        input_lines.append(current_line)  



def deleteLine():
    global lines
    global filename
    print(len(lines)-1)
    # puts lines in an array

    query = int(input())# 1=1
    #query = query + 1
    if query > len(lines):
        print('out of range')
    if query <= len(lines):
        searched_line = (lines[query])
        print(searched_line)
        edit_choice = str(input())
        if edit_choice == 'q': 
            return lines
        if edit_choice == 'd': 
            searched_line = lines.pop(query)  # Remove and store the line to be deleted
            print(f'Deleted: {searched_line}')
            with open(filename, 'w') as file:
                file.write('\n'.join(lines))
    

def write():
    global input_lines  
    global filename
    with open(filename, 'a') as file:
        for line in input_lines:
            file.write(line + '\n')
    input_lines = []  # Clear the list after writing

def clear():
    global filename
    with open(filename, 'w') as file:
        file.write("")

def print_file():
    global filename
    os.system('cat '+str(filename))
   
def command():
    global filename
    q = 0
    while q == 0:
        command = str(input('!'))
        if command == 'q':
            break
        os.system(command)

main()
