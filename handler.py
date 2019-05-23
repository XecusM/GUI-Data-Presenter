import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

def GraphSetting(ImportedData,GraphOptions):
    '''
    This function creates html file for the selected type of graph
    available types:
        - scatter
        - line
        - bar
        - histogram
    '''
    # intiate graph data list
    data = list()
    # create html scatter graph
    if GraphOptions['type'] == 'scatter':
        # create data for the desired graph
        for x in GraphOptions['x']:
            # create trace for graph data
            trace = go.Scatter(
                x = ImportedData[x],
                y = ImportedData[GraphOptions['y']],
                mode = 'markers',
                name=x)
            # add trace to graph data
            data.append(trace)
        # setting layout for the desired graph
        layout = go.Layout(
            title = GraphOptions['title'],
            xaxis = dict(title = GraphOptions['Xtitle']),
            yaxis = dict(title = GraphOptions['Ytitle']),
            hovermode ='closest')
        # create the figure for graph ploting
        fig = go.Figure(data=data, layout=layout)
        pyo.plot(fig, filename='results.html')
    # create html line graph
    elif GraphOptions['type'] == 'line':
        # create data for the desired graph
        for x in GraphOptions['x']:
            # create trace for graph data
            trace = go.Scatter(
                x = ImportedData[x],
                y = ImportedData[GraphOptions['y']],
                mode = 'lines',
                name = x)
            # add trace to graph data
            data.append(trace)
        # setting layout for the desired graph
        layout = go.Layout(
            title = GraphOptions['title'],
            xaxis = dict(title = GraphOptions['Xtitle']),
            yaxis = dict(title = GraphOptions['Ytitle']),
            hovermode ='closest')
        # create the figure for graph ploting
        fig = go.Figure(data=data, layout=layout)
        # export the html file
        pyo.plot(fig, filename='results.html')
    # create html bar chart
    elif GraphOptions['type'] == 'bar':
        # create data for the desired graph
        for x in GraphOptions['x']:
            # create trace for graph data
            trace = go.Bar(
                x = ImportedData[x],
                y = ImportedData[GraphOptions['y']],
                name=x)
            # add trace to graph data
            data.append(trace)
        # setting layout for the desired graph
        layout = go.Layout(
            title = GraphOptions['title'],
            xaxis = dict(title = GraphOptions['Xtitle']),
            yaxis = dict(title = GraphOptions['Ytitle']),
            hovermode ='closest')
        # create the figure for graph ploting
        fig = go.Figure(data=data, layout=layout)
        # export the html file
        pyo.plot(fig, filename='results.html')
    # create histogram chart
    elif GraphOptions['type'] == 'histogram':
        # create data for the desired graph
        for x in GraphOptions['x']:
            # create trace for graph data
            trace = go.Histogram(
                x = ImportedData[x],
                name=x)
            # add trace to graph data
            data.append(trace)
        # setting layout for the desired graph
        layout = go.Layout(
            title = GraphOptions['title'],
            xaxis = dict(title = GraphOptions['Xtitle']),
            hovermode ='closest')
        # create the figure for graph ploting
        fig = go.Figure(data=data, layout=layout)
        # export the html file
        pyo.plot(fig, filename='results.html')
    else:
        # an error message if type not recognized
        message = 'Graph type not recognized'
        print(message)
        return message
    # successful message
    message = 'Graph has been extracted successfully'
    print(message)
    return message
def main():
    '''
    Function for testing handler script with test_data.csv data
    '''
    # import data from csv file
    ImportedData = pd.read_csv('test_data.csv')
    # apply settings for graph options
    GraphOptions = {'type':'scatter',
                    'x':['X','D'],
                    'y':'Y',
                    'title':'test graph',
                    'Xtitle':'X axis',
                    'Ytitle':'Y axis'}
    # call function to export the html file
    GraphSetting(ImportedData,GraphOptions)

if __name__ == '__main__':
    main()
