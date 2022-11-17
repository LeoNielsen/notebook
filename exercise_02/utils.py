import os

def get_file_names(folderpath,out='output.txt'):
    a = open(out, "w")
    for path, subdirs, files in os.walk('notebooks/my_notebooks/exercise_02/utils.py'):
        for filename in files:
            print(files)
            f = os.path.join(path, filename)
            a.write(str(f) + os.linesep) 

get_file_names("")

    