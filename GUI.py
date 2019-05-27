from tkinter import *
from tkinter import filedialog
import pandas as pd
import handler

class TopFrame(Frame):

    def OpenFile(self):
        file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file',filetypes = [('CSV Files','*.csv')])
        if file:
            data = pd.read_csv(file)
            file.close()
            self.FileLabel['text'] = file.name
            axis.AxisSelection(data,True)

    def BrowseWidgets(self):
        self.BrowseLabel = Label(self,
                                text = 'Choose your CSV file: ',
                                anchor = E)
        self.Browse = Button(self,
                            text = "Browse ...",
                            command = self.OpenFile,
                            anchor = W)
        self.FileLabel = Label(self,
                            text = '  ')

        # self.BrowseLabel.grid(row = 0, column = 0, columnspan = 2)
        # self.Browse.grid(row = 0, column = 2)
        # self.FileLabel.grid(row = 1, column = 0,columnspan = 3)
        self.BrowseLabel.pack()
        self.Browse.pack()
        self.FileLabel.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.BrowseWidgets()

class AxisFrame(Frame):

    def AxisSelection(self,data=NONE,Active=False):
        self.Xlabel = Label(self,
                            text = 'Select X axis:',
                            anchor = 'w')
        self.Xmenu = OptionMenu(self,' ',' ')
        self.Ylabel = Label(self,
                            text = 'Select Y axis:',
                            anchor = 'w')
        self.Ymenu = OptionMenu(self,' ',' ')

        self.Xmenu.configure(state = 'disabled')
        self.Ymenu.configure(state = 'disabled')
        self.Xlabel.grid(row = 0, column = 0, columnspan = 2)
        self.Xmenu.grid(row = 1, column = 0, columnspan = 2)
        self.Ylabel.grid(row = 0, column = 2, columnspan = 2)
        self.Ymenu.grid(row = 1, column = 2, columnspan = 2)
        if Active:
            choices = list()
            for value in data.columns:
                choices.append(value)
            Xvalue = StringVar(self)
            Xvalue.set(choices[0])
            self.Xmenu = OptionMenu(self,Xvalue,*choices)
            Yvalue = StringVar(self)
            Yvalue.set(choices[1])
            self.Ymenu = OptionMenu(self,Yvalue,*choices)
            self.Xmenu.configure(state = 'active')
            self.Ymenu.configure(state = 'active')
            self.Xlabel.grid(row = 0, column = 0, columnspan = 2)
            self.Xmenu.grid(row = 1, column = 0, columnspan = 2)
            self.Ylabel.grid(row = 0, column = 2, columnspan = 2)
            self.Ymenu.grid(row = 1, column = 2, columnspan = 2)
            print(choices)
            print(data)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.AxisSelection()

class GenerateFrame(Frame):

    def GenerateWidget(self):
        self.Generate = Button(self,
                                text = 'Generate HTML')

        # self.Generate.grid(row = 0, column = 2, columnspan = 2)
        self.Generate.pack(side = LEFT)

    def QuitWidget(self):
        self.QUIT = Button(self,
                            text = 'Quit',
                            fg = 'red',
                            command = self.quit)

        # self.QUIT.grid(row = 0, column = 0, columnspan = 2)
        self.QUIT.pack(side = LEFT)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.QuitWidget()
        self.GenerateWidget()

class StatusFrame(Frame):

    def StatusBar(self):
        self.status = Label(self,
                        text = 'Help information .. ',
                        bd = 1,
                        relief = SUNKEN,
                        anchor = W)
        self.status.pack(side = LEFT, fill = X)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(side = LEFT)
        self.StatusBar()

root = Tk()

root.title('Data Presenter')
root.geometry("400x200")
root.resizable(0, 0)

top = TopFrame(master=root)
axis = AxisFrame(master=root)
generate = GenerateFrame(master=root)
status = StatusFrame(master=root)

root.mainloop()
root.destroy()
