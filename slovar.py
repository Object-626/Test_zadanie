import os

def search_file_js(folder_list, N):
    #функция осуществляющая поиск файлов формата .js
    js_folders = []
    #Список содержащий пути к файлам формата .js
    for i in folder_list:
        js_count = 0
        for j, _, files in os.walk(i):
            if not any(file.endswith('.js') for file in files):
                continue
            if not any(os.path.isdir(os.path.join(j, folder)) for folder in os.listdir(j)):
                js_folders.append(j)
                js_count += len([file for file in files if file.endswith('.js')])
                if js_count == 0:
                    continue
                js_folders.append(js_count)
                js_count = 0
    dict_folders = {js_folders[i]: js_folders[i + 1] for i in range(0, len(js_folders), 2)}
    dict_generator = [{} for _ in range(N)]
    dict_folders = sorted(dict_folders.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = 0
    for i in range(len(dict_folders)):
        sorted_dict = sorted(dict_generator, key=lambda x: sum(x.values()))
        sorted_dict[0][dict_folders[i][0]] = dict_folders[i][1]
    return sorted_dict
dir_list = [
    r'C:\Users\попытка №6\Desktop\A',
    r'C:\Users\попытка №6\Desktop\B'
]
#Внесите в список dir_list пути к папкам содержащим файлы формата .js
print(search_file_js(dir_list, 3))