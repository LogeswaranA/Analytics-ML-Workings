import os
folderpath = "../files"
file_path = os.path.join(folderpath, 'employee.csv')
print(file_path)
# Open and read the file
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print(lines)
    # Extract header
    header = lines[0].strip().split(',')
    data = [dict(zip(header,line.strip().split(','))) for line in lines][1:]
    
    #data = [dict(zip(header,line.strip.split('1'))) for line in lines[1:]]

    print(data)
    print(header)
else:
    print("no files")