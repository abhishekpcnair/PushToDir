import os 
from collections import Counter

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

files = [f for f in os.listdir('.') if os.path.isfile(f)]
extension_list = []
for f in files:
    extension_list.append(os.path.splitext(f)[1][1:].strip().lower())

extension_list = list(filter(None, extension_list))
print('File extensions available are',set(extension_list))

for i in set(extension_list):
    folder_name = i
    path = dir_path+'/'+folder_name
    if(os.path.exists(path) is False):
        os.mkdir(folder_name)


for f in files:
    ext = os.path.splitext(f)[1][1:].strip().lower()
    old_path = dir_path+'/'+f
    new_path = dir_path+'/'+ext+'/'+f
    os.rename(old_path,new_path)
    print('Moving to the new Path ->',new_path)

