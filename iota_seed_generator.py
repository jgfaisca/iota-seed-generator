#!/usr/bin/python
#
# Generate IOTA wallet seed 
# 81 characters A-Z and 9  
#

from random import SystemRandom
alphabet = u'9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
generator = SystemRandom()
print(u''.join(generator.choice(alphabet) for _ in range(81)))
