import os
import filecmp
import itertools


def are_files_duplicates(file_path1, file_path_2):
    if filecmp.cmp(file_path1, file_path_2):
        return True
    return False


def take_files(root):
    file_dict = {}
    for path, dirs, files in os.walk(root):
        for f_name in files:
            if f_name not in file_dict.keys():
                file_dict[f_name] = list()
            file_dict[f_name].append(path)
    return file_dict


def look_files(filedict):
    equal_list = []
    for name in list(filedict):
        if len(filedict[name]) > 1:
            for way1, way2 in itertools.combinations(filedict[name], 2):
                if are_files_duplicates(way1 + "\\" + name, way2 + "\\" + name):
                    equal_list.append((way1 + "\\" + name, way2 + "\\" + name))
    return equal_list


if __name__ == '__main__':
    my_root = input("Write watching dir way: ") + "\\"
    my_file_dict = take_files(my_root)
    my_equal_list = look_files(my_file_dict)
    for couple in my_equal_list:
        print(couple[0])
        print(couple[1])
        print()
