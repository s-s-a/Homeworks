import os

file_to_del = 'temp.tmp'
dir_to_del = 'temp_dir'

if os.path.isfile(file_to_del):
    os.remove(file_to_del) # Для файлов используем os.remove()

if os.path.isdir(dir_to_del):
    os.rmdir(dir_to_del)   # Для пустых директорий — os.rmdir()
