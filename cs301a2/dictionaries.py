# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:53:35 2018

@author: hans8
"""

import random
import time

n = 200000
start_time = time.time()
test_dictionary = {keys: random.random() for keys in range (0,n)}

# returns all the values in the test_dictionary
def values():
    test_values = test_dictionary.values()
    return (test_values)
    

# returns all the keys in the test dictionary
def keys():
    test_keys = test_dictionary.keys()
    return (test_keys)
    

# returns all the key:value pairs in the dictionary
def items():
    test_items = test_dictionary.items()
    return (test_items)
    

# returns a specific key in the dictionary
def get(): 
    test_getValues = test_dictionary
    return (test_getValues.get(12345))
    
# searches the key, and if it doesnt exist, prints, an alternate value
def get_one(): 
    test_getValueOne = test_dictionary
    return (test_getValueOne.get(200001,199998))
        

# calls and prints the functions. Traded out to test each individual funciton
print (get())
print("--- %s seconds ---" % (time.time() - start_time))





