# Image Compression Benchmark

This is a simple command line Python tool to aid in comparing the performances of different image compression algorithms, namely lossless WebP, AVIF, JPEG XL and PNG. By adding your own commands to `commands.py`, you can use it to test other file formats as well.

The program was created for use in my Bachelor's thesis exploring the differences between modern lossless image formats and PNG.

## Usage

Place the image datasets you wish to use under subdirectories of the `datasets` folder. The path for each individual image should be of the form `datasets/<dataset_name>/<image_name>`.

Before you run the program, you will have to ensure that all necessary encoding/decoding packages are installed on your system. See [Packages for encoding/decoding](#packages-for-encodingdecoding).

After this, run

```
python benchmark.py <dataset_name>
```

to re-encode the images in the different formats and log the results. The newly created images can be found under `datasets/<dataset_name>/<format_name>/`

You can see the raw data in `results.csv`, or view the aggregated averages from multiple tests in `results_formatted.ods`. Do note that you will have to edit this spreadsheet in order to have it correctly linked to the data on your file system and use the names of the datasets you're using.

`dataset_sample.py` is a helper script you can use to create a smaller sample of images from a larger dataset. It can be called with three arguments: dataset name, new dataset name, and sample size. This can be useful if the original dataset in its entirety is too large to run through in a reasonable amount of time. 

## Packages for encoding/decoding

- `libwebp` for WebP
- `libavif` for AVIF
- `libjxl` for JPEG XL
- `ImageMagick` and `netpbm` for PNG

### Commands

These are the encoding/decoding commands that are being used through `commands.py` to perform the benchmarks.

#### WebP

`cwebp <input> -o <output> -lossless`

`dwebp <input> -o - -ppm > /dev/null`

#### AVIF

`avifenc <input> <output> -l`

`avifdec <input> -i`

#### JPEG XL

`cjxl <input> <output> --distance 0`

`djxl <input>`

#### PNG

`convert <input> <output>`

`pngtopnm <input> > /dev/null`

## Datasets

The image datasets you use with the program should be placed within subdirectories of the `datasets` folder.

For licensing reasons, I will not be redistributing the specific datasets I personally used in my research. You can find them from the following links.

### Dataset sources

`testimages` from https://testimages.org/ - SAMPLING_8BIT_RGB_2400x2400

`kodak` from https://r0k.us/graphics/kodak/

`clic` from https://clic2024.compression.cc/tasks/#image - Validation set

`emojis` from https://github.com/googlefonts/noto-emoji

`medical` from https://bbbc.broadinstitute.org/BBBC038
