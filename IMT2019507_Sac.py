#LRU implementation has been done for this 4-way set associative cache
import math,random 

s = input("Enter file name you would like to run (with it's extension) : ")

def hex_to_binary(ini_string):    # This function basically converts hexadecimal string to a binary string
    n = int(ini_string, 16)  
    bStr = '' 
    while n > 0: 
        bStr = str(n % 2) + bStr 
        n = n >> 1    
    return bStr 

def binaryToDecimal(n):           # This function returns decimal value of a binary string
    return int(n,2)

memory = []                       # This is main memory
priority = []                     # This is used for LRU Implementation
validity = []                     # This is used to check validity of an address
miss_count = 0
hit_count = 0
timer = 0

#We will have a timer which will be continuously incremented everytime in a while loop(its like time)
#Whenever a tag is accessed/checked or assigned in a block, its corresponding priority in the priority list is set to the timer value in that iteration of the loop 
#So if block has the least priority value, it means that it was accessed/modified a longer while ago than the other blocks

for i in range(16384):            # according to the problem given, the memory and other lists should have length of 2 power 14
    memory.append(['0','0','0','0'])
    priority.append([0,0,0,0])
    validity.append([0,0,0,0])
    
f = open(s,"r")
str_list = f.readlines()          # stores all the lines of file till eof into str_list 
binary_addr_list = []

for i in str_list:
    binary_addr_list.append(hex_to_binary(i[4:12]).zfill(32))  # we convert hexadecimal format to binary format and store it in another list

for binary_str in binary_addr_list:
    
    timer += 1
    tag = binary_str[0:16]
    index = binaryToDecimal(binary_str[16:30])  # tag and index are extracted from the string
    
    if tag in memory[index]:                    # if tag is present at memory[index]...
    
        ind = memory[index].index(tag)
        
        if validity[index][ind] == 1:           # if it's valid bit is 1...
        
            hit_count += 1                      # then we increase the count of hit_count
            priority[index][ind] = timer
        
    else:
    
        miss_count += 1                         # If there's no tag match, we will increase miss_count by 1
        
        if 0 in validity[index]:                # if there is an unused block whose valid bit is 0, we use it to store data
        
            var = validity[index].index(0)      
            memory[index][var] = tag            # make its value = tag in memory 
            validity[index][var] = 1            # we change valid bit to 1
            priority[index][var] = timer        # we assign it's priority the value of timer
            
        else:                                   # if every block is full, then we will evict a block according to LRU algorithm
        
            memory[index][priority[index].index(min(priority[index]))] = tag
            priority[index][memory[index].index(tag)] = timer

print("For file : " + s)
print("The number of misses are : " + str(miss_count))
print("The number of hits are : " + str(hit_count))
print("hit rate :",(hit_count/(hit_count + miss_count))*100)
f.close()

