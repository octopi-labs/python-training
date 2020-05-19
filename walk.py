import os
from os import walk
from pprint import  pprint

basepath = os.path.dirname(__file__)
files = {}

for dirpath, dirnames, filenames in os.walk(basepath):
    if ("venv" not in dirpath and
        "__pycache__" not in dirpath and
        ".git" not in dirpath and
        ".pytest_cache" not in dirpath and
        ".vscode" not in dirpath and
        ".sonarlint" not in dirpath):

        file_list = [name for name in filenames if ".py" in name and ".pyc" not
                     in name]
        files[dirpath] = sorted(file_list)

pprint(files)

if files:
    for dir, file_list in files.items():
        counter = 0
        for file in file_list:
            counter += 1
            if "ex" in file:
                source = dir + os.sep + file
                destination = dir + os.sep + "ex{0}.py".format(counter)
                os.rename(source, destination)

