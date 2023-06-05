from os import getcwd, path, mkdir, listdir
from shutil import move
from colorama import init, Fore

__version__ = 1.0
__author__ = 'Rafael'
__github__ = 'https://github.com/RafaelHorta?tab=repositories'
__doc__ = 'Organize files by extension'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CURRENT_PATH = getcwd()
EXTENSIONS_LIST = {
    'pictures': ['png', 'jpg', 'jpeg', 'gif'],
    'videos': ['mp4', 'mkv', 'avi'],
    'audio': ['mp3', 'wav', 'ogg'],
    'office': ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf'],
    'notes': ['txt', 'py'],
    'zips': ['zip', 'rar']
}
count_directories = 0
count_files_moved = 0

init() # Initialize colorama

"""
- - Moves files from the origin path to the destiny path and counts them
"""

def move_files(origin, destiny):
    global count_files_moved

    move(origin, destiny)

    count_files_moved += 1

    print(f'{Fore.BLUE}-- MOVE FILE {Fore.YELLOW}{origin}{Fore.BLUE} TO DIRECTORY {Fore.WHITE}{destiny}{Fore.RESET}')

"""
- - Create destination directories if don't exist and count the new directory
"""

def make_directory(dirname):
    global count_directories

    if not path.exists(dirname):
        mkdir(dirname)

        print(f'{Fore.MAGENTA}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(f'{Fore.BLUE}- MAKE DIRECTORY {Fore.WHITE}{dirname}{Fore.RESET}')
        print(f'{Fore.MAGENTA}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

        count_directories += 1

"""
- - Validate if the file extension is in the extensions list and then proceed to make and move
"""

def validate_extension(filename):
    for dirname, extensions in EXTENSIONS_LIST.items():
        name, ext = path.splitext(filename)

        if ext[1:] in extensions:
            make_directory(dirname)
            move_files(filename, dirname)

if __name__ == '__main__':
    print(f'{Fore.BLUE}CURRENT DIRECTORY {Fore.RED}{CURRENT_PATH}{Fore.RESET}\n')

    for name in listdir():
        if path.isfile(name) and name not in __file__:
            validate_extension(name)

    print(f'\n{Fore.MAGENTA}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print(f'{Fore.BLUE}DIRECTORIES CREATED: {Fore.CYAN}{count_directories}')
    print(f'{Fore.BLUE}FILES MOVED: {Fore.CYAN}{count_files_moved}\n')
