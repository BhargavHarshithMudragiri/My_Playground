#Script to update server.conf file using file operations in python

def update_server_config(filepath,key,value):
    with open(filepath,"r") as fileread:
        FileContent = fileread.readlines()
    
    with open(filepath,"w") as filewrite:
        for line in FileContent:
            if key in line:
                filewrite.write(key + " = " + value + "\n")
            else:
                filewrite.write(line)

update_server_config("server_config_file.conf","MAX_CONNECTIONS","600")