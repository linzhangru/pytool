import pandas as pd
from pandas import DataFrame,Series
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

df = pd.read_excel("output.xlsx",sheet_name='OOM_ADJ_Persist')#
#print df["OOM_ADJ.Native"]
#print df["OOM_ADJ.Persist.com.android.phone"]


app = dash.Dash()
app.layout = html.Div([
    html.Label("OOM_ADJ_CheckBoxes"),
    dcc.Checklist(
        id="OOM_ADJ_Checklist",
        options = [
            {'label':"OOM_ADJ.Persist.com.android.phone"              ,'value':"phone"           },
            {'label':"OOM_ADJ.Persist.com.android.systemui"           ,'value':"systemui"        },
            {'label':"OOM_ADJ.Persist.com.mediatek.ims"               ,'value':"ims"             },
            {'label':"OOM_ADJ.Persist.com.transsion.keyguardgesture"  ,'value':"keyguardgesture" },
            {'label':"OOM_ADJ.Persist.com.transsion.statisticalsales" ,'value':"statisticalsales"},
        ],
        values=["systemui"]),         #the default True items for the checkboxes
    dcc.Graph(id="OOM_ADJ_Persist"),    
],style={'columnCount': 1})

@app.callback(Output("OOM_ADJ_Persist",'figure'),
              [Input("OOM_ADJ_Checklist",'values')])
def update_figure(selected_items):
    print selected_items
    print len(selected_items)

    traces = []
    for i in selected_items:
        if cmp(str(i),"phone") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["OOM_ADJ.Persist.com.android.phone"]),1), 
                                     y = df["OOM_ADJ.Persist.com.android.phone"].values,
                                     mode='lines+markers',
                                     name='Phone'))
            print type(df["OOM_ADJ.Persist.com.android.phone"])

        if cmp(str(i),"systemui") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["OOM_ADJ.Persist.com.android.systemui"]),1), 
                                     y = df["OOM_ADJ.Persist.com.android.systemui"].values,
                                     mode='lines+markers',
                                     name='Systemui'))
            print type(df["OOM_ADJ.Persist.com.android.systemui"])

        if cmp(str(i),"ims") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["OOM_ADJ.Persist.com.mediatek.ims"]),1), 
                                     y = df["OOM_ADJ.Persist.com.mediatek.ims"].values,
                                     mode='lines+markers',
                                     name='IMS'))
            print type(df["OOM_ADJ.Persist.com.mediatek.ims"])

        if cmp(str(i),"keyguardgesture") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["OOM_ADJ.Persist.com.transsion.keyguardgesture"]),1), 
                                     y = df["OOM_ADJ.Persist.com.transsion.keyguardgesture"].values,
                                     mode='lines+markers',
                                     name='KeyguardGesture'))
            print type(df["OOM_ADJ.Persist.com.transsion.keyguardgesture"])
            
        if cmp(str(i),"statisticalsales") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["OOM_ADJ.Persist.com.transsion.statisticalsales"]),1), 
                                     y = df["OOM_ADJ.Persist.com.transsion.statisticalsales"].values,
                                     mode='lines+markers',
                                     name='Statisticalsales'))
            print type(df["OOM_ADJ.Persist.com.transsion.statisticalsales"])
            
    ret = {
        'data' : traces,
        'layout' : go.Layout(
            xaxis={'type':'line','title':'indexs'},
            yaxis={'title':'MemoryConsumed', 'range':[-10,400]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest')
    }
    return ret
                          

if __name__ == '__main__':
        app.run_server(debug=True)

