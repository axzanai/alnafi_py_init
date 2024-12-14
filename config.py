import os 

def create_file(filename):
    try:
        if os.path.exists(filename):
            print(f"File {filename} already exist.")
            return
    
        else:
            with open(filename, "w") as file:
                file.write("")
                print(f"File {filename} ")
    
    except FileExistsError:
        print(f"File {srcname} not found.")
    except PermissionError:
        print("Permission denied. Check your file permissions.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")        

def rename_file(srcname, dstname):
    try:
        if not os.path.exists(srcname):
            print(f"Source file {srcname} does not exist.")
            return
        
        if os.path.exists(dstname):
            print(f"Destination file {dstname} already exist.")
        
        os.rename(srcname, dstname)
        print(f"File name updated from {srcname} to {dstname}.")
    except FileExistsError:
        print(f"File {srcname} not found.")
    except PermissionError:
        print("Permission denied. Check your file permissions.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
               
def remove_file(filename):
    try:
        if not os.path.exists(filename):
            print(f"File {filename} does not exist.")
            return
        
        os.remove(filename)
        print(f"{filename} removed successfully")
        
    except FileExistsError:
        print(f"File {filename} not found.")
    except PermissionError:
        print("Permission denied. Check you file permissions.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
    

def read_file(filename = input("Enter file name?")):
    try:
        with open(filename) as f:
            content = f.read()
        print(content)
    except Exception as e:
        print(f"Unexpected error: {e}")
        
read_file()

