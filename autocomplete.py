import os
import readline

def file_completer(text, state):
    line = readline.get_line_buffer()
    path = os.path.expanduser(line)
    if os.path.isdir(path):
        path += '/'
    if os.path.isfile(path):
        return None
    if state == 0:
        if os.path.isdir(path):
            completions = os.listdir(path)
        else:
            completions = [f for f in os.listdir(os.path.dirname(path)) if f.startswith(os.path.basename(path))]
    return completions[state]

readline.set_completer(file_completer)
readline.parse_and_bind('tab: complete')

while True:
    input_string = input("Enter a file or directory path: ")
    if os.path.exists(input_string):
        print("Path exists!")
    else:
        print("Path does not exist.")


"""
python autocomplete.py
(press tab)
Enter a file or directory path: /usr/local/
"""
