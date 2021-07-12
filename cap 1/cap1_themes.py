import dash_bootstrap_components as dbc
import dash
import dash_html_components as html

# instanciando o app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
"""
app.layout = html.Div([ #criando div para montar o dashboard, com a lib dash_html_components
    html.H1('Poverty and Equity Database',
            style={
                'color':'blue',
                'font-size':'40px',
                }),#conteudo do H1
    html.H2('The World Bank'), #conteudo H2
    dbc.Tabs([
        dbc.Tabs([
            
            html.Ul([
                html.Br(),#conteudo da lista
                html.Li('Number of Economies: 170'), #primeiro conteudo da lista
                html.Li('Temporal Covarege : 1974- 2019'),#segundo conteudo da lista
                html.Li('Update Frequency: Quarterly'),
                html.Li('Last Updated: March 18, 2020'),
                html.Li(
                            [
                                'Source: ',
                                html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
                            ]
                )
             ])
        ], label = 'Key Facts'),
        
        dbc.Tabs([
            html.Ul([
                html.Br(),
                html.Li('Book title: Interactive Dashboards and Data Apps with Plotly and Dash'),
                html.Li(['GitHub repo: ',
                         html.A('https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash',href='https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash')
                        ])
            ])
        ], label= 'Project Info')
        
    ]),
    
])
"""

app.layout = html.Div([
    html.H1('Poverty And Equity Database',
            style={'color': 'blue',
                   'fontSize': '40px'}),
    html.H2('The World Bank'),
    dbc.Tabs([
       dbc.Tab([
           html.Ul([
               html.Br(),
               html.Li('Number of Economies: 170'),
               html.Li('Temporal Coverage: 1974 - 2019'),
               html.Li('Update Frequency: Quarterly'),
               html.Li('Last Updated: March 18, 2020'),
               html.Li([
                   'Source: ',
                   html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',
                          href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
               ])
           ])

       ], label='Key Facts'),
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li('Book title: Interactive Dashboards and Data Apps with Plotly and Dash'),
                html.Li(['GitHub repo: ',
                         html.A('https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash',
                                href='https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash')
                         ])
            ])
        ], label='Project Info')
    ]),
])
if __name__ =='__main__': # Rodando o app;
    app.run_server(debug=True)