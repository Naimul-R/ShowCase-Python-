"""
🧩 Scenario — Student Score Manager
📝 Requirements
    1. Create an empty list called scores.
    2. Ask the user to enter 5 student scores (use loop).
    3. Perform the following operations in order:
        Step A — Add Operations
            -Append one extra score (user input).
            -Insert score 50 at index position 2.
        Step B — Remove Operations
            -Remove the first occurrence of a score entered by the user.
            -Pop the last score and store it in a variable called removed_score.
        Step C — Analysis
            -Count how many times score 75 appears.
            -Find the index of score 100 (if it exists).
        Step D — Organize Data
            -Sort the list in ascending order.
            -Reverse the list (so it becomes descending).
    4. Print:
        Final score list
        Removed score
        Count of 75
        Index of 100 (or a message if not found)
"""
# Step 1 - Create an empty list
scores = []

# Take 5 student scores
print("Enter 5 student scores:")

for i in range(5):
    score = int(input(f"Score {i+1}: "))
    scores.append(score)

# ----------------------------
# Step A — Add Operations
# ----------------------------
extra_score = int(input("Enter extra score: "))
scores.append(extra_score)

# Insert 50 at index 2 position
scores.insert(2, 50)

# ----------------------------
# Step B — Remove Operations
# ----------------------------
remove_value = int(input("Enter the score you want to remove: "))

if remove_value in scores:
    scores.remove(remove_value)
else:
    print("Score not found, Invalid score!")

# Pop the last score
remove_score = scores.pop()

# ----------------------------
# Step C — Analysis
# ----------------------------
count = scores.count(75)

# Find index of 100 safety
if 100 in scores:
    index_100 = scores.index(100)
else:
    index_100 = "Index 100 is not found in the scores boad."

# ----------------------------
# Step D — Organize Data
# ----------------------------

# Sort Ascending
scores.sort()

# Descending or reverse data
scores.reverse()

# ----------------------------
# Final Output
# ----------------------------
print("\n===== Final Output =====")
print("inal Score = ",scores)
print("Removed Score = ", remove_value)
print("Count of 75 = ", count)
print("Index of 100 = ", index_100)