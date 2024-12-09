import os 

# os.rename("main.py", "nafi.py")
# def remove_file(filename = input("Enter file name?")):
#     try:
#         os.remove(filename)
#         print(f"The file {filename} has been removed.")
#     except FileNotFoundError:
#         print(f"The file {filename} does not exist.")
        

def create_file(filename = input("Enter file name?")):
    try:
        with open(filename, "w") as f:
            f.write("")
    except Exception as e:
        print(f"An error occured: {e}")
        
# create_file()

def read_file(filename = input("Enter file name?")):
    try:
        with open(filename) as f:
            content = f.read()
        print(content)
    except Exception as e:
        print(f"Unexpected error: {e}")
        
read_file()