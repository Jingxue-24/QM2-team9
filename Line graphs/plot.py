import pandas as pd
import plotly.express as px

df1 = pd.read_csv('Data/median.csv')
fig1 = px.line(df1, x = 'Year', y = ['Median length', 'Median Danceability', 'Median Energy', 'Median Instrumentalness', 'Median Acousticness', 'Median Liveness', 'Median Loudness', 'Median Speechiness', 'Median Tempo', 'Median Time signature'], title = 'Median')
fig1.write_html('Output/Median.html')

df2 = pd.read_csv('Data/std.csv')
fig2 = px.line(df2, x = 'Year', y = ['Std of length', 'Std of Danceability', 'Std of Energy', 'Std of Instrumentalness', 'Std of Acousticness', 'Std of Liveness', 'Std of Loudness', 'Std of Speechiness', 'Std of Tempo', 'Std of Time signature'], title = 'Standard Deviation')
fig2.write_html('Output/Std.html')

df3 = pd.read_csv('Data/var.csv')
fig3 = px.line(df3, x = 'Year', y = ['Var of length', 'Var of Danceability', 'Var of Energy', 'Var of Instrumentalness', 'Var of Acousticness', 'Var of Liveness', 'Var of Loudness', 'Var of Speechiness', 'Var of Tempo', 'Var of Time signature'], title = 'Variance')
fig3.write_html('Output/Var.html')
