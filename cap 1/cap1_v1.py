import dash
import dash_html_components as html


# instanciando o app
app = dash.Dash(__name__)

# adicionando o layout
app.layout = html.Div([ #criando div para montar o dashboard, com a lib dash_html_components
    html.H1('Hello, World') #conteudo do H1
])

if __name__ =='__main__': # Rodando o app;
    app.run_server(debug=True)