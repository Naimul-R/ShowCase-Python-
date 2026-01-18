import os 

def create_file (filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename}: created successfully!")
    except FileExistsError:
        print(f"File name {filename} already exits!")

    except Exception as E:
        print("An error occurred!")


def view_all_file():
    files = os.listdir()
    if not files:
        print("No file is found!")
    else:
        print("Files in directory!")
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("An error occurred!")


def read_file(filename):
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(f"Content of '{filename}' :\n{content}")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")

    except Exception as e:
        print("An error occurred!")


def edit_file(filename):
    try:
        with open('sample.txt', 'a') as f:
            content = input("Enter data to add = ")
            f.write(content + "\n")
            print(f"Content added to {filename} successfully!")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")

    except Exception as e:
        print("An error occurred!")

