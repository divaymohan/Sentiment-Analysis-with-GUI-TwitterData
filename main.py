import tkinter as tk
from tkinter import ttk
import frames
from Graphs import scatter,bargraph

strings = ''
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "SentAna App")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command=lambda:self.show_frame(frames.savesettings) )
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        filemenu.add_command(label="collect data",command=lambda :self.show_frame(frames.CollectionData))
        menubar.add_cascade(label="File", menu=filemenu)

        exchangeChoice = tk.Menu(menubar, tearoff=1)
        exchangeChoice.add_command(label="Naive-Bayes",
                                   command=lambda: self.show_frame(frames.NaiveBayesGUI))
        exchangeChoice.add_command(label="MultinomialNaivebayes",
                                   command=lambda: self.show_frame(frames.MultinomialNaivebayes))
        exchangeChoice.add_command(label="BinomialNaivebayes",
                                   command=lambda: self.show_frame(frames.BinomialNaivebayes))
        exchangeChoice.add_command(label="LogisticRegression",
                                   command=lambda: self.show_frame(frames.LogisticRegeration))
        exchangeChoice.add_command(label="NuSVC",
                                   command=lambda: self.show_frame(frames.NuSVC))

        exchangeChoice.add_command(label="Bag-Of-Word",
                                   command=lambda: self.show_frame(frames.BOW))
        exchangeChoice.add_command(label="Hybrid",
                                   command=lambda: self.show_frame(frames.Hybrid))
        menubar.add_cascade(label="SentAna", menu=exchangeChoice)

        # dataTF = tk.Menu(menubar, tearoff=1)
        # dataTF.add_command(label="Tick",
        #                    command=lambda: frames.n.popupmessage('tick'))
        # dataTF.add_command(label="1 day",
        #                    command=lambda: frames.n.popupmessage('1d'))
        # dataTF.add_command(label="3 day",
        #                    command=lambda: frames.n.popupmessage('3d'))
        # dataTF.add_command(label="1 Week",
        #                    command=lambda: frames.n.popupmessage('7d'))
        # menubar.add_cascade(label="Data Time Frame", menu=dataTF)

        # TIME_INTR = tk.Menu(menubar, tearoff=1)
        #
        # TIME_INTR.add_command(label="Tick",
        #                   command=lambda: frames.n.popupmessage('tick'))
        # TIME_INTR.add_command(label="1 minute",
        #                   command=lambda: frames.n.popupmessage('1Min'))
        # TIME_INTR.add_command(label="5 minute",
        #                   command=lambda: frames.n.popupmessage('5Min'))
        # TIME_INTR.add_command(label="15 minute",
        #                   command=lambda: frames.n.popupmessage('15Min'))
        # TIME_INTR.add_command(label="30 minute",
        #                   command=lambda: frames.n.popupmessage('30Min'))
        # TIME_INTR.add_command(label="1 Hour",
        #                   command=lambda: frames.n.popupmessage('1H'))
        # TIME_INTR.add_command(label="3 Hour",
        #                   command=lambda: frames.n.popupmessage('3H'))
        # menubar.add_cascade(label="Time Interval", menu=TIME_INTR)

        # topIndi = tk.Menu(menubar, tearoff=1)
        # topIndi.add_command(label="None",
        #                     command=lambda: frames.n.popupmessage('none'))
        # topIndi.add_separator()
        # topIndi.add_command(label="MODI",
        #                     command=lambda: frames.n.popupmessage('MODI'))
        # topIndi.add_command(label="RAHUL",
        #                     command=lambda: frames.n.popupmessage('RAHUL'))
        # topIndi.add_command(label="Kejriwal",
        #                     command=lambda: frames.n.popupmessage('Kejriwal'))

        # menubar.add_cascade(label="Top Indicator", menu=topIndi)

        mainI = tk.Menu(menubar, tearoff=1)
        mainI.add_command(label="None",
                          command=lambda: frames.n.popupmessage('none'))
        mainI.add_separator()
        mainI.add_command(label="BAR",
                          command=lambda: self.show_frame(frames.BarGraph))
#         mainI.add_command(label="Scatter Plot",
#                           command=scatter.app.run_server(debug=True)
# )
        mainI.add_command(label="Popularity Chart",
                          command=lambda: self.show_frame(frames.Wordcloud))
        mainI.add_command(label="Popularity In Percentage",
                      command=lambda: self.show_frame(frames.Pychart))
        menubar.add_cascade(label="Graph Indicator", menu=mainI)


        startStop = tk.Menu(menubar, tearoff=1)
        startStop.add_command(label="Resume",
                              command=lambda: frames.n.popupmessage('start'))
        startStop.add_command(label="Pause",
                              command=lambda: frames.n.popupmessage('stop'))
        menubar.add_cascade(label="Resume/Pause Client", menu=startStop)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tutorial", command=lambda :frames.n.popupmessage("tutorial"))
        menubar.add_cascade(label="Help", menu=helpmenu)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}
        for F in (frames.NaiveBayesGUI,frames.LogisticRegeration,frames.BOW,frames.NuSVC,frames.BinomialNaivebayes,frames.MultinomialNaivebayes,frames.StartPage,frames.savesettings,frames.CollectionData,frames.Hybrid,frames.Wordcloud,frames.BarGraph,frames.Pychart):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(frames.StartPage)

        tk.Tk.iconbitmap(self, default='photo/logo.ico')

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



app = SeaofBTCapp()
app.geometry("800x650")
# ani = animation.FuncAnimation(n.f, animate, interval=1000)
app.mainloop()
