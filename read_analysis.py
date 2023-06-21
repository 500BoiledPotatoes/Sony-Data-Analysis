import os
import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
import cufflinks as cf
cf.go_offline(connected=True)
init_notebook_mode(connected=True)
path = 'files'
path_read_encoder = []
path_read_decoder = []

def read(file_path):
    temp_list = os.listdir(file_path)
    for temp_list_each in temp_list:
        if os.path.isfile(file_path + '/' + temp_list_each):
            temp_path = file_path + '/' + temp_list_each
            if os.path.splitext(temp_path)[-1] == '.csv':
                if temp_path.split('/')[1][0] == 'd':
                    path_read_decoder.append(temp_path)
                elif temp_path.split('/')[1][0] == 'e':
                    path_read_encoder.append(temp_path)
            else:
                continue
        else:
            read(file_path + '/' + temp_list_each)


read(path)

def decoder_analysis():
    for file in path_read_decoder:
        df = pd.read_csv(file)

        df[['DateTime', 'RTT', 'RecvBufs']].iplot(
        y='RTT',
        x='DateTime',
        mode = 'lines',
        secondary_y = 'RecvBufs',
        opacity=0.8,
        symbol = 1,
        xTitle = 'Date',
        yTitle = 'RTT',
        secondary_y_title = 'RecvBufs',
        title = file.split('/')[1]

    )
decoder_analysis()


def encoder_analysis():
    for file in path_read_encoder:
        df = pd.read_csv(file)
        df[['DateTime', 'RTT', 'SendBufs']].iplot(
            y='RTT',
            x='DateTime',
            mode='lines',
            secondary_y='SendBufs',
            opacity=0.8,
            symbol=1,
            xTitle='Date',
            yTitle='RTT',
            secondary_y_title='SendBufs',
            title=file.split('/')[1]
        )
encoder_analysis()
# print(df.to_string())

