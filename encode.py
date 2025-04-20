import os
import shutil
import subprocess
import sys
import time

import commands

def time_command(cmd):
    start = time.perf_counter()
    subprocess.run(
        " ".join(cmd),
        shell=True,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    end = time.perf_counter()
    return end - start

def main():
    if len(sys.argv) < 2:
        print("No dataset name given")
        return
    
    dataset_folder = f"datasets/{sys.argv[1]}"

    if not os.path.isdir(dataset_folder):
        print(f"Dataset {dataset_folder} does not exist")
        return

    image_names = []

    for file in os.listdir(dataset_folder):
        if not os.path.isfile(f"{dataset_folder}/{file}"): continue
        if not file.lower().endswith(".png"): continue
        image_names.append(file[:-4])


    tests = [
        ("webp", "encode", commands.webp_encode),
        # ("avif", "encode", commands.avif_encode),
        # ("jxl", "encode", commands.jxl_encode),
        # ("webp", "decode", commands.webp_decode),
        # ("png", "decode", commands.png_decode),
        # ("jxl", "decode", commands.jxl_decode)
    ]

    for fmt, op, cmd in tests:
        folder_path = f"{dataset_folder}/{fmt}"

        # Ensure empty destination folder for new files
        if op == "encode":
            if os.path.isdir(folder_path):
                shutil.rmtree(folder_path)
            os.mkdir(folder_path)

        encoding_time = 0.0

        count = 0
        for image_name in image_names:
            if op == "decode":
                subprocess.run(["touch", f"{folder_path}/{image_name}"])
            duration = time_command(cmd(dataset_folder, image_name))
            encoding_time += duration

            count += 1
            if count%100 == 0: print(count)

        print(fmt, op, encoding_time)
    return


if __name__ == "__main__":
    main()
