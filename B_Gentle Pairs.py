# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:38:36 2021

@author: Angelo Marcetty
"""




def resolve(x):
        
    r = 0
    
    x = x.split("\n")
    
    print(x)
    
    for i in x:
        print(i+1)
        
        p = x[i+int(1)] 
        
        a1 = p[0]
        a2 = p[2]




inp = "3\n0 0\n1 2\n2 1"
print(inp)
#inp = input()
resolve(inp)