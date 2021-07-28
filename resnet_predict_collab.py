# -*- coding: utf-8 -*-
"""resnet_predict_collab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZPTBQQPOss_qZv9ddHEM41xg7_4wW_bB
"""

import numpy as np
import pandas as pd
import torch
import keras
import os, gc, pathlib
from sklearn.metrics import confusion_matrix
from fastai import *
from fastai.vision.all import *
from fastai.tabular.all import *
from fastai.text.all import *
#from fastai.medical.imaging import *
from fastai.vision.data import ImageDataLoaders
from fastai.vision.models import *
import torchvision.models as models
from fastai.callback.schedule import lr_find
from fastai.callback.schedule import *
from matplotlib import pyplot as plt
from fastai.imports import *
from fastai.torch_core import *
from fastai.learner import *

learner=load_learner("/content/drive/MyDrive/Colab Notebooks/pretrained_model/resnet/final_resnet/btc_final2.pkl")

def is_true(x):
    if x[0]=='yes':
        return "Tumor detected."
    else:
        return "Tumor not detected."

img=PILImage.create(f"/content/drive/MyDrive/Colab Notebooks/BrainTumor/brain_tumor_dataset/yes/Y109.JPG")

x=learner.predict(img)

print("Test Result:",is_true(x),"\nProbability:",x[2])