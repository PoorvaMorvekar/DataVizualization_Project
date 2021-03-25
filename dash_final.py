
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


data1 = pd.read_csv('Country wise adaptatoin.csv',sep=',')
data2 = pd.read_csv('Alt-fuel-stations.csv',sep=',')
data3 = pd.read_csv('Electric_Vehicle_Population_Data.csv')
data4 = pd.read_csv('Electric_Vehicle_Population_Size_History.csv',sep=',')
data5 = pd.read_csv('global-electric-car-sales.csv')
data6 = pd.read_csv('Producers_market_share.csv')
data7 = pd.read_csv('2019-2040.csv',sep=',')



img1 = px.pie(data1,values="Public Chargers",names="Country",title='Measures taken by countries to adapt to change in EV market')
img2 = px.line_3d(data2,x=" Year ",y=" Electric ",z="Total alt fuels except electric",title='Comparison of Alternate Fuels')
img3 = px.choropleth(data3,locations='State',color='Electric Vehicle Type', locationmode="USA-states", scope="usa",title='US map showing major category of EV adopted in each state')
img4 = px.line(data4,x='Date',y='Electric Vehicle (EV) Total',title='Change in EV adaptation by public over the period of time')
img5 = px.bar(data5, x='Countries', y='Total sales in million',
             color='Total sales in million',
             labels={'pop':'Sales in millions'}, height=400,title='Electric Vehicles sales chart')
img6 = px.bar(data7,x='Year',y=['Sales(in million)','EV share(%)'],title='Prediction of rise in EV over the next 20 years.')
img7 = px.histogram(data6,x='Market share(%)',y='Producer',title='Market share of automobile companies in EV sector')
img8 = px.density_heatmap(data3,x='Model Year',y='Make',title='Journey of companies is developing Electric automobiles')

app.layout = html.Div([
    html.H1('Electric Vehicle adaptation and future market.'),
    html.H3('Project done by: M.CRASTA Nikhil Gavin and MME MORVEKAR Poorva Vivek'),
    html.Div([
        html.P('EV sales started to pick up in 2009 and have rapidly been increasing ever since. Especially 2015 was a big year for electric vehicles, with a 78% increase in the amount of electric vehicles on the roads compared to 2014 (International Energy Agency, 2016). But what growth will we expect in the near future? And will each country meet their sustainability goals they committed to? A few countries have already expressed interest in slashing emissions and banning the internal combustion engine. China, USA, Norway, Germany, The Netherlands and even India aim to ban the internal combustion engine in 10 to 15 years time ( ThinkProgress , 2016). The world is now moving in the right direction.'),
        html.H4('INTRODUCTION'),
        html.H5('The following visualizations show the adaptation and the future market of Electric vehicles.'),
    dcc.Graph(
        figure = img2),
    html.Div([
        html.P('We know that the innovation and development in the field of Alternate fuels has been going on since the 90\'s, many alternating fuels have been adapted such as CNG,LPG etc and alternate methods are still being tried and tested. Recent innovation and development in the field of EV has seen a sudden spike in the adaptation of Alternating fuel by the people.'),
        html.P('Thus making EV\'s the breakthrough technology has been seeking for. The Plot above shows the change in adaptation of EV\'s when compared to other alternating fuels over the years.')]),
        html.P('We see the journey of EV\'s in the state From 0 in 1992 to 78,301 in 2019. '),
    dcc.Graph(
        figure = img1),
    html.Div([
        html.P('China is leading the market in adaptation of the Electric Vehicles. As you can see the chart above china has installed 3,01,238 publicly available chargers that is 51% of the total market.')]),
        html.P('China is followed by the United Stats of America with 11% of the total market share. And then followed by Netherlands with 8.45%'),
        ]),
    dcc.Graph(
        figure = img3),
    html.Div([
        html.P('In this map we can see the major category of EV\'s being adapted in different states. We see that several states have been adapting to the change in trend.'),
        html.P('We can expect to see growth in each state over the coming period of time.')]),
    dcc.Graph(
        figure = img4),
    html.Div([
        html.P('In this map we can see the adaptation of EV\'s by the public in the state over a period of time from Jan 2017 to September 2020. We see a steady increase in the graph which shows us that the public is readily accepting the change. We can expect to see a steady increase over the coming years as more and more people will be moving towards the adaptation of EV\'s.'),
        ]),
    dcc.Graph(
        figure = img5),
    html.Div([
        html.P('Here we see the list countries which are playing a major role in the adoption of EV\'s. We can see that again china is the market leader in this category as well. ')]),
    dcc.Graph(
        figure = img7),
    html.Div([
        html.P('Several companies have been conducting research in the field of EV\'s and some of which are successful have been accepted by the public. Tesla Inc holds the major stake in the global market as the manufacturer of plug-in Ev\'s with 17.95% of the total market share. This is then followed by the VW group with 12.6% of the total market share.'),
        html.P('In the coming future we can see many new car makers in picture with sevral innovative ideas and products being offered to the public and thus keeping the trend going.' )]),
    dcc.Graph(
        figure = img8),
    html.Div([
        html.P('By observing the heat map we can see that over a period of time several companies have launched several models of EV\'s into the public market. Several models  ranging from low-range EV to sports EV have been launched. Once again we can observe that the sales of Tesla EV\'s are high in the market over the period of time. As Tesla Inc. is seen dominating the market as of today, It will be interesting to see who will be the major player in this sector in the coming future. '),
        ]),
    dcc.Graph(
        figure = img6),
    html.Div([
        html.P('We now see the future of EV market, by the factors of companies and the public adapting to the change in trend. It is expected to have a market share of 58% in the year 2040 according to several survey\'s conducted on the same.The future is bright for the industry and the people are also ready to adapt to it.'),
        html.H5('We can thus conclude that EV\'s are going to play a major role in the coming future and the future looks bright. We hope to see a lot of innovation and research in this field and thus moving the world to a better future.')       
        ])])

if __name__ == '__main__':
    app.run_server(debug = False)

                      