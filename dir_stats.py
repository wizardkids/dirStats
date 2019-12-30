"""
dir_stats.py

Richard E. Rawson
2019-12-04

Program Description:
GOAL: dirStats is a disk usage statistics viewer and cleanup tool for Microsoft Windows (all current variants). dirStats reads the whole directory tree once and then presents it in three useful views: the directory list, which resembles the tree view of the Windows Explorer but is sorted by file/subtree size; the treemap, which shows the whole contents of the directory tree straight away; and the extension list, which serves as a legend and shows statistics about the file types.
"""

import os
from glob import glob
from pathlib import Path

import win32com.client as com


def formatted_directories(root_dir):
    """
    Given a path, generate a formatted list of folder and subfolders.

    Arguments:
        root_dir {str} -- a valid path
    """


root_dir = 'C:\\temp'
os.chdir(root_dir)

# does not appear to be recursive
obj = os.scandir()
# List all files and diretories
# in the specified path
print("Files and Directories in '% s':" % root_dir)
for entry in obj:
    # if entry.is_dir() or entry.is_file():
    print(entry.name)
    print(entry.stat(follow_symlinks=True).st_size)

print('\n')
# The following won't work on some folders
# due to lack of permission
fso = com.Dispatch("Scripting.FileSystemObject")
folder = fso.GetFolder(root_dir)
print(folder.size, 'bytes')
print(folder.size / 1024, 'KB')
print(folder.size / 1024 / 1024, 'MB')

exit()

# get the name of the root dir, the one folder that is common
# to rest of the folders
common_folder = Path(root_dir).parts[-1]

# get the number of directories
d = Path(root_dir).glob('**/**')
num_dirs = sum(1 for _ in d)

d = Path(root_dir).glob('**/**')
# first folder is the root folder
last_folder = root_dir
cnt = 0
for i in range(num_dirs):
    next_d = Path(next(d))

    # get the path relative to "common_folder"
    directory = os.path.relpath(next_d, Path(root_dir))

    # indent directory depending on how many backslashes there are
    ndent = ' ' * 3 * (directory.count('\\') + 1)

    # first, print the common folder; then print the rest
    # indenting as appropriate for the level of the folder
    if i == 0:
        print(Path(common_folder))
    else:
        print(ndent, directory)


if __name__ == '__main__':
    pass
    # formatted_directories('')
