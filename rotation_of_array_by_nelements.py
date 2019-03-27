arr = [1, 2, 3, 4, 5, 6, 7] 
n = 7
d = t = 4
temp = arr[:d]

    
for a in range(n-d):
    arr[a]=arr[d]
    d+=1
i = 0
for a in range(n-t,n):
    arr[a] = temp[i]
    i+=1
    
#def printArray(arr, size): 
for i in range(n): 
    print ("% d"% arr[i], end =" ") 
    
    
#Time complexity : O(n)
#Auxiliary Space : O(d)
