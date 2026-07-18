import sys
import clipboard 
import json

def save_items(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)


if len(sys.argv) == 2:
    command = sys.argv[1]
    
    if command == "save":
        print("Save")
    elif command == "load":
        print("Load")
    elif command == "list":
        print("List")
    else:
        print("Unknown Command!")
else:
    print("Please pass excatly one command!!")