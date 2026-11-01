def non_recursive(n):
    a,b = 0,  1
    for i in range(n):
        print(a, end=" ")
        a,b = b, a+b
    
def recursive(n):
     if  n<=1:
         return n
     else:
         return recursive(n-1) + recursive(n-2)


n = int(input("Enter the val of n = "))

print("Non Recursive ")
non_recursive(n)
    
print("\nRecursive")
for i in range(n):
    print(recursive(i), end=" ")    