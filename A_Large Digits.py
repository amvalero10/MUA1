# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def resolve(x):
    x = x.split()
    
    a = x[0]
    b = x[1]
    
    af = 0
    bf = 0
    
    for i in a:
        af = int(i)+int(af)
        
    for i in b:
        bf = int(i)+int(bf)
        
    
    if af >= bf:
        print(af)
    else:
        print(bf)
        

#inp = "123 234"
#inp = "593 953"
#inp = "100 999"
inp = input()
resolve(inp)