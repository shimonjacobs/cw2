# Object Classifier

### Overview
This program can detect objects in an image. The user provides training images, and then a base image. The program will detect the items from the training images in the base images.

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

To use the program, run the following in your terminal

```
python3 /directorypath/main.py
```  
replacing "my directorypath" with the directory path to your file

>**Note:** Alternatively try replacing `python3` with `python` or `py` depending on your system

The program will prompt you to enter the number of training images you would like to use: enter a number.

```
Enter the number of images you want to use:
>>> 3
```

The program will ask you to enter the paths of those files:
```
Enter the object 1 image:
>>> /myfilepath/query_1.jpg
```
replacing `myfilepath` with the path to the file.

After entering your query (training) images, it will prompt you to enter the base image:
```
Enter the base image:
>>> /myfilepath/base.jpg
```

The program will then return images showing the steps of identifying the objects, as well as the coordinates of the bounding boxes for the detected images

**contributors:**
- Shimon Jacobs
- Nastaran Keramati
- Safinaz Khalil
- Nadia Khodai
