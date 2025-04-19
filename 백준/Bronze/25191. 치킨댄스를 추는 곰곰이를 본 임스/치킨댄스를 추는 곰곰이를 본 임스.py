chicken = int(input())
cola, beer = map(int, input().split())
print(min(cola // 2 + beer, chicken))