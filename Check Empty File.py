import os

# check if size of file is 0
path_delisted = "/dbfs/FileStore/tables/FirstRate30mins_Delisted"

for filename_delisted in os.listdir(path_delisted):
    if os.stat(filename_delisted).st_size == 0:
        print(f'File {filename_delisted.split("_")[0]} is empty')
        dbutils.fs.rm("/FileStore/tables/FirstRate30mins_Delisted/" + filename_delisted)
