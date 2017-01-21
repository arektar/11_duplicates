import os
import filecmp
import itertools
import collections
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("root_file_path", type=str, )
    args = parser.parse_args()
    root_file_path = args.root_file_path
    return root_file_path


def are_files_duplicates(file_path1, file_path_2):
    return bool(filecmp.cmp(file_path1, file_path_2))


def receive_all_file_ways(root):
    root = os.path.abspath(root)
    dict_of_files = collections.defaultdict(list)
    for path, dirs, files in os.walk(root):
        for f_name in files:
            dict_of_files[f_name].append(path)
    return dict_of_files


def look_files(filedict):
    dict_of_equal_files = collections.defaultdict(set)
    for name, paths in filedict.items():
        if len(paths) <= 1:
            continue
        for first_file_path, second_file_path in itertools.combinations(paths, 2):
            full_filename1 = os.path.join(first_file_path, name)
            full_filename2 = os.path.join(second_file_path, name)
            if are_files_duplicates(full_filename1, full_filename2):
                dict_of_equal_files[name].add(full_filename1)
                dict_of_equal_files[name].add(full_filename2)
    return dict_of_equal_files


if __name__ == '__main__':
    my_root = parse_arguments()
    my_dict_of_files = receive_all_file_ways(my_root)
    my_dict_of_equal_files = look_files(my_dict_of_files)
    print("Duplicates:")
    for duplicate_file_name in list(my_dict_of_equal_files):
        for full_duplicate_filename in my_dict_of_equal_files[duplicate_file_name]:
            print(full_duplicate_filename)
        print()
