import matplotlib
#from new import animate
import nltk
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet
from tkinter import ttk

from tkinter import filedialog

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import constants
from nltk.classify import ClassifierI
from statistics import mode
import random
from nltk.corpus import movie_reviews
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

import pandas as pd

import numpy as np
from matplotlib import pyplot

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
style.use("ggplot")


f = Figure(figsize=(2, 2), dpi=100)
a = f.add_subplot(111)
df = pd.DataFrame()

def animate(i):
    pullData = open("sampleData.txt", "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()

    a.plot(xList, yList)

def popupmessage(msg):
    popup=tk.Tk()
    popup.wm_title("Accuracy")
    label = ttk.Label(popup,text = "Accuracy: ",font =NORM_FONT)
    label.pack(side = "left",fill ="x",pady=10)
    label = ttk.Label(popup,text=msg,font=NORM_FONT)
    label.pack(side="right",fill="x",pady=5)
    B1=ttk.Button(popup,text="Okay",command=popup.destroy)
    B1.pack(side="bottom")
    popup.mainloop()

def popupmessage1(msg,ss):
    popup=tk.Tk()
    popup.wm_title("Accuracy")
    label = ttk.Label(popup,text = "Accuracy: ",font =NORM_FONT)
    label.pack(side = "left",fill ="x",pady=10)
    label = ttk.Label(popup,text=msg,font=NORM_FONT)
    label.pack(side="right",fill="x",pady=5)
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="right", fill="x", pady=5)
    B1=ttk.Button(popup,text="Okay",command=popup.destroy)
    B1.pack(side="bottom")
    popup.mainloop()