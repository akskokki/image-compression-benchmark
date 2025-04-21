import csv
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
    
    dataset_name = sys.argv[1]
    dataset_folder = f"datasets/{dataset_name}"

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
        ("avif", "encode", commands.avif_encode),
        ("jxl", "encode", commands.jxl_encode),
        ("png", "encode", commands.png_encode),
        ("webp", "decode", commands.webp_decode),
        ("avif", "decode", commands.avif_decode),
        ("jxl", "decode", commands.jxl_decode),
        ("png", "decode", commands.png_decode),
    ]

    log_file = "results.csv"
    fieldnames = ["format", "operation", "dataset", "time", "size"]
    write_header = not os.path.exists(log_file)

    print(f"Beginning benchmarks on {dataset_name}")

    with open(log_file, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()

        for fmt, op, cmd in tests:
            format_path = f"{dataset_folder}/{fmt}"

            if op == "encode":
                # Ensure empty destination folder for new files
                if os.path.isdir(format_path):
                    shutil.rmtree(format_path)
                os.mkdir(format_path)

            total_time = 0.0

            progress_counter = 0
            progress_milestone = round(len(image_names) / 10)

            for image_name in image_names:
                if op == "decode":
                    # Ensure image is cached for more consistent decoding benchmarks
                    subprocess.run(["touch", f"{format_path}/{image_name}"])
                t = time_command(cmd(dataset_folder, image_name))
                total_time += t

                progress_counter += 1
                if (progress_counter % progress_milestone == 0):
                    print(
                        f"\r{fmt} {op} {total_time:.4f} ({progress_counter} / {len(image_names)})",
                        end="",
                        flush=True
                    )

            writer.writerow({
                "format": fmt,
                "operation": op,
                "dataset": dataset_name,
                "time": total_time,
                "size": sum(os.path.getsize(f) for f in os.scandir(format_path))
            })

            print(f"\r{fmt} {op} {total_time:.4f}{20*' '}")


if __name__ == "__main__":
    main()
