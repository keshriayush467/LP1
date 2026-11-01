n = int(input("\nEnter the no of items "))

profit = []
weight = []
for i in range(n):
    
    profit.append(int(input("\nEnter the profit ")))
    weight.append(int(input("\nEnter the weight ")))

capacity = int(input("\nEnter the capacity "))


dp = [[0]* (capacity+1)  for i in range(n+1)]


for i in range(1,n+1):
    for w in range(capacity+1):
        if weight[i-1] <=w:
            dp[i][w] = max( profit[i-1] + dp[i-1][w- weight[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]

print("Max Profit ", dp[n][capacity])

