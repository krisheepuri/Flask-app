def read_func(name, username, password, dob, file_path):
    data = open(file_path, "r")
    data = data.read()
    data_values = data.split(",")
    if name in data_values:
        return ("Name is taken")
        
    if username in data_values:
        return ("username is taken")
    data_new = open(file_path, "a")
    data_new.write(f'\n{name}, {username}, {password}, {dob}')
    data_new.close()







































            
