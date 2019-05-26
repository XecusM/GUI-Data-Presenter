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
            print(data)
            self.FileLabel['text'] = file.name

    def StatusBar(self):
        pass

    def BrowseWidgets(self):
        self.BrowseLabel = Label(self,
                                text = 'Choose your CSV file: ' )
        self.Browse = Button(self,
                            text = "Browse ...",
                            command = self.OpenFile)

        self.BrowseLabel.pack(side = LEFT)
        self.Browse.pack(side = LEFT)

        self.FileLabel = Label(self)
        self.FileLabel.pack()

    def QuitWidget(self):
        self.QUIT = Button(self,
                            text = 'Quit',
                            fg = 'red',
                            command = self.quit)

        self.QUIT.pack(side = BOTTOM)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.BrowseWidgets()
        self.QuitWidget()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
