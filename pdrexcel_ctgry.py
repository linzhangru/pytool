import pandas as pd
from pandas import DataFrame,Series
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

df = pd.read_excel("output.xlsx", sheet_name='category')
#print df["OOM_ADJ.Native"]

app = dash.Dash()
app.layout = html.Div([
    html.Label("OOM_ADJ_CheckBoxes"),
    dcc.Checklist(
        id="category_Checklist",
        options = [
            {'label':"category.Native"          ,'value':"Native"      },
            {'label':"category.Dalvik"          ,'value':"Dalvik"      },
            {'label':"category.dex_mmap"        ,'value':"dex_mmap"    },
            {'label':"category.so_mmap"         ,'value':"so_mmap"     },
            {'label':"category.unknown"         ,'value':"unknown"     },
            {'label':"category.oat_mmap"        ,'value':"oat_mmap"    },
            {'label':"category.art_mmap"        ,'value':"art_mmap"    },
            {'label':"category.dalvik_other"    ,'value':"dalvik_other"},
            {'label':"category.apk_mmap"        ,'value':"apk_mmap"    },
            {'label':"category.egl_mtrack"      ,'value':"egl_mtrack"  },
            {'label':"category.gl_mtrack"       ,'value':"gl_mtrack"   },
            {'label':"category.stack"           ,'value':"stack"       },
            {'label':"category.gfx_dev"         ,'value':"gfx_dev"     },
            {'label':"category.other_mmap"      ,'value':"other_mmap"  },
            {'label':"category.jar_mmap"        ,'value':"jar_mmap"    },
            {'label':"category.cursor"          ,'value':"cursor"      },
            {'label':"category.other_mtrack"    ,'value':"other_mtrack"},
        ],
        values=["native",]),         #the default True items for the checkboxes
    dcc.Graph(id="category"),    
],style={'columnCount': 1})

@app.callback(Output("category",'figure'),
              [Input("category_Checklist",'values')])
def update_figure(selected_items):
    print selected_items
    print len(selected_items)

    traces = []
    for i in selected_items:
        if cmp(str(i),"Native") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.Native"]),1), 
                                     y = df["category.Native"].values,
                                     mode='lines+markers',
                                     name='Native'))
            print type(df["category.Native"])

        if cmp(str(i),"Dalvik") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.Dalvik"]),1), 
                                     y = df["category.Dalvik"].values,
                                     mode='lines+markers',
                                     name='Dalvik'))
            print type(df["category.Dalvik"])

        if cmp(str(i),"dex_mmap") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.dex_mmap"]),1), 
                                     y = df["category.dex_mmap"].values,
                                     mode='lines+markers',
                                     name='dex_mmap'))
            print type(df["category.dex_mmap"])

        if cmp(str(i),"so_mmap") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.so_mmap"]),1), 
                                     y = df["category.so_mmap"].values,
                                     mode='lines+markers',
                                     name='so_mmap'))
            print type(df["category.so_mmap"])
            
        if cmp(str(i),"unknown") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.unknown"]),1), 
                                     y = df["category.unknown"].values,
                                     mode='lines+markers',
                                     name='unknown'))
            print type(df["category.unknown"])

        if cmp(str(i),"oat_mmap") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.oat_mmap"]),1), 
                                     y = df["category.oat_mmap"].values,
                                     mode='lines+markers',
                                     name='oat_mmap'))
            print type(df["category.oat_mmap"])

        if cmp(str(i),"art_mmap") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.art_mmap"]),1), 
                                     y = df["category.art_mmap"].values,
                                     mode='lines+markers',
                                     name='art_mmap'))
            print type(df["category.art_mmap"])

        if cmp(str(i),"dalvik_other") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.dalvik_other"]),1), 
                                     y = df["category.dalvik_other"].values,
                                     mode='lines+markers',
                                     name='dalvik_other'))
            print type(df["category.dalvik_other"])

        if cmp(str(i),"apk_mmap") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.apk_mmap"]),1), 
                                     y = df["category.apk_mmap"].values,
                                     mode='lines+markers',
                                     name='category.apk_mmap'))
            print type(df["category.apk_mmap"])

        if cmp(str(i),"egl_mtrack") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.egl_mtrack"]),1), 
                                     y = df["category.egl_mtrack"].values,
                                     mode='lines+markers',
                                     name='egl_mtrack'))
            print type(df["category.egl_mtrack"])

        if cmp(str(i),"gl_mtrack") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.gl_mtrack"]),1), 
                                     y = df["category.gl_mtrack"].values,
                                     mode='lines+markers',
                                     name='gl_mtrack'))
            print type(df["category.gl_mtrack"])

        if cmp(str(i),"stack") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.stack"]),1), 
                                     y = df["category.stack"].values,
                                     mode='lines+markers',
                                     name='stack'))
            print type(df["category.stack"])


        if cmp(str(i),"gfx_dev") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.gfx_dev"]),1), 
                                     y = df["category.gfx_dev"].values,
                                     mode='lines+markers',
                                     name='gfx_dev'))
            print type(df["category.gfx_dev"])

        if cmp(str(i),"other_mmap") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.other_mmap"]),1), 
                                     y = df["category.other_mmap"].values,
                                     mode='lines+markers',
                                     name='other_mmap'))
            print type(df["category.other_mmap"])

        if cmp(str(i),"jar_mmap") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.jar_mmap"]),1), 
                                     y = df["category.jar_mmap"].values,
                                     mode='lines+markers',
                                     name='jar_mmap'))
            print type(df["category.jar_mmap"])

        if cmp(str(i),"cursor") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.cursor"]),1), 
                                     y = df["category.cursor"].values,
                                     mode='lines+markers',
                                     name='cursor'))
            print type(df["category.cursor"])

        if cmp(str(i),"other_mtrack") == 0:
            traces.append(go.Scatter(x = np.arange(0,len(df["category.other_mtrack"]),1), 
                                     y = df["category.other_mtrack"].values,
                                     mode='lines+markers',
                                     name='other_mtrack'))
            print type(df["category.other_mtrack"])

            
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
