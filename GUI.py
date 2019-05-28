from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import handler
import os

class TopFrame(Frame):

    def OpenFile(self):
        file = filedialog.askopenfile(parent=root,
                                        mode='rb',
                                        title='Choose a file',
                                        filetypes = [('CSV Files','*.csv')])
        if file:
            filename = os.path.split(file.name)[-1]
            data = pd.read_csv(file)
            file.close()
            self.FileLabel['text'] = filename
            axis.AxisSelection(data,True)
            generate.Generate.config(state = 'normal')
            self.FileLabel.bind('<Enter>',self.FileEnter)
            self.FileLabel.bind('<Leave>',self.OnLeave)
            generate.Generate.pack(side = LEFT)

    def BrowseWidgets(self):
        self.BrowseLabel = Label(self,
                                text = 'Choose your CSV file: ',
                                width = 18)
        self.Browse = Button(self,
                            text = "Browse ...",
                            command = self.OpenFile,
                            width = 10)
        self.FileLabel = Label(self,
                            text = '  ',
                            anchor = NE,
                            width = 18)

        self.BrowseLabel.pack(side = LEFT)
        self.Browse.pack(side = LEFT, padx = 10, pady = 10)
        self.FileLabel.pack(side = LEFT, padx = 10, pady = 10)

        self.Browse.bind('<Enter>', self.BrowseEnter)
        self.Browse.bind('<Leave>', self.OnLeave)

    def BrowseEnter(self, event):
        status.status['text'] = 'Browse for csv file'

    def FileEnter(self, event):
        status.status['text'] = 'Imported File Name'

    def OnLeave(self, event):
        status.status['text'] = ' '

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.BrowseWidgets()

class AxisFrame(Frame):

    def GraphSelection(self):
        self.Glabel = Label(self,
                            text = 'Select Graph Type:',
                            anchor = NW)
        self.Gvalue = StringVar(self)
        self.Gvalue.set('Scatter')
        self.Gmenu = OptionMenu(self,
                                self.Gvalue ,
                                'Scatter' ,
                                'Line' ,
                                'Bar',
                                'Histogram')
        self.Gmenu.bind('<Enter>',self.GmenuEnter)
        self.Gmenu.bind('<Leave>',self.OnLeave)

        self.Gmenu.configure(width = 10)
        self.Glabel.grid(row = 1, column = 0, columnspan = 2,
                        padx = 10, pady = 10)
        self.Gmenu.grid(row = 2, column = 0, columnspan = 2,
                        padx = 10)

    def AxisSelection(self,data=NONE,Active=False):
        self.Tlabel = Label(self,
                            text = 'Enter Title Name:',
                            anchor = NE)
        self.Tentry = Entry(self, width = 30)
        self.Xlabel = Label(self,
                            text = 'Select X axis:',
                            anchor = NW)
        self.Xmenu = OptionMenu(self,' ',' ')
        self.Ylabel = Label(self,
                            text = 'Select Y axis:',
                            anchor = NW)
        self.Ymenu = OptionMenu(self,' ',' ')

        self.Xmenu.bind('<Enter>',self.XmenuEnter)
        self.Xmenu.bind('<Leave>',self.OnLeave)
        self.Ymenu.bind('<Enter>',self.YmenuEnter)
        self.Ymenu.bind('<Leave>',self.OnLeave)
        self.Tentry.bind('<Enter>',self.TentryEnter)
        self.Tentry.bind('<Leave>',self.OnLeave)

        self.Xmenu.configure(width = 10)
        self.Ymenu.configure(width = 10)
        self.Xmenu.configure(state = 'disabled')
        self.Ymenu.configure(state = 'disabled')

        self.Tlabel.grid(row = 0, column = 0, columnspan = 2,
                        padx = 10)
        self.Tentry.grid(row = 0, column = 2, columnspan = 4)
        self.Xlabel.grid(row = 1, column = 2, columnspan = 2,
                        pady = 10)
        self.Xmenu.grid(row = 2, column = 2, columnspan = 2)
        self.Ylabel.grid(row = 1, column = 4, columnspan = 2,
                        padx = 10, pady = 10)
        self.Ymenu.grid(row = 2, column = 4, columnspan = 2,
                        padx = 10)
        if Active:
            choices = list()
            for value in data.columns:
                choices.append(value)
            self.Xvalue = StringVar(self)
            self.Xvalue.set(choices[0])
            self.Xmenu = OptionMenu(self, self.Xvalue, *choices)
            self.Yvalue = StringVar(self)
            self.Yvalue.set(choices[1])
            self.Ymenu = OptionMenu(self, self.Yvalue, *choices)
            self.Xmenu.configure(width = 10)
            self.Ymenu.configure(width = 10)
            self.Xmenu.configure(state = 'active')
            self.Ymenu.configure(state = 'active')
            self.Xmenu.bind('<Enter>',self.XmenuEnter)
            self.Xmenu.bind('<Leave>',self.OnLeave)
            self.Ymenu.bind('<Enter>',self.YmenuEnter)
            self.Ymenu.bind('<Leave>',self.OnLeave)
            self.Xlabel.grid(row = 1, column = 2, columnspan = 2,
                            pady = 10)
            self.Xmenu.grid(row = 2, column = 2, columnspan = 2)
            self.Ylabel.grid(row = 1, column = 4, columnspan = 2,
                            padx = 10, pady = 10)
            self.Ymenu.grid(row = 2, column = 4, columnspan = 2,
                            padx = 10)
            self.data = data

    def XmenuEnter(self, event):
        status.status['text'] = 'Select data for X axis'

    def YmenuEnter(self, event):
        status.status['text'] = 'Select data for Y axis'

    def GmenuEnter(self, event):
        status.status['text'] = 'Select graph type'

    def TentryEnter(self, event):
        status.status['text'] = 'Enter the title name you want to assign'

    def OnLeave(self, event):
        status.status['text'] = ' '

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.AxisSelection()
        self.GraphSelection()

class GenerateFrame(Frame):

    def GenerateWidget(self):
        self.Generate = Button(self,
                                text = 'Generate HTML',
                                fg = 'green',
                                command = self.CreateGraph,
                                width = 15)
        self.Generate.config(state = 'disabled')

        self.Generate.bind('<Enter>',self.GenerateEnter)
        self.Generate.bind('<Leave>',self.OnLeave)

        self.Generate.pack(side = LEFT, padx = 10, pady = 10)

    def QuitWidget(self):
        self.QUIT = Button(self,
                            text = 'Quit',
                            fg = 'red',
                            command = self.quit,
                            width = 15)

        self.QUIT.bind('<Enter>',self.QUITEnter)
        self.QUIT.bind('<Leave>',self.OnLeave)

        self.QUIT.pack(side = LEFT, padx = 10, pady = 10)

    def CreateGraph(self):
        if axis.Tentry.get():
            self.Generate.config(state = 'disabled')
            self.Generate.pack(side = LEFT, padx = 10, pady = 10)
            filename = filedialog.asksaveasfilename(
                                        initialfile= 'results.html',
                                        defaultextension=".html",
                                        filetypes=[('HTML files', '.html')],
                                        title="Choose location")
            Tvalue = axis.Tentry.get()
            Gvalue = axis.Gvalue.get()
            Xvalue = axis.Xvalue.get()
            Yvalue = axis.Yvalue.get()
            GraphOptions = {'type':Gvalue,
                            'x':['X','D'],
                            'y':'Y',
                            'title':Tvalue,
                            'Xtitle':Xvalue,
                            'Ytitle':Yvalue,
                            'file':filename}
            # call function to export the html file
            handler.GraphSetting(axis.data,GraphOptions)
            self.Generate.config(state = 'normal')
            self.Generate.pack(side = LEFT)
        else:
            messagebox.showinfo("Attention","Please enter the graph title!")

    def GenerateEnter(self, event):
        status.status['text'] = 'Click to generate the results graph'

    def QUITEnter(self, event):
        status.status['text'] = 'End the program'

    def OnLeave(self, event):
        status.status['text'] = ' '

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
                        anchor = NW,
                        width = 400)
        self.status.pack(side = LEFT)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(side = LEFT)
        self.StatusBar()

root = Tk()

root.title('Data Presenter')
root.geometry("400x210")
root.resizable(0, 0)

top = TopFrame(master=root)
axis = AxisFrame(master=root)
generate = GenerateFrame(master=root)
status = StatusFrame(master=root)

root.mainloop()
root.destroy()
