"""
Docstring for a-Topics.Nested_Loop
Nested Loop = A loop within Another loop (Outer, Inner)
                Outer Loop:
                    Inner Loop:
"""

# Simple Loop
for i in range (1, 10):
    print(i, end=" ") # end=" ", using to print number in one line.
print()

# Nested Loop
for i in range(3):
    for j in range(1, 10):
        print(j, end=" ")
    print()

# A small project type nested loop
rows = int(input("Enter the number of Rows : "))
colums = int(input("Enter the number of colums : "))
symbol = input("Enter the symbol: ")

for i in range(rows):
    for y in range(colums):
        print(symbol, end="")
    print()