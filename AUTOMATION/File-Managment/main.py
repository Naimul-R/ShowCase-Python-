import os 

source_dir = "C:/Users/anony/Downloads"

with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)