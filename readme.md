# Classification

### Overview
This program can detect objects in an image. The user provides a training image, and then a series of query images. THe program will detect the items in the query images.

### prerequisites
the following libraries need to be installed:

1. openCV
2. Matplotlib

you can install it from their website or by using `pip`:

```console
python3 -m pip install -U pip
python3 -m pip install -U matplotlib
python3 -m pip install -U opencv-python
```
Alternatively try replacing `python3` with `python` or `py` depending on your system

### Using the program 

First you must put all images required in the images folder. Name the training image `train.jpg`

To use the program, run the following in your terminal

```
python3 /directorypath/main.py
```  

replacing "my directorypath" with the directory path to your file

the program will list all images in the images fomlder and then propt with:
>enter the id of images you would like to use, seperated by a space, or leave it empty to use all:

to run it on all images, just press enter. If you want to see it run on images 2 and 4 for instance enter the following

```
2 4
```

The program will then return a list of coordinates of the detected object.

**contributors:**
- Shimon Jacobs
- Nastaran Keramati
- Safinaz Khalil
- Nadia Khodai
