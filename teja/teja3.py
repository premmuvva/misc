# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:17:43 2018

@author: reddy
"""
from time import sleep
def main():
    current_line=0
    while(True):
        with open("cache.txt") as f:
            total_lines=0
            for line in f:
                total_lines+=1
                if current_line<total_lines:
                    print(line)
            current_line=total_lines
        
main()