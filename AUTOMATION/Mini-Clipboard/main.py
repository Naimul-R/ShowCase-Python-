import sys
import clipboard 
import json

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