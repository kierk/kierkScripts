#! /usr/bin/env python

import struct, socket


host = "amazeing.hackable.software"
port = 1337
buttonup = 31337
buttondown = 31339
buttonleft = 31336
buttonright = 31338

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
# s.send(passing)

def move_up():
	s_up = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s_up.connect((host, buttonup))
	s.send()
def move_down():
def move_left():
def move_down():


# Main to Edit
def main():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	s.send


if __name__ == "__main__":
    main()


