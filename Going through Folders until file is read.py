# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello")
import os
def search(root):
    new_dir = {}
    for element in os.listdir(root):
        if os.path.isfile(os.path.join(root, element)):
                          try:
                              with open(os.path.join(root, element)) as file:
                                  new_dir[os.path.join(root, element)] = file.readline()
                          except UnicodeDecodeError:
                                pass
        elif os.path.isdir(os.path.join(root, element)):
            new_dir.update(search(os.path.join(root,element)))
    return new_dir

print(search('C:'))
                              