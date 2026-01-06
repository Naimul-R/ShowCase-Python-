row = 5
for i in range(1, row + 1):
    print(" " * (row - i ), end="")
    for j in range(1, i + 1):
        print(j, end= " ")
        
    print()