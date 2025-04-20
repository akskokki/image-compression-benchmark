def webp_encode(dataset_folder, image_name):
    return [
        "cwebp",
        "-lossless",
        f"{dataset_folder}/{image_name}.png",
        "-o", f"{dataset_folder}/webp/{image_name}.webp",
    ]

def webp_decode(dataset_folder, image_name):
    return [
        "dwebp",
        f"{dataset_folder}/webp/{image_name}.webp",
        "-ppm",
        "-o - > /dev/null",
    ]

def avif_encode(dataset_folder, image_name):
    return [
        "avifenc",
        "-l",
        f"{dataset_folder}/{image_name}.png",
        f"{dataset_folder}/avif/{image_name}.avif",
    ]

def jxl_encode(dataset_folder, image_name):
    return [
        "cjxl",
        "-d 0",
        f"{dataset_folder}/{image_name}.png",
        f"{dataset_folder}/jxl/{image_name}.jxl",
    ]

def jxl_decode(dataset_folder, image_name):
    return [
        "djxl",
        f"{dataset_folder}/jxl/{image_name}.jxl",
    ]

def png_encode(dataset_folder, image_name):
    return [
        "zopflipng",
        f"{dataset_folder}/{image_name}.png",
        f"{dataset_folder}/png/{image_name}.png",
    ]

def png_decode(dataset_folder, image_name):
    return [
        "pngtopnm",
        f"{dataset_folder}/png/{image_name}.png",
        "> /dev/null"
    ]