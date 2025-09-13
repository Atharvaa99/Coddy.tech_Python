prices = input().split(',')
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(',')
budget = int(input())

affordable_items = []
total_budget_needed = 0
cant_afford = 0

for index, item in enumerate(items):
    if prices[index] <= budget:
        total_budget_needed += prices[index]
        affordable_items.append(item)
    else:
        cant_afford += 1

print(f"Can buy: {affordable_items}")
print(f"Total budget needed: {total_budget_needed}")
print(f"Can't afford: {cant_afford}")
