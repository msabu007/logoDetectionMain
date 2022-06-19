# Logo detection Model

## project structure

1. images folder : the folder contains the images used training, it hast the jpg files as well as the label annotated xml files as well.
2. output folder : the folder used to save the cropped image after the logo detection
3. preprocessing.ipynb : contains the image augmentation steps for preparing the training dataset
4. testCode.ipynb : contains all the steps of the total process from data loading, data preprocessing, model training and model checking and finally the dtected logo cropping.
5. model_weights.pth : the saved model object, which can be resued 
6. requirements.txt : list of all the package used in the project
7. main.py : the run file for the fastApi
8. components.py : support functions for the main.py

## Dataset

There are mainly 6 unique images. these images are then augmented to for a total of 47 images, which the training dataset. some of the images are horizontally or vertically flipped and some are rotated to make the augmentation. the details of the augmentation process are in the prepocessing.ipynb

## running the app

1. create a vritualenivironment, if the you anaconda python interpreter, create one using that or create a an environment using python with follwing code

`` c:\>python -m venv c:\path\to\myenv ``

2. open a empty folder, then clone this repository using terminal

`` git clone https://github.com/msabu007/codeLogoDetection.git ``

3. activate the created environment

if conda;
`` conda activate <env_name> ``
for windows 
`` path\to\myenv\Scripts\activate ``

4. open a terminal in the cloned folder, then install the required packages

Note: the python version used for the development is 3.9.12

`` pip install -r requirements.txt ``

5. run the app

`` python main.py ``

6. if the all went correctly you can see a web address to open, something like http:/127.0.0.1:8000

7. now that the app is running, please open a browser window and enter the below address

`` http://127.0.0.1:8000/docs ``

8. the click on the post tab
9. click on try out
10. upload the test image
11. click on execute
12. after success full run, a window with labelled image will pop up and a cropped image will be stored in the output folder of the project directory