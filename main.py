import os.path
import sys
import glob
import subprocess
from colorama import Fore


def get_clang_files(path):
    return glob.glob(path + '/**/*.c')

def compile_cfile(path):
    print(Fore.YELLOW + "compiling", os.path.basename(path))
    cp = subprocess.run(['gcc', path, '-lm'], encoding='utf-8', stdout=subprocess.PIPE)
    if cp.returncode != 0:
        print(Fore.RED + os.path.basename(path) + ' compile failed.', file=cp.stderr)

def autocompile():
    path = sys.argv[1]
    print(Fore.GREEN + "get list of c-lang files. path: ", path)
    # list
    files = get_clang_files(path)
    print(Fore.GREEN + "files: ", len(files))

    # compile
    for c_path in files:
        compile_cfile(c_path)

if __name__ == '__main__':
    autocompile()
