import pandas as pd
from pandas import DataFrame,Series
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

df = pd.read_excel("output.xlsx", sheet_name='All')
#print df["OOM_ADJ.Native"]

app = dash.Dash()
app.layout = html.Div([
    html.Label("OOM_ADJ_CheckBoxes"),
    dcc.Checklist(
        id="OOM_ADJ_Checklist",
        options = [
            {'label':"FreeRam"                ,'value':"FreeRam"               },
            {'label':"FreeRam.Cached_pss"     ,'value':"FreeRam_Cached_pss"    },
            {'label':"FreeRam.Cached_kernel"  ,'value':"FreeRam_Cached_kernel" },
            {'label':"FreeRam.free"           ,'value':"FreeRam_free"          },
            {'label':"UsedRam"                ,'value':"UsedRam"               },
            {'label':"UsedRam.usedpss"        ,'value':"usedpss"               },
            {'label':"UsedRam.kernel"         ,'value':"usedkernel"            },
            {'label':"LostRam"                ,'value':"LostRam"               },
            {'label':"ZRAM.physical_used"     ,'value':"ZRAM_physical_used"    },
            {'label':"ZRAM.in_swap"           ,'value':"ZRAM_in_swap"          },
            {'label':"ZRAM.total_swap"        ,'value':"ZRAM_total_swap"       },
        ],
        values=["FreeRam","UsedRam","LostRam","ZRAM.physical_used",]),         #the default True items for the checkboxes
    dcc.Graph(id="OOM_ADJ"),    
],style={'columnCount': 1})

@app.callback(Output("OOM_ADJ",'figure'),
              [Input("OOM_ADJ_Checklist",'values')])
def update_figure(selected_items):
    print selected_items
    print len(selected_items)

    traces = []
    for i in selected_items:
        print i
        if cmp(str(i),"FreeRam") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["FreeRam"]),1), 
                                     y = df["FreeRam"].values,
                                     mode='lines+markers',
                                     name='FreeRam'))
            print type(df["FreeRam"])

        if cmp(str(i),"FreeRam_Cached_pss") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["FreeRam.Cached_pss"]),1), 
                                     y = df["FreeRam.Cached_pss"].values,
                                     mode='lines+markers',
                                     name='FreeRam_Cached_pss'))
            print type(df["FreeRam.Cached_pss"])

        if cmp(str(i),"FreeRam_Cached_kernel") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["FreeRam.Cached_kernel"]),1), 
                                     y = df["FreeRam.Cached_kernel"].values,
                                     mode='lines+markers',
                                     name='FreeRam_Cached_kernel'))
            print type(df["FreeRam.Cached_kernel"])

        if cmp(str(i),"FreeRam_free") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["FreeRam.free"]),1), 
                                     y = df["FreeRam.free"].values,
                                     mode='lines+markers',
                                     name='FreeRam_free'))
            print type(df["FreeRam.free"])
            
        if cmp(str(i),"UsedRam") == 0:
            print "adding UsedRam data"
            print df["UsedRam"]
            traces.append(go.Scatter(x = np.arange(0,len(df["UsedRam"]),1), 
                                     y = df["UsedRam"].values,
                                     mode='lines+markers',
                                     name='UsedRam'))
            print type(df["UsedRam"])

        if cmp(str(i),"usedpss") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["UsedRam.usedpss"]),1), 
                                     y = df["UsedRam.usedpss"].values,
                                     mode='lines+markers',
                                     name='usedpss'))
            print type(df["UsedRam.usedpss"])

        if cmp(str(i),"usedkernel") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["UsedRam.kernel"]),1), 
                                     y = df["UsedRam.kernel"].values,
                                     mode='lines+markers',
                                     name='usedkernel'))
            print type(df["UsedRam.kernel"])

        if cmp(str(i),"LostRam") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["LostRam"]),1), 
                                     y = df["LostRam"].values,
                                     mode='lines+markers',
                                     name='LostRam'))
            print type(df["LostRam"])

        if cmp(str(i),"ZRAM_physical_used") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["ZRAM.physical_used"]),1), 
                                     y = df["ZRAM.physical_used"].values,
                                     mode='lines+markers',
                                     name='ZRAM_physical_used'))
            print type(df["ZRAM.physical_used"])

        if cmp(str(i),"ZRAM_in_swap") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["ZRAM.in_swap"]),1), 
                                     y = df["ZRAM.in_swap"].values,
                                     mode='lines+markers',
                                     name='ZRAM_in_swap'))
            print type(df["ZRAM.in_swap"])

        if cmp(str(i),"ZRAM_total_swap") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["ZRAM.total_swap"]),1), 
                                     y = df["ZRAM.total_swap"].values,
                                     mode='lines+markers',
                                     name='ZRAM_total_swap'))
            print type(df["ZRAM.total_swap"])
            
    ret = {
        'data' : traces,
        'layout' : go.Layout(
            xaxis={'type':'line','title':'indexs'},
            yaxis={'title':'MemoryConsumed', 'range':[-300,1000]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest')
    }
    return ret
                          

if __name__ == '__main__':
        app.run_server(debug=True)
