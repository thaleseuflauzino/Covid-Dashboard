from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
dataset = pd.read_csv('database.csv', sep=",")
tabela = dataset.values.tolist()

casosnovos = []
region = []
newdeaths = []
tablepie = []
piedataset = []

for row in tabela:
    if not row[2] == '':
        casosnovos = row[3]
        region = row[0]
        tablepie.append([region, casosnovos])

for row in tablepie:
    piedataset.append({"Region": row[0], "Casos Novos": row[1]})

tablepie1 = []
MortesNovas = []
regiao = []
piedataset1 = []

i = 0
num_elements_list = len(tabela)
while i < num_elements_list:
    row = tabela[i]
    regiao = row[0]
    MortesNovas = row[5]
    if not row[2] == '':
        tablepie1.append([regiao, MortesNovas])
    i += 1

i = 0
tamanho = len(tablepie1)

while i < tamanho:
    piedataset1.append(
        {"Regiao": tablepie1[i][0], "Obitos Novos": tablepie1[i][1]})
    i += 1

regiao = []
Estado = []
Data = []
CasosNovos = []
ObitosNovos = []
TabelaNova = []
dfdataset = []

for row in tabela:
    regiao = row[0]
    Estado = row[1]
    Data = row[2]
    CasosNovos = row[3]
    ObitosNovos = row[5]
    if not row[2] == '':
        # if Estado == 'São Paulo' or Estado == 'Rio de Janeiro' or Estado == 'Espírito Santo' or Estado == 'Minas Gerais':
        TabelaNova.append([regiao, Data, Estado, CasosNovos, ObitosNovos])

for i in TabelaNova:
    dfdataset.append({"regiao": i[0], "Data": i[1], "Estado": i[2],
                     "Casos Novos": i[3], "Obitos Novos": i[4]})

Estado = []
Data1 = []
CasosAcumulados = []
ObitosAcumulados = []
tablewhile = []
whiledataset = []

i = 0
tamanholista = len(tabela)
while i < tamanholista:
    row = tabela[i]
    Estado = row[1]
    Data1 = row[2]
    CasosAcumulados = row[4]
    ObitosAcumulados = row[6]

    if not row[2] == '':
        # if Estado == 'São Paulo' or Estado == 'Rio de Janeiro' or Estado == 'Espírito Santo' or Estado == 'Minas Gerais':
        if row[4] >= 1:
            tablewhile.append(
                [Data1, Estado, CasosAcumulados, ObitosAcumulados])
    i += 1

i = 0
tamanho = len(tablewhile)
while i < tamanho:
    whiledataset.append({"Data1": tablewhile[i][0], "Estado": tablewhile[i][1],
                        "Casos Acumulados": tablewhile[i][2], "Obitos Acumulados": tablewhile[i][3]})
    i += 1

opcoes = ('Obitos Acumulados por Região', 'Casos Acumulados por Região', 'Casos Novos por Estado',
          'Casos Acumulados por Estado', 'Obitos Novos por Estado', 'Obitos Acumulados por Estado')

opcoes1 = ('Sudeste', 'Sul', 'Centro-Oeste', 'Norte', 'Nordeste')

app.layout = html.Div(children=[
    html.H1(children='Coronavírus (COVID-19) no Brasil.'),
    html.H2(children='''
        Gráficos sobre COVID-19 no Brasil entre Janeiro e Abril.
    '''),
    html.H3(children='''
        Escolha o Gráfico referente ao dado desejado.
    '''),
    html.Div([
        dcc.Dropdown(opcoes, value='NYC', id='Grafico-1', style={
                     'width': '50%', 'display': 'inline-block'}),
        dcc.Graph(
            id='graph1'
        ),
        html.Div([
            html.H2(children='Casos Acumulados de COVID19 no Brasil por Região'),
            html.H3(children='Escolha qual região deseja ver os dados'),
            dcc.Dropdown(opcoes1, value='NYC', id='Grafico-2', style={
                'width': '50%', 'display': 'inline-block'}),
            dcc.Graph(
                id='graph2'
            ),
            html.Div([
                html.H2(
                    children='Óbitos Acumulados de COVID19 no Brasil por Região'),
                html.H3(children='Escolha qual região deseja ver os dados'),
                dcc.Dropdown(opcoes1, value='NYC', id='Grafico-3', style={
                    'width': '50%', 'display': 'inline-block'}),
                dcc.Graph(
                    id='graph3'
                ),
            ])
        ])
    ]),
])

# CALLBACKS FIRST DROPDOWN

@ app.callback(
    Output('graph1', 'figure'),
    Input('Grafico-1', 'value'),
)
def update_output(value):
    if value == 'Obitos Acumulados por Região':
        fig = px.pie(piedataset1, names='Regiao', values='Obitos Novos', title="GRAFICO ESCOLHIDO",
                     color_discrete_sequence=px.colors.sequential.RdBu)
        fig.update_traces(textposition='inside', textinfo='percent+label')

    elif value == 'Casos Acumulados por Região':
        fig = px.pie(piedataset, names='Region', values='Casos Novos', title="GRAFICO ESCOLHIDO",
                     color_discrete_sequence=px.colors.sequential.RdBu)
        fig.update_traces(textposition='inside', textinfo='percent+label')

    elif value == 'Casos Novos por Estado':
        fig = px.line(dfdataset, x='Data', y='Casos Novos', color='Estado',
                      markers=True, title="GRAFICO ESCOLHIDO")
        fig.update_yaxes(title='Quantidade de Casos Novos',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    elif value == 'Casos Acumulados por Estado':
        fig = px.line(whiledataset, x='Data1', y='Casos Acumulados', color='Estado',
                      markers=True, title="GRAFICO ESCOLHIDO")
        fig.update_yaxes(title='Quantidade de Casos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    elif value == 'Obitos Novos por Estado':
        fig = px.line(dfdataset, x='Data', y='Obitos Novos', color='Estado',
                      markers=True, title="GRAFICO ESCOLHIDO")
        fig.update_yaxes(title='Quantidade de Obitos Novos',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    elif value == 'Obitos Acumulados por Estado':
        fig = px.line(whiledataset, x='Data1', y='Obitos Acumulados', color='Estado',
                      markers=True, title='Grafico Escolhido')
        fig.update_yaxes(title='Quantidade de Obitos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    else:
        fig = px.line(title="Região não especificada")
        fig.update_yaxes(title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    return fig

Estado = []
Data1 = []
CasosAcumulados = []
ObitosAcumulados = []
tableSudeste = []
tableSul = []
tableNorte = []
tableNordeste = []
tableCentrooeste = []
# i = 0
# tamanholista = len(tabela)
# while i < tamanholista:
# row = tabela[i]
for row in tabela:
    Estado = row[1]
    Data1 = row[2]
    CasosAcumulados = row[4]
    ObitosAcumulados = row[6]
    if not row[2] == '':
        if Estado == 'São Paulo' or Estado == 'Rio de Janeiro' or Estado == 'Espírito Santo' or Estado == 'Minas Gerais':
            if row[4] >= 1:
                tableSudeste.append(
                    [Data1, Estado, CasosAcumulados, ObitosAcumulados])
            whiledatasetSudeste = []
            for i in tableSudeste:
                whiledatasetSudeste.append({"Data Sudeste": i[0], "Estados Sudeste": i[1],
                                            "Casos Acumulados Sudeste": i[2], "Obitos Acumulados Sudeste": i[3]})
            # while i < tam:
            # i += 1
            # print('whiledatasetSudeste')
        elif Estado == 'Distrito Federal' or Estado == 'Mato Grosso do Norte' or Estado == 'Mato Grosso do Sul' or Estado == 'Goiás':
            if row[4] >= 1:
                tableCentrooeste.append(
                    [Data1, Estado, CasosAcumulados, ObitosAcumulados])
            whiledatasetCentrooeste = []
            for i in tableCentrooeste:
                whiledatasetCentrooeste.append({"Data Centro Oeste": i[0], "Estados Centro Oeste": i[1],
                                                "Casos Acumulados Centro Oeste": i[2], "Obitos Acumulados Centro Oeste": i[3]})
        elif Estado == 'Amazonas' or Estado == 'Acre' or Estado == 'Roraima' or Estado == 'Pará' or Estado == 'Rondônia' or Estado == 'Amapá' or Estado == 'Tocantins':
            if row[4] >= 1:
                tableNorte.append(
                    [Data1, Estado, CasosAcumulados, ObitosAcumulados])
            whiledatasetNorte = []
            for i in tableNorte:
                whiledatasetNorte.append({"Data Norte": i[0], "Estados Norte": i[1],
                                          "Casos Acumulados Norte": i[2], "Obitos Acumulados Norte": i[3]})
        elif Estado == 'Bahia' or Estado == 'Ceará' or Estado == 'Maranhão' or Estado == 'Paraíba' or Estado == 'Pernambuco' or Estado == 'Piauí' or Estado == 'Sergipe' or Estado == 'Rio Grande do Norte':
            if row[4] >= 1:
                tableNordeste.append(
                    [Data1, Estado, CasosAcumulados, ObitosAcumulados])
            whiledatasetNordeste = []
            for i in tableNordeste:
                whiledatasetNordeste.append({"Data Nordeste": i[0], "Estados Nordeste": i[1],
                                             "Casos Acumulados Nordeste": i[2], "Obitos Acumulados Nordeste": i[3]})
        elif Estado == 'Rio Grande do Sul' or Estado == 'Paraná' or Estado == 'Santa Catarina':
            if row[4] >= 1:
                tableSul.append(
                    [Data1, Estado, CasosAcumulados, ObitosAcumulados])
            whiledatasetSul = []
            for i in tableSul:
                whiledatasetSul.append({"Data Sul": i[0], "Estados Sul": i[1],
                                        "Casos Acumulados Sul": i[2], "Obitos Acumulados Sul": i[3]})

# CALLBACKS SECOND DROPDOWN

@app.callback(
    Output('graph2', 'figure'),
    Input('Grafico-2', 'value'),
)
def update_output(value):
    if value == 'Sudeste':
        fig = px.line(whiledatasetSudeste, x='Data Sudeste', y='Casos Acumulados Sudeste', color='Estados Sudeste',
                      markers=True, title="Casos Acumulados de Covid19 no Brasil por Região Desejada")
        fig.update_yaxes(title='Quantidade de Casos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    elif value == 'Sul':
        fig = px.line(whiledatasetSul, x='Data Sul', y='Casos Acumulados Sul', color='Estados Sul',
                      markers=True, title="Casos Acumulados de Covid19 Brasil por Região Desejada")
        fig.update_yaxes(title='Quantidade de Casos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    elif value == 'Norte':
        fig = px.line(whiledatasetNorte, x='Data Norte', y='Casos Acumulados Norte', color='Estados Norte',
                      markers=True, title="Casos Acumulados de Covid19 no Brasil por Região Desejada")
        fig.update_yaxes(title='Quantidade de Casos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    elif value == 'Nordeste':
        fig = px.line(whiledatasetNordeste, x='Data Nordeste', y='Casos Acumulados Nordeste', color='Estados Nordeste',
                      markers=True, title="Casos Acumulados de Covid19 no Brasil por Região Desejada")
        fig.update_yaxes(title='Quantidade de Casos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    elif value == 'Centro-Oeste':
        fig = px.line(whiledatasetCentrooeste, x='Data Centro Oeste', y='Casos Acumulados Centro Oeste', color='Estados Centro Oeste',
                      markers=True, title="Casos Acumulados de Covid19 no Brasil por Região Desejada")
        fig.update_yaxes(title='Quantidade de Casos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')
    
    else:
        fig = px.line(title="Região não especificada")
        fig.update_yaxes(title='Quantidade de Casos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    return fig

# CALLBACKS THIRD DROPDOWN

@app.callback(
    Output('graph3', 'figure'),
    Input('Grafico-3', 'value'),
)
def update_output(value):
    if value == 'Sudeste':
        fig = px.line(whiledatasetSudeste, x='Data Sudeste', y='Obitos Acumulados Sudeste', color='Estados Sudeste',
                      markers=True, title="Óbitos Acumulados de Covid19 no Brasil por Região Desejada")
        fig.update_yaxes(title='Quantidade de Óbitos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    elif value == 'Sul':
        fig = px.line(whiledatasetSul, x='Data Sul', y='Obitos Acumulados Sul', color='Estados Sul',
                      markers=True, title="Óbitos Acumulados de Covid19 no Brasil por Região Desejada")
        fig.update_yaxes(title='Quantidade de Óbitos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    elif value == 'Norte':
        fig = px.line(whiledatasetNorte, x='Data Norte', y='Obitos Acumulados Norte', color='Estados Norte',
                      markers=True, title="Óbitos Acumulados de Covid19 no Brasil por Região Desejada")
        fig.update_yaxes(title='Quantidade de Óbitos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    elif value == 'Nordeste':
        fig = px.line(whiledatasetNordeste, x='Data Nordeste', y='Obitos Acumulados Nordeste', color='Estados Nordeste',
                      markers=True, title="Óbitos Acumulados de Covid19 no Brasil por Região Desejada")
        fig.update_yaxes(title='Quantidade de Óbitos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    elif value == 'Centro-Oeste':
        fig = px.line(whiledatasetCentrooeste, x='Data Centro Oeste', y='Obitos Acumulados Centro Oeste', color='Estados Centro Oeste',
                      markers=True, title="Óbitos Acumulados de Covid19 no Brasil por Região Desejada")
        fig.update_yaxes(title='Quantidade de Óbitos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    else:
        fig = px.line(title="Região não especificada")
        fig.update_yaxes(title='Quantidade de Óbitos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green')
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
