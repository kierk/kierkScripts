#!/usr/bin/env python

################################################
# File to clean bindshells off of Bandit Server
# Uploading to Git as Test
################################################

import sys, struct,socket, subprocess, os

passing = 'exit'
for i in range(0xffff0000, 0xffffffff, 0x20):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("gangsta", 8080))
        s.send(passing)
