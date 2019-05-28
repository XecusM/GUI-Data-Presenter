from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import handler
import os

class BrowseFrame(Frame):
    '''
    Class for file browse details
    i.e. bowse button and imported file label
    '''
    def OpenFile(self):
        '''
        Method for file open pop-up window to import csv file data
        '''
        # assign window to variable
        file = filedialog.askopenfile(parent=root,
                                        mode='rb',
                                        title='Choose a file',
                                        filetypes = [('CSV Files','*.csv')])
        # Check if user choose a file or not
        if file:
            # get the file name without its path
            filename = os.path.split(file.name)[-1]
            # import data from csv file
            data = pd.read_csv(file)
            # close connection of the opened file
            file.close()
            # view the file name
            self.FileLabel['text'] = filename
            # send data to graph frame
            graph.AxisSelection(data,True)
            # enable Generate button
            generate.Generate.config(state = 'normal')
            # send information to status bar
            self.FileLabel.bind('<Enter>',self.FileEnter)
            self.FileLabel.bind('<Leave>',self.OnLeave)
            # view changes of Generate button
            generate.Generate.pack(side = LEFT)

    def BrowseWidgets(self):
        '''
        Method for browse button frame details
        '''
        # identify label for browse button
        self.BrowseLabel = Label(self,
                                text = 'Choose your CSV file: ',
                                width = 18)
        # identify browse button
        self.Browse = Button(self,
                            text = "Browse ...",
                            command = self.OpenFile,
                            width = 10)
        # identify label for imported file name
        self.FileLabel = Label(self,
                            text = '  ',
                            anchor = NE,
                            width = 18)
        # link browse button mouse hover to status bar
        self.Browse.bind('<Enter>', self.BrowseEnter)
        self.Browse.bind('<Leave>', self.OnLeave)
        # view browse frame details
        self.BrowseLabel.pack(side = LEFT)
        self.Browse.pack(side = LEFT, padx = 10, pady = 10)
        self.FileLabel.pack(side = LEFT, padx = 10, pady = 10)

    def BrowseEnter(self, event):
        '''
        Method for browse button entering mouse hover
        '''
        status.status['text'] = 'Browse for csv file'

    def FileEnter(self, event):
        '''
        Method for imported file label entering mouse hover
        '''
        status.status['text'] = 'Imported File Name'

    def OnLeave(self, event):
        '''
        Method for browse details leaving mouse hover
        '''
        status.status['text'] = ' '

    def __init__(self, master=None):
        '''
        Method for initial details of the browse frame
        '''
        # link browse frame to root
        Frame.__init__(self, master)
        # view browse frame
        self.pack()
        # view browse frame details
        self.BrowseWidgets()

class GraphFrame(Frame):
    '''
    Class for graph options selection
    i.e. X axis, Y axis and graph type
    '''
    def GraphSelection(self):
        '''
        Method for graph type selection
        '''
        # identify label for graph type options
        self.Glabel = Label(self,
                            text = 'Select Graph Type:',
                            anchor = NW)
        # set the default value for graph type options
        self.Gvalue = StringVar(self)
        self.Gvalue.set('Scatter')
        # identify graph type options
        self.Gmenu = OptionMenu(self,
                                self.Gvalue ,
                                'Scatter' ,
                                'Line' ,
                                'Bar',
                                'Histogram')
        # link graph options mouse hover to status bar
        self.Gmenu.bind('<Enter>',self.GmenuEnter)
        self.Gmenu.bind('<Leave>',self.OnLeave)
        # view graph details
        self.Gmenu.configure(width = 10)
        self.Glabel.grid(row = 1, column = 0, columnspan = 2,
                        padx = 10, pady = 10)
        self.Gmenu.grid(row = 2, column = 0, columnspan = 2,
                        padx = 10)

    def AxisSelection(self,data=NONE,Active=False):
        '''
        Method for axis selection details
        '''
        # identify label for graph title
        self.Tlabel = Label(self,
                            text = 'Enter Title Name:',
                            anchor = NE)
        # identify entry for graph title
        self.Tentry = Entry(self, width = 30)
        # identify label for x axis options
        self.Xlabel = Label(self,
                            text = 'Select X axis:',
                            anchor = NW)
        # identify x axis options
        self.Xmenu = OptionMenu(self,' ',' ')
        # identify label for y axis options
        self.Ylabel = Label(self,
                            text = 'Select Y axis:',
                            anchor = NW)
        # identify y axis options
        self.Ymenu = OptionMenu(self,' ',' ')
        # link axis options mouse hover to status bar
        self.Xmenu.bind('<Enter>',self.XmenuEnter)
        self.Xmenu.bind('<Leave>',self.OnLeave)
        self.Ymenu.bind('<Enter>',self.YmenuEnter)
        self.Ymenu.bind('<Leave>',self.OnLeave)
        self.Tentry.bind('<Enter>',self.TentryEnter)
        self.Tentry.bind('<Leave>',self.OnLeave)
        # configure axis details
        self.Xmenu.configure(width = 10)
        self.Ymenu.configure(width = 10)
        self.Xmenu.configure(state = 'disabled')
        self.Ymenu.configure(state = 'disabled')
        # view axis details
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
        # check if data imported or not
        if Active:
            # initate a list of choices
            choices = list()
            # get columns names to the list
            for value in data.columns:
                choices.append(value)
            # set the default value for x axis options
            self.Xvalue = StringVar(self)
            self.Xvalue.set(choices[0])
            # identify x axis options
            self.Xmenu = OptionMenu(self, self.Xvalue, *choices)
            # set the default value for y axis options
            self.Yvalue = StringVar(self)
            self.Yvalue.set(choices[1])
            # identify y axis options
            self.Ymenu = OptionMenu(self, self.Yvalue, *choices)
            # configure axis details
            self.Xmenu.configure(width = 10)
            self.Ymenu.configure(width = 10)
            self.Xmenu.configure(state = 'active')
            self.Ymenu.configure(state = 'active')
            # link axis options mouse hover to status bar
            self.Xmenu.bind('<Enter>',self.XmenuEnter)
            self.Xmenu.bind('<Leave>',self.OnLeave)
            self.Ymenu.bind('<Enter>',self.YmenuEnter)
            self.Ymenu.bind('<Leave>',self.OnLeave)
            # view axis details
            self.Xlabel.grid(row = 1, column = 2, columnspan = 2,
                            pady = 10)
            self.Xmenu.grid(row = 2, column = 2, columnspan = 2)
            self.Ylabel.grid(row = 1, column = 4, columnspan = 2,
                            padx = 10, pady = 10)
            self.Ymenu.grid(row = 2, column = 4, columnspan = 2,
                            padx = 10)
            # create a self variable for the imported data
            self.data = data

    def XmenuEnter(self, event):
        '''
        Method for x axis options entering mouse hover
        '''
        status.status['text'] = 'Select data for X axis'

    def YmenuEnter(self, event):
        '''
        Method for y axis options entering mouse hover
        '''
        status.status['text'] = 'Select data for Y axis'

    def GmenuEnter(self, event):
        '''
        Method for graph options entering mouse hover
        '''
        status.status['text'] = 'Select graph type'

    def TentryEnter(self, event):
        '''
        Method for title entry entering mouse hover
        '''
        status.status['text'] = 'Enter the title name you want to assign'

    def OnLeave(self, event):
        '''
        Method for graph details leaving mouse hover
        '''
        status.status['text'] = ' '

    def __init__(self, master=None):
        '''
        Method for initial details of the graph frame
        '''
        # link graph frame to root
        Frame.__init__(self, master)
        # view graph frame
        self.pack()
        # view graph frame details
        self.AxisSelection()
        self.GraphSelection()

class GenerateFrame(Frame):
    '''
    Class for generate html file details
    '''
    def GenerateWidget(self):
        '''
        Method for generate button frame details
        '''
        # identify generate button
        self.Generate = Button(self,
                                text = 'Generate HTML',
                                fg = 'green',
                                command = self.CreateGraph,
                                width = 15)
        # configure generate button
        self.Generate.config(state = 'disabled')
        # link generate button mouse hover to status bar
        self.Generate.bind('<Enter>',self.GenerateEnter)
        self.Generate.bind('<Leave>',self.OnLeave)
        # view generate button
        self.Generate.pack(side = LEFT, padx = 10, pady = 10)

    def QuitWidget(self):
        '''
        Method for generate button frame details
        '''
        # identify quit button
        self.QUIT = Button(self,
                            text = 'Quit',
                            fg = 'red',
                            command = self.quit,
                            width = 15)
        # link quit button mouse hover to status bar
        self.QUIT.bind('<Enter>',self.QUITEnter)
        self.QUIT.bind('<Leave>',self.OnLeave)
        # view quit button
        self.QUIT.pack(side = LEFT, padx = 10, pady = 10)

    def CreateGraph(self):
        '''
        Method for creating results graph
        '''
        # check if graph title exists
        if graph.Tentry.get():
            # disable generate button during generating
            self.Generate.config(state = 'disabled')
            # review generate button
            self.Generate.pack(side = LEFT, padx = 10, pady = 10)
            # get the results file name
            filename = filedialog.asksaveasfilename(
                                        initialfile= 'results.html',
                                        defaultextension=".html",
                                        filetypes=[('HTML files', '.html')],
                                        title="Choose location")
            # get the graph title
            Tvalue = graph.Tentry.get()
            # get the graph type
            Gvalue = graph.Gvalue.get()
            # get x axis selected data
            Xvalue = graph.Xvalue.get()
            # get y axis selected data
            Yvalue = graph.Yvalue.get()
            # create options for handler script to create results file
            GraphOptions = {'type':Gvalue,
                            'x':[Xvalue],
                            'y':Yvalue,
                            'title':Tvalue,
                            'Xtitle':Xvalue,
                            'Ytitle':Yvalue,
                            'file':filename}
            # call function to export the html file
            handler.GraphSetting(graph.data,GraphOptions)
            # notify that the data exported
            status.status['text'] = 'Graph has been exported successfully'
            # enable generate button
            self.Generate.config(state = 'normal')
            # review generate button
            self.Generate.pack(side = LEFT)
        else:
            # give a message to enter the graph title
            messagebox.showinfo("Attention","Please enter the graph title!")

    def GenerateEnter(self, event):
        '''
        Method for generate button entering mouse hover
        '''
        status.status['text'] = 'Click to generate the results graph'

    def QUITEnter(self, event):
        '''
        Method for quit button entering mouse hover
        '''
        status.status['text'] = 'End the program'

    def OnLeave(self, event):
        '''
        Method for generate details leaving mouse hover
        '''
        status.status['text'] = ' '

    def __init__(self, master=None):
        '''
        Method for initial details of the generate frame
        '''
        # link generate frame to root
        Frame.__init__(self, master)
        # view generate frame
        self.pack()
        # view generate frame details
        self.QuitWidget()
        self.GenerateWidget()

class StatusFrame(Frame):
    '''
    Class for status bar details
    '''
    def StatusBar(self):
        '''
        Method for status bar details
        '''
        # identify label for status bar
        self.status = Label(self,
                        text = 'Help information .. ',
                        bd = 1,
                        relief = SUNKEN,
                        anchor = NW,
                        width = 400)
        # view status bar
        self.status.pack(side = LEFT)

    def __init__(self, master=None):
        '''
        Method for initial details of the status frame
        '''
        # link status frame to root
        Frame.__init__(self, master)
        # view status frame
        self.pack(side = LEFT)
        # view status frame details
        self.StatusBar()

# create vriable for tkinter application
root = Tk()

# set the application title
root.title('Data Presenter')
# set application size
root.geometry("400x210")
# disable application resizing
root.resizable(0, 0)

# get browse frame details
browse = BrowseFrame(master=root)
# get graph frame details
graph = GraphFrame(master=root)
# get generate fram details
generate = GenerateFrame(master=root)
# get status fram details
status = StatusFrame(master=root)

# view application
root.mainloop()
# remove application window after quit
root.destroy()
