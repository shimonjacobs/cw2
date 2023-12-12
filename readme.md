# Object Classifier

### Overview
This program can detect objects in an image. The user provides training images, and then a base image. THe program will detect the items from the training images in the base images.

### prerequisites
the following libraries need to be installed:

1. openCV
2. Matplotlib

you can install it from their website or by using `pip`:

```console
python3 -m pip install -U pip
python3 -m pip install -U matplotlib
python3 -m pip install -U opencv-contrib-python
```
>**Note:** Alternatively try replacing `python3` with `python` or `py` depending on your system

### Using the program 

First you must put all images required in the images folder. Name the base image `base.jpg`

>**Note:** the base image must be called `base.jpg`

To use the program, run the following in your terminal

```
python3 /directorypath/main.py
```  
replacing "my directorypath" with the directory path to your file

>**Note:** Alternatively try replacing `python3` with `python` or `py` depending on your system



the program will list all images in the images folder and then prompt you to select:

```
1. img1.jpg
2. img2.jpg
3. img3.jpg

enter the id of the training images you would like to use, seperated by a space, or leave it empty to use all:
```

to run it on all images, just press enter. If you want to see it run on images 1 and 3 for instance, enter the following:

```
1 3
```

The program will then return a list of coordinates of the detected object.

**contributors:**
- Shimon Jacobs
- Nastaran Keramati
- Safinaz Khalil
- Nadia Khodai
