import visualization
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.figure import Figure
import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import sqlite3
import pandas as pd
import samm
from wordcloud import WordCloud, STOPWORDS

class bargraph:

    f1 = Figure(figsize=(2, 2), dpi=100)
    bar = f1.add_subplot(111)

    y_pos = np.arange(len(visualization.objects))
    graph= bar.bar(y_pos, visualization.observation, align='center', alpha=0.5)
    graph[0].set_color('r')
    graph[1].set_color('g')
    # graph[2].set_color('b')
    plt.xticks(y_pos, visualization.objects)
    plt.ylabel('No of Tweet')
    plt.title('Polarity of Tweets')
    # plt.legend((graph[0],graph[1]), ('Negative', 'Positive'))
class pychart:
    f2 = Figure(figsize=(2,2), dpi=100)
    py = f2.add_subplot(111)

    observation = visualization.observation
    labels = ['dislike', 'like']
    py.pie(observation, labels=labels, autopct='%.2f')
    plt.title('Narendra modi popularity')


class wordcloud:
    data = samm.dataForWordcloud()
    df = pd.DataFrame(data)
    df.columns = ('terms', 'frec')
    print(df.head())
    word_string = ' '
    for index, row in df.iterrows():
        word_string += (row['terms'] + ' ') * row['frec']

    wordcloud = WordCloud(font_path='Aaargh.ttf',
                          stopwords=STOPWORDS,
                          background_color='black',
                          width=1200,
                          height=1000
                          ).generate(word_string)

    fig = plt.figure(figsize=(2, 2))
    a = fig.add_subplot(111)
    a.imshow(wordcloud)
    a.axis('off')

class scatter:
    app = dash.Dash(__name__)
    app.layout = html.Div(
        [   html.H2('Live Twitter Sentiment'),
            dcc.Graph(id='live-graph', animate=True),
            dcc.Interval(
                id='graph-update',
                interval=1*1000
            ),
        ]
    )

    @app.callback(Output('live-graph', 'figure'),
                  events=[Event('graph-update', 'interval')])
    def update_graph_scatter(self):
        try:
            conn = sqlite3.connect('twitter.db')
            c = conn.cursor()
            df = pd.read_sql("SELECT * FROM sentiment WHERE tweet LIKE '%black%' ORDER BY unix DESC LIMIT 1000", conn)
            df.sort_values('unix', inplace=True)
            df['sentiment_smoothed'] = df['sentiment'].rolling(int(len(df)/5)).mean()
            df.dropna(inplace=True)

            X = df.unix.values[-100:]
            Y = df.sentiment_smoothed.values[-100:]

            data = plotly.graph_objs.Scatter(
                    x=X,
                    y=Y,
                    name='Scatter',
                    mode= 'lines+markers'
                    )

            return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                        yaxis=dict(range=[min(Y),max(Y)]),)}

        except Exception as e:
            with open('errors.txt','a') as f:
                f.write(str(e))
                f.write('\n')



