## Commands

### Encoding

`cwebp <input> -o <output> -lossless`

`cjxl <input> <output> --distance 0`

`avifenc <input> <output> -l`

`zopflipng <input> <output>`

`optipng <input> <output> -o7`

### Decoding

`dwebp <input> -o - -ppm > /dev/null`

`avifdec <input> -i`

`djxl <input>`

`pngtopnm <input> > /dev/null`

## Datasets

dataset sources

`testimages` from https://testimages.org/ SAMPLING_16BIT_RGB_2400x2400

`kodak` from https://r0k.us/graphics/kodak/

`sipi` from https://sipi.usc.edu/database/database.php?volume=misc

`clic` from https://clic2024.compression.cc/tasks/#image validation set

`emojis` from https://github.com/googlefonts/noto-emoji
