#!/bin/sh
# A shell script to optimize and lossily compress the Quran PNG images.
# This script requires oxipng & pngquant to be installed & added to PATH.
# Author : Abdallah Abdelazim

echo "STEP 1"
echo ">>> Optimization (lossless compression) with oxipng"
oxipng -o 3 -i 1 --strip safe *.png

echo "STEP 2"
echo ">>> Applying lossy compression on images using pngquant"
pngquant --force --ext=.png --skip-if-larger --speed 1 --strip --verbose 16 *.png

echo "STEP 3"
echo ">>> Reoptimization (lossless compression) with oxipng"
oxipng -o 3 -i 1 --strip safe *.png
