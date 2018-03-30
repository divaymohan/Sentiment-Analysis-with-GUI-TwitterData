import matplotlib
import samm as s
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from matplotlib import style

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
style.use("ggplot")
import new as n
from tkinter import *
import dataCollection
from Graphs import scatter
from Graphs import bargraph
from Graphs import pychart
from Graphs import wordcloud
import algorithm

class StartPage(tk.Frame):
    file_name = " "
    def load_file(self):
        self.file_name = filedialog.askopenfilename(filetypes=([('All files', '*.*'),
                                                                ('Text files', '*.txt'),
                                                                ('CSV files', '*.csv')]))
        print(type(self.file_name))
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=("""This prediction may be wrong.if you want to contineu press 'agree' else 'disagree'."""), font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Agree",
                             command=lambda: controller.show_frame(Hybrid))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree",
                             command=quit)
        button2.pack()
        button3 = ttk.Button(self, text="upload file",
                             command=self.load_file)
        button3.pack()
        label1 = tk.Label(self, text= " ".join(self.file_name), font=LARGE_FONT)
        label1.pack(pady=10, padx=10)




class Hybrid(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hybrid Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button2 = ttk.Button(self,text = "execute model",
                             command = lambda: n.popupmessage(algorithm.Accuracy(algorithm.voted_classifier)))
        button2.pack()
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

class NaiveBayesGUI(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NaiveBayesGUI Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button2 = ttk.Button(self, text="execute model",
                             command=lambda: n.popupmessage(algorithm.Accuracy(algorithm.NaiveBayes)))
        button2.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class MultinomialNaivebayes(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MultinomialNaivebayes Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button2 = ttk.Button(self, text="execute model",
                             command=lambda: n.popupmessage(algorithm.Accuracy(algorithm.MNB_classifier)))
        button2.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
class BinomialNaivebayes(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BinomialNaivebayes Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button2 = ttk.Button(self, text="execute model",
                             command=lambda: n.popupmessage(algorithm.Accuracy(algorithm.Bnaivebayes)))
        button2.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
class LogisticRegeration(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="LogisticRegression Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button2 = ttk.Button(self, text="execute model",
                             command=lambda: n.popupmessage(algorithm.Accuracy(algorithm.LogisticR_classifier)))
        button2.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class NuSVC(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NuSVC Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button2 = ttk.Button(self, text="execute model",
                             command=lambda: n.popupmessage(algorithm.Accuracy(algorithm.Linear_SVC)))
        button2.pack()

        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class BOW(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BOW Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(n.f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
class CollectionData(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Data Collection page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label1 = tk.Label(self,text="Enter consumer_key")
        label1.pack(pady=5,padx=5)

        form1 = tk.Entry(self)
        form1.pack()

        label2 = tk.Label(self, text="Enter consumer_secret")
        label2.pack(pady=5, padx=5)

        form2 = tk.Entry(self)
        form2.pack()

        label3 = tk.Label(self, text="Enter access_key")
        label3.pack(pady=5, padx=5)

        form3 = tk.Entry(self)
        form3.pack()

        label4 = tk.Label(self, text="Enter access_secret")
        label4.pack(pady=5, padx=5)

        form4 = tk.Entry(self)
        form4.pack()

        label5 = tk.Label(self, text="Enter key Words")
        label5.pack(pady=5, padx=5)

        form5 = tk.Entry(self)
        form5.pack()

        button = ttk.Button(self,text="start_collection",command=lambda :dataCollection.CollectionData(form1.get(),form2.get(),form3.get(),form4.get(),form5.get()))
        button.pack()
        button = ttk.Button(self, text="Stop_collection",
                            command=lambda: dataCollection.stopCollection())
        button.pack()

class savesettings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Settings", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


          # initializing the choice, i.e. Python

        languages = [
            "Naive bayes",
            "MultinomialNaiveBayes",
            "Hybrid",
            "NuSVC",
            "regression"
        ]
        variable = StringVar()
        variable.set(languages[0])  # default value

        def ShowChoice():
            return variable.get()

        strings = variable.get()
        tk.Label(self,
                 text="""Choose Algorithm""",
                 justify=tk.LEFT,
                 padx=20).pack()
        ttk.OptionMenu(self,variable,*languages).pack()




        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

class Wordcloud(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Popularity Chart", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(wordcloud.fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

class BarGraph(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bar Graph", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(bargraph.f1, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

class Pychart(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="pychart Graph", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(pychart.f2, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class Live(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Live graph", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        canvas = FigureCanvasTkAgg(pychart.f2, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        button1 = ttk.Button(self, text="Back to Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
