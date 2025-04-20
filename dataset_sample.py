import os
import random
import shutil
import sys

def main():
    src_folder = "datasets/" + sys.argv[1]
    dst_folder = "datasets/" + sys.argv[2]
    num_files = int(sys.argv[3])

    all_files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]

    selected_files = random.sample(all_files, min(num_files, len(all_files)))


    os.mkdir(dst_folder)
    for file in selected_files:
        shutil.copy(os.path.join(src_folder, file), os.path.join(dst_folder, file))

if __name__ == "__main__":
    main()