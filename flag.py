#flag.py
#author: mogilevets nikita

import sys

def check_N(N):
    if N <= 0 or N%2 != 0:
        raise Exception("ArgumentError")

def print_string(s):
    sys.stdout.write(s)
    
def output_horizontal_line(N):
    for i in range(3*N + 2):
        print_string("#")
    print_string("\n")

def output_top_line(N):
    output_horizontal_line(N)

def output_bottom_line(N):
    output_horizontal_line(N)

def output_line(N):
    sys.stdout.write("#")
    for i in range(3*N):
        print_string(" ")
    print_string("#")
    print_string("\n")

def output_circle(N, width):
    print_string("#")
    blank_width = 3*N//2 - width//2 - 1
    for i in range(0, blank_width):
        print_string(" ")
    print_string("*")
    for i in range(0, width):
        print_string("o")
    print_string("*")
    for i in range(0, blank_width):
        print_string(" ")
    print_string("#")
    print_string("\n")

def flag():
    N = int(input("Parse N:"))

    check_N(N)
    
    output_top_line(N)

    for i in range(N//2):
        output_line(N)

    width = 0

    for i in range(0,N//2):
        output_circle(N, width)
        width += 2

    width -= 2

    for i in range(0, N//2):
        output_circle(N, width)
        width -= 2

    for i in range(N//2):
        output_line(N)

    output_bottom_line(N)

flag()
