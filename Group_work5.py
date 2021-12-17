# ----1---
def count_digit(num_list):
    set1 = set(num_list)
    list1 = list(set1)
    dict_ = {}
    for i in list1:
        result = num_list.count(i)
        dict_[i] = result
    return dict_


num_list = [1, 1, 3, 2, 1, 3, 4]
print(count_digit(num_list))

# --------2--------
import os


def get_extention(data):
    result_list = []
    list_files = []
    if isinstance(data, str):
        dir_ = os.walk(data)
        for i in dir_:
            for j in i[2]:
                list_files.append(j)
        result_list = validate_ext(list_files)
    else:
        result_list = validate_ext(data)
    return result_list


def validate_ext(extensions):
    result_list = []
    for i in extensions:
        name_file = os.path.splitext(i)
        result = name_file[1].replace('.', '')
        if result == '':
            raise EOFError("Расширение отсутсвует")
        result_list.append(result)
    return result_list


print(get_extention(["help.docx", "koka.txt", "main.pdf", "test.txt", "test1.csv"]))