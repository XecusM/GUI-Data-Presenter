from tkinter import *
from tkinter import filedialog
import pandas as pd
import handler

class TopFrame(Frame):

    def AxisSelectiong(self,data):
        pass

    def OpenFile(self):
        file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file',filetypes = [('CSV Files','*.csv')])
        if file:
            data = pd.read_csv(file)
            file.close()
            self.FileLabel['text'] = file.name
            print(data)

    def BrowseWidgets(self):
        self.BrowseLabel = Label(self,
                                text = 'Choose your CSV file: ')
        self.Browse = Button(self,
                            text = "Browse ...",
                            command = self.OpenFile)
        self.FileLabel = Label(self)

        # self.BrowseLabel.grid(row = 0, column = 0, columnspan = 2)
        # self.Browse.grid(row = 0, column = 2)
        # self.FileLabel.grid(row = 1, column = 0,columnspan = 3)
        self.BrowseLabel.pack(side = LEFT)
        self.Browse.pack(side = LEFT)
        self.FileLabel.pack()

    def GenerateWidget(self):
        self.Generate = Button(self,
                                text = 'Generate HTML')

        # self.Generate.grid(row = 2, column = 0, columnspan = 2)
        self.Generate.pack()

    def QuitWidget(self):
        self.QUIT = Button(self,
                            text = 'Quit',
                            fg = 'red',
                            command = self.quit)

        # self.QUIT.grid(row = 2, column = 2, columnspan = 2)
        self.QUIT.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.BrowseWidgets()
        self.GenerateWidget()
        self.QuitWidget()

class StatusFrame(Frame):

    def StatusBar(self):
        self.status = Label(self,
                        text = 'Help information .. ',
                        bd = 1,
                        relief = SUNKEN,
                        anchor = NW)
        self.status.pack(side = LEFT, fill = X)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(side = BOTTOM)
        self.StatusBar()

root = Tk()
top = TopFrame(master=root)
status = StatusFrame(master=root)
root.mainloop()
root.destroy()
