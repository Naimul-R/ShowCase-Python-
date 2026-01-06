n = 6

#for i in range(n, 0, -1): #for reverse patten

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()