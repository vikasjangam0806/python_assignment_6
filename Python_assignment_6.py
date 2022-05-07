#Q-1 Python program to add two Matrices
# Program to add two matrices using nested loop
 
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)

#Q-2 Python program to multiply two matrices
# Program to multiply two matrices using nested loops
 
# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix   
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
     
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
 
# iterating by row of A
for i in range(len(A)):
 
    # iterating by column by B
    for j in range(len(B[0])):
 
        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
 
for r in result:
    print(r)

#Q-3 Python program for Matrix Product
# Python3 code to demonstrate
# Matrix Product
# Using list comprehension + loop
  
# getting Product
def prod(val) :
    res = 1 
    for ele in val:
        res *= ele
    return res 
  
# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
  
# printing original list
print("The original list : " + str(test_list))
  
# using list comprehension + loop
# Matrix Product
res = prod([ele for sub in test_list for ele in sub])
  
# print result
print("The total element product in lists is : " + str(res))

#Q-4 Adding and Subtracting Matrices in Python
# Program to add two matrices using nested loop
 
X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] - Y[i][j]
 
for r in result:
    print(r)

#Q-5 Transpose a matrix in Single line in Python
m = [[1,2],[3,4],[5,6]]
for row in m :
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
    print(row)

#Q-6 Python | Matrix creation of n*n
# Python3 code to demonstrate
# matrix creation of n * n
# using list comprehension
  
# initializing N
N = 4
  
# printing dimension
print("The dimension : " + str(N))
  
# using list comprehension
# matrix creation of n * n
res = [list(range(1 + N * i, 1 + N * (i + 1)))
                            for i in range(N)]
  
# print result
print("The created matrix of N * N: " + str(res))



#Q-7 Python | Get Kth Column of Matrix
# Python3 code to demonstrate working of
# Get Kth Column of Matrix
# using list comprehension
  
# initialize list
test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initialize K
K = 2
  
# Get Kth Column of Matrix
# using list comprehension
res = [sub[K] for sub in test_list]
  
# printing result
print("The Kth column of matrix is : " + str(res))

#Q-8 Python – Vertical Concatenation in Matrix
# Python3 code to demonstrate working of 
# Vertical Concatenation in Matrix
# Using loop
  
# initializing lists
test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]
  
# printing original list
print("The original list : " + str(test_list))
  
# using loop for iteration
res = []
N = 0
while N != len(test_list):
    temp = ''
    for idx in test_list:
          
        # checking for valid index / column
        try: temp = temp + idx[N]
        except IndexError: pass
    res.append(temp)
    N = N + 1
  
res = [ele for ele in res if ele]
  
# printing result 
print("List after column Concatenation : " + str(res))

#Q-9 Python program to check if a string is palindrome or not
# function which return reverse of a string
 
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

 #Q-10 Python program to check whether the string is Symmetrical or Palindrome
# Python program to demonstrate
# symmetry and palindrome of the
# string
 
 
# Function to check whether the
# string is palindrome or not
def palindrome(a):
  
    # finding the mid, start
    # and last index of the string
    mid = (len(a)-1)//2     #you can remove the -1 or you add <= sign in line 21 
    start = 0                #so that you can compare the middle elements also.
    last = len(a)-1
    flag = 0
 
    # A loop till the mid of the
    # string
    while(start <= mid):
  
        # comparing letters from right
        # from the letters from left
        if (a[start]== a[last]):
             
            start += 1
            last -= 1
             
        else:
            flag = 1
            break;
             
    # Checking the flag variable to
    # check if the string is palindrome
    # or not
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")
         
# Function to check whether the
# string is symmetrical or not       
def symmetry(a):
     
    n = len(a)
    flag = 0
     
    # Check if the string's length
    # is odd or even
    if n%2:
        mid = n//2 +1
    else:
        mid = n//2
         
    start1 = 0
    start2 = mid
     
    while(start1 < mid and start2 < n):
         
        if (a[start1]== a[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break
      
    # Checking the flag variable to
    # check if the string is symmetrical
    # or not
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
         
# Driver code
string = 'amaama'
palindrome(string)
symmetry(string)