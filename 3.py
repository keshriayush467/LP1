n = int(input("Enter the no of items "))

profit = []
weight = []

for i in range(n):
    p = int(input("\nEnter the profit "))
    w = int(input("\nEnter the weight "))
    profit.append(p)
    weight.append(w)
    
capacity = int(input("\nEnter the capacity "))
    
ratio = []

for i in range(n):
    ratio.append(profit[i]/weight[i])

for i in range(n):
    for j in range(i+1, n):
        if ratio[i] < ratio[j]:
            ratio[i], ratio[j] = ratio[j] , ratio[i]
            profit[i] , profit[j] = profit[j] , profit[i]
            weight[i], weight[j]  = weight[j] , weight[i]
            
            
total_profit = 0

for i in range(n):
    if weight[i] <= capacity:
        total_profit += profit[i]
        capacity -=weight[i]  
    else:
        total_profit += ratio[i]* capacity
        break
    
print("\nThe Max profit is ", total_profit)
  