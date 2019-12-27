var = 0 
while var <= 20:
    if var % 2 == 0: #### indicates its even 
         var +=1 
         continue  ## will continue the loop 
         print("Testing after continue")
    print(f"we are counting odd number: {var}")
    var +=1
print(f"Done of Counting all odd numbers to {var-1}")
    
    
