def fun(digits):
    digits=digits[::-1]
    i,carry=0,0
    flag=True
    
    while flag:
#         if digit is 9 place 0 at that location and loop again
        if digits[i] == 9:
            digits[i]=0

            flag=True
        else:
#             if digit is not 9 then just inc value and replace it and break loop because carry is not genearted as values are 0<=digist[i]>=9
            digits[i]=digits[i]+1
            break
            
        i=i+1
#         if more then 1 9's then else may never be executed for [9,9] then by using i value if it i>=len(digits) means just append 1 
        if i >= len(digits):
            print("In")
            digits.append(1)
            flag=False
            

    return digits[::-1]
            
