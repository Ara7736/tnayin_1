import os
import json
from collections import OrderedDict
import pathlib
import shutil

def Get_distribution(ara):
    """ This function will return the json """
    list_of_files_1 = os.listdir(ara)
    list_of_file_extension = []
    for i in list_of_files_1:
        filename, file_extension = os.path.splitext(i)
        list_of_file_extension.append(file_extension)
    set_of_list = set(list_of_file_extension)
    dict_of_esp = {}
    for i in set_of_list:
        count = 0
        for j in list_of_file_extension:
            if j == i:
                count += 1
        dict_of_esp[i] = count
    dict_of_esp_sorted = dict(sorted(dict_of_esp.items(), key=lambda item: item[1]))

    Json_file = json.dumps(dict_of_esp_sorted, indent=4)

    with open('Hakob.json', 'w') as Json_write:
        Json_write.write(Json_file)
    return Json_write

def Get_sizes(ara):
    """
    It will return the sizes of files in the list
    """
    tnayin_1 = pathlib.Path(ara)

    list_of_files_for_sizes = list(tnayin_1.iterdir())

    
    dict_of_sizes = {}
    for i in list_of_files_for_sizes:
        size = str(round((os.path.getsize(i))/(1024*1024),3)) + ' ' + 'MB'
        dict_of_sizes[size] = i.name 
    dict_of_sizes = dict(sorted(dict_of_sizes.items()))
    Json_file_1 = json.dumps(dict_of_sizes, indent = 4)
    with open('file_sizes.json', 'w') as Json_write_1:
        Json_write_1.write(Json_file_1)

def orginizer(ara):
    list_of_files_1 = os.listdir(ara)
    list_of_file_extension = []
    list_of_file_names = []
    for i in list_of_files_1:
        filename, file_extension = os.path.splitext(i)
        list_of_file_extension.append(file_extension)
        list_of_file_names.append(filename)
    set_of_list = set(list_of_file_extension)
    for i in set_of_list:
        my_path = ara + i + '_files'
        os.mkdir(my_path)
        for j in list_of_files_1:
            filename, file_extension = os.path.splitext(j)
            if file_extension == i:

                shutil.move(ara + j, my_path)




if __name__ == "__main__":
    # print(Get_distribution(ara= "C:/Users/ara.sedrakyan/Desktop/Presentations"))
    # print(Get_sizes(ara= "C:/Users/ara.sedrakyan/Desktop/Presentations"))
    print(orginizer(ara = "C:/Users/ara.sedrakyan/Desktop/Presentations/"))

