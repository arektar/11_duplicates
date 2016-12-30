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
    for file1,file2 in itertools.combinations(file_list,2):
            if are_files_duplicates(file1,file2):
                print(file1 + "\n" + file2 + "\n")

