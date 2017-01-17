import os
import filecmp
import itertools


def are_files_duplicates(file_path1, file_path_2):
    return bool(filecmp.cmp(file_path1, file_path_2))


def receive_all_file_ways(root):
    root = os.path.abspath(root)
    dict_of_files = {}
    for path, dirs, files in os.walk(root):
        for f_name in files:
            if f_name not in dict_of_files.keys():
                dict_of_files[f_name] = list()
            dict_of_files[f_name].append(path)
    return dict_of_files


def look_files(filedict):
    dict_of_equal_files = {}
    for name in list(filedict):
        if len(filedict[name]) > 1:
            for way1, way2 in itertools.combinations(filedict[name], 2):
                full_filename1 = os.path.join(way1, name)
                full_filename2 = os.path.join(way2, name)
                if are_files_duplicates(full_filename1, full_filename2):
                    if name not in dict_of_equal_files.keys():
                        dict_of_equal_files[name] = list()
                    if way1 not in dict_of_equal_files[name]:
                        dict_of_equal_files[name].append(full_filename1)
                    if way2 not in dict_of_equal_files[name]:
                        dict_of_equal_files[name].append(full_filename2)
    return dict_of_equal_files


if __name__ == '__main__':
    my_root = input("Write watching dir way: ")
    my_dict_of_files = receive_all_file_ways(my_root)
    my_dict_of_equal_files = look_files(my_dict_of_files)
    print("Duplicates:")
    for duplicate_file_name in list(my_dict_of_equal_files):
        for full_duplicate_filename in my_dict_of_equal_files[duplicate_file_name]:
            print(full_duplicate_filename)
        print()
