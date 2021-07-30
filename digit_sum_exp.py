"""
Author: A. Salas
Project: 
Created:  Wed Jul 28 15:33:06 2021
Description: 
"""

#imports
import time

#main function
def main(x, y):
    pow_int = pow(x,y)
     
    while True:
        temp_i = 0
        temp_s = str(pow_int)
        for i in range(len(temp_s)):
            temp_i += int(temp_s[i])
     
        pow_int = temp_i
        if (len(str(pow_int)) == 1):
            break
     
    return pow_int 

#auto-run main
if __name__ == "__main__":
    
    #upper limites of n and exponent
    n_range = 1000
    pow_range = 100
    
    #this will hold instances
    temp_array = [0,0,0,0,0,0,0,0,0,0]
  
    start = time.perf_counter() #start tracking time
    for j in range(2,pow_range):
        for i in range(2, n_range):
            result = main(i, j)
            #print(f"Number #{x} | Result: {result}")
            temp_array[result] += 1
            if(result ==3 or result == 6):
                print(f"NUMBER:  {i} | EXP: {j} | RESULT: {result}")
 
    stop = time.perf_counter() #stop time
    
    for i in range(len(temp_array)):
        print(f"i: {i} | Count: {temp_array[i]}")
        
    print(f"Elapsed time: {stop-start}")            
        
#TODO: 

    
