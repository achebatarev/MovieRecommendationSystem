# COVID-19-Flask-app
This app utilizes a deep convolutional neural network to detect COVID-19 in chest X-ray images. The model was pretrained from chest radiography images that are open source and available to the general public, and was built by the [COVID-Net Open Source Initiative](https://github.com/lindawangg/COVID-Net). 

This Flask app allows a user to upload an image of a chest X-ray and recieve a prediction of the probability that image is normal, contains Pneumonia, or contains COVID-19. To make these predictions, we integrated the `inference.py` program from COVID-NET as a class file located in our `tensor.py` file. We have provided some test images locatd in the images folder. This is just a simple Flask app project and is by no means at all perfect. **Please do not use COVID-Net for self-diagnosis and seek help from your local health authorities.**

## Install Requirements
- Open your terminal in this folder and run the following command:
`pip install -r requirements.txt`

## Getting Started with COVID-19 model
- Download all the files from the [COVIDNet-CXR-Large](https://drive.google.com/drive/folders/1eNidqMyz3isLjGYN1evzQu--A-JVkzbk) pretrained model.
- You may end up with multiple zipped folders after downloading evertything.
- Unizip the folders and delete the original zipfiles.
- Make sure to move the files into the models folder.
- Your models folder should look like this:
```
      ├── models
      │   └── COVIDNet-CXR-Large
      │       ├── checkpoint
      │       ├── model-8485.data-00000-of-00001
      │       ├── model-8485.index
      │       ├── model.meta
      │       └── savedModel
      │           ├── saved_model.pb
      │           └── variables
      │               ├── variables.data-00000-of-00001
      │               └── variables.index
```

## Running the App
- Open your terminal in this folder and run the following command:
`python app.py`
