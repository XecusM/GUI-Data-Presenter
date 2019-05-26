from tkinter import *
from tkinter import filedialog
import pandas as pd
import handler

class Application(Frame):

    def AxisSelectiong(self,data):
        pass

    def OpenFile(self):
        file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file',filetypes = [('CSV Files','*.csv')])
        if file:
            data = pd.read_csv(file)
            file.close()
            self.FileLabel['text'] = file.name
            print(data)

    def StatusBar(self):
        pass

    def BrowseWidgets(self):
        self.BrowseLabel = Label(self,
                                text = 'Choose your CSV file: ')
        self.Browse = Button(self,
                            text = "Browse ...",
                            command = self.OpenFile)
        self.FileLabel = Label(self)

        self.BrowseLabel.grid(row = 0, column = 0, columnspan = 2)
        self.Browse.grid(row = 0, column = 2)
        self.FileLabel.grid(row = 1, column = 0,columnspan = 3)

    def GenerateWidget(self):
        self.Generate = Button(self,
                                text = 'Generate HTML')

        self.Generate.grid(row = 2, column = 0, columnspan = 2)

    def QuitWidget(self):
        self.QUIT = Button(self,
                            text = 'Quit',
                            fg = 'red',
                            command = self.quit)

        self.QUIT.grid(row = 2, column = 2, columnspan = 2)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.BrowseWidgets()
        self.GenerateWidget()
        self.QuitWidget()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
