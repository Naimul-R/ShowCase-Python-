"""
Docstring for a-Topics.Nested Loop.Patterns
"""
# Patter-1
for i in range(5):
    for y in range(1, 6):
        print("*", end=" ")
    print()

# Patter-2
r = 5
for i in range(1, r+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

#Patter-3
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Patter-4
n = 6
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Patter-5
n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()