import glob
import sys


def main():
    texfiles = get_tex_file(get_args())
    if yes_no_input():
        try:
            for texfile in texfiles:
                replace_comma(texfile)
            print("\033[32m" + "success!!" + "\033[0m")
        except Exception as e:
            print(e)
    else:
        sys.exit()


# Get the directory path with command line arguments
def get_args():
    if len(sys.argv) == 1:
        print("\033[31m" + "error" + "\033[0m")
        print("\033[31m" + "usage: python main.py [directory]" + "\033[0m")
        sys.exit()
    else:
        dir_path = sys.argv[1]
        print("dir path:", dir_path)
        return dir_path


# Recursively retrieve tex files in a directory
def get_tex_file(dir_path):
    tex_file_list = glob.glob(dir_path + "**" + "/*.tex", recursive=True)
    if len(tex_file_list) == 0:
        print("error")
        print("no tex file found")
        sys.exit()
    else:
        print("tex file:", tex_file_list)
        return tex_file_list


# Replace dokuten and kuten to comma and period
def replace_comma(filename):
    with open(filename, "r") as f:
        lines = f.read()
    lines = lines.replace("、", "，")
    lines = lines.replace("。", "．")
    with open(filename, "w") as f:
        f.write(lines)


# Ask user whether to continue
def yes_no_input():
    while True:
        choice = input("置換を開始しても良いですか？" + " (y/n): ").lower()
        if choice in ["y", "ye", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False


if __name__ == "__main__":
    main()
