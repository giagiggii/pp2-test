class string:
    def __init__(s):
        s.input_string = ""

    def inp(s): #get string then print upper
        s.input_string = input()

    def cout(s):
        print(s.input_string.upper())

s1= string()
s1.inp()
s1.cout()
