# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
array1 = [3,8]
array2 = [9,3,9]
print('array1', array1)
print('array2',array2)
print('#'*30)

def plus(array1, array2):
    array1 = array1[::-1]
    array2 = array2[::-1]
    if len(array1) - len(array2) > 0:
        array2+=[0]*(len(array1)-len(array2))
    else:
        array1+=[0]*(len(array2)-len(array1))
    ans = []
    carry = 0
    
    for i in range(max(len(array1), len(array2))):
        subans = array1[i] + array2[i] + carry
        ans.append(subans%10)
        carry = subans//10
    
    if carry!=0:
        ans+=[carry]
    return ans[::-1]
    
print('plusAns:',plus(array1, array2))
print('#'*30)

def multiply(array1, array2):
    array1 = array1[::-1]
    array2 = array2[::-1]
    if len(array1) - len(array2) > 0:
        array2+=[0]*(len(array1)-len(array2))
    else:
        array1+=[0]*(len(array2)-len(array1))
    
    ans = []
    
    for i in range(len(array1)):
        subAns = [0]*i
        subCarry = 0
        for j in range(len(array2)):
            subAns.append((array1[j]*array2[i]+subCarry)%10)
            subCarry = (array1[j]*array2[i]+subCarry)//10
        if subCarry!=0:
            subAns+=[subCarry]
        subAns = subAns[::-1]
        ans = plus(subAns, ans)

    return ans

print('multiplyAns:',multiply(array1, array2))


        
        
        
        
        