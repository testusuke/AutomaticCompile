import os.path
import sys
import glob
import subprocess

GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'

def get_clang_files(path):
    return glob.glob(path + '/**/*.c', recursive=True)

def compile_cfile(path):
    print(YELLOW + "compiling", os.path.basename(path))
    cp = subprocess.run(['gcc', path, '-lm'], encoding='utf-8', stdout=subprocess.PIPE)
    if cp.returncode != 0:
        print(RED + os.path.basename(path) + ' compile failed.', file=cp.stderr)
        return False
    else:
        print(GREEN + "compile successful.")
        return True

def autocompile():
    path = sys.argv[1]
    print(YELLOW + "get list of c-lang files. path: ", path)
    # list
    files = get_clang_files(path)
    files.sort()
    print(YELLOW + "files: ", len(files))

    # compile
    success = 0
    failed = 0
    for c_path in files:
        if compile_cfile(c_path):
            success += 1
        else:
            failed += 1

    print(GREEN + "All process finished.")
    print(GREEN + str(success) + " files compile successful.")
    print(RED + str(failed) + " files compile failed.")

if __name__ == '__main__':
    autocompile()
