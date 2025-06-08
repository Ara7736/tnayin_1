# we need to import libraries like os and json
import os
import json

#"""" for receiving the list of files in the folder we need to use os
# the listdir from os 
# after we create an list and add in it the extensions of the files
# for that purpose we use path.splitext() function form os"


tnayin = "C:/Users/ara.sedrakyan/Desktop/tnayin_1/My_Files"
list_of_files_1 = os.listdir(tnayin)
list_of_file_extension = []
for i in list_of_files_1:
    filename, file_extension = os.path.splitext(i)
    list_of_file_extension.append(file_extension)

#""""" To finde the count of each type of extensions in the list 
# and present it in the dictonary we define a dictonary and after looping
# we found our dictonary
set_of_list = set(list_of_file_extension)
dict_of_esp = {}
for i in set_of_list:
    count = 0
    for j in list_of_file_extension:
        if j == i:
            count += 1
    dict_of_esp[i] = count
dict_of_esp_sorted = dict(sorted(dict_of_esp.items(), key=lambda item: item[1]))
#"" To save 
Json_file = json.dumps(dict_of_esp_sorted, indent=4)
print(Json_file)
with open('Mano.json', 'w') as Json_write:
    Json_write.write(Json_file)