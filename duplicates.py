import os, filecmp

def are_files_duplicates(file_path1, file_path_2):
    if filecmp.cmp(file_path1,file_path_2):
        return True
    return False


if __name__ == '__main__':
    root=input("Write watching dir way: ") + "\\"
    file_list = []
    for path, dirs, files in os.walk(root):
        for fname in files:
           file_list.append(os.path.join(path, fname))
    while file_list:
        file1=file_list.pop(0)
        for file2 in file_list:
            if are_files_duplicates(file1,file2):
                print(file1)
                print(file2)
                print()

