# Direct mapped Cache implementation
import math 

s = input("Enter file name you would like to run (with it's extension) : ")

def hex_to_binary(ini_string):    # This function basically converts hexadecimal string to a binary string

    n = int(ini_string, 16)  
    bStr = ''   
    while n > 0: 
        bStr = str(n % 2) + bStr 
        n = n >> 1    
    
    return bStr 

def binaryToDecimal(n):        # This function returns decimal value of a binary string
    return int(n,2)

memory = []                    # This is main memory
miss_count = 0
hit_count = 0
validity = []                  # This is used to check validity of an address

for i in range(65536):         # according to the problem given, the memory and other lists should have length of 2 power 16
    memory.append(0)
    validity.append(0)
    
f = open(s,"r")
str_list = f.readlines()       # stores all the lines of file till eof into str_list 
binary_addr_list = []

for i in str_list:
    binary_addr_list.append(hex_to_binary(i[4:12]).zfill(32))  # we convert hexadecimal format to binary format and store it in another list

for binary_str in binary_addr_list:
    
    tag = binary_str[0:14]                                     # tag and index are extracted from the string
    index = binaryToDecimal(binary_str[14:30])
    
    if(memory[index] == tag and validity[index] == 1):         # if it's valid bit is 1 and there's a tag match, increase the count of hit_count
        hit_count += 1
        
    else:
        memory[index] = tag                                    # in case there is no tag match, we simply replace the value present at memory[index] by tag and also increase miss_count
        validity[index] = 1                                    # We also set it's validity to 1
        miss_count += 1 
        
print("For file : " + s)
print("The number of misses are : " + str(miss_count))
print("The number of hits are : " + str(hit_count))
print("hit rate :",(hit_count/(hit_count + miss_count))*100)
f.close()

