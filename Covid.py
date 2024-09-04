from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Inicializar o aplicativo Dash
app = Dash(__name__)

# Ler o dataset
dataset = pd.read_csv('database.csv', sep=",")

# Converter para lista de listas
tabela = dataset.values.tolist()

# Processar dados para gráficos de pizza
piedataset = [{"Region": row[0], "Casos Novos": row[3]} for row in tabela if row[2] != '']
piedataset1 = [{"Regiao": row[0], "Obitos Novos": row[5]} for row in tabela if row[2] != '']

# Converter para DataFrames e agregar
df_piedataset = pd.DataFrame(piedataset)
df_piedataset1 = pd.DataFrame(piedataset1)

df_piedataset_agg = df_piedataset.groupby('Region').sum().reset_index()
df_piedataset1_agg = df_piedataset1.groupby('Regiao').sum().reset_index()

# Processar dados para gráficos de linha
dfdataset = [
    {
        "regiao": row[0], 
        "Data": row[2], 
        "Estado": row[1], 
        "Casos Novos": row[3], 
        "Obitos Novos": row[5]
    } 
    for row in tabela 
    if row[2] != ''
]

dfdataset = pd.DataFrame(dfdataset)

whiledataset = [
    {
        "Data1": row[2], 
        "Estado": row[1], 
        "Casos Acumulados": row[4], 
        "Obitos Acumulados": row[6]
    } 
    for row in tabela 
    if row[2] != '' and pd.notna(row[4]) and row[4] >= 1
]

whiledataset = pd.DataFrame(whiledataset)

# Inicializar listas regionais
whiledatasetSudeste = []
whiledatasetSul = []
whiledatasetNorte = []
whiledatasetNordeste = []
whiledatasetCentrooeste = []

# Processar dados regionais
for row in tabela:
    if row[2] != '':
        data, estado, casos_acumulados, obitos_acumulados = row[2], row[1], row[4], row[6]
        if estado in ['São Paulo', 'Rio de Janeiro', 'Espírito Santo', 'Minas Gerais']:
            whiledatasetSudeste.append({
                "Data": data, 
                "Estado": estado, 
                "Casos_Acumulados": casos_acumulados, 
                "Obitos_Acumulados": obitos_acumulados
            })
        elif estado in ['Distrito Federal', 'Mato Grosso do Norte', 'Mato Grosso do Sul', 'Goiás']:
            whiledatasetCentrooeste.append({
                "Data": data, 
                "Estado": estado, 
                "Casos_Acumulados": casos_acumulados, 
                "Obitos_Acumulados": obitos_acumulados
            })
        elif estado in ['Amazonas', 'Acre', 'Roraima', 'Pará', 'Rondônia', 'Amapá', 'Tocantins']:
            whiledatasetNorte.append({
                "Data": data, 
                "Estado": estado, 
                "Casos_Acumulados": casos_acumulados, 
                "Obitos_Acumulados": obitos_acumulados
            })
        elif estado in ['Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Sergipe', 'Rio Grande do Norte']:
            whiledatasetNordeste.append({
                "Data": data, 
                "Estado": estado, 
                "Casos_Acumulados": casos_acumulados, 
                "Obitos_Acumulados": obitos_acumulados
            })
        elif estado in ['Rio Grande do Sul', 'Paraná', 'Santa Catarina']:
            whiledatasetSul.append({
                "Data": data, 
                "Estado": estado, 
                "Casos_Acumulados": casos_acumulados, 
                "Obitos_Acumulados": obitos_acumulados
            })

# Converter listas regionais para DataFrames
df_sudeste = pd.DataFrame(whiledatasetSudeste)
df_sul = pd.DataFrame(whiledatasetSul)
df_norte = pd.DataFrame(whiledatasetNorte)
df_nordeste = pd.DataFrame(whiledatasetNordeste)
df_centrooeste = pd.DataFrame(whiledatasetCentrooeste)

# Definir layout do Dash
app.layout = html.Div(className='container', children=[
    html.H1('Coronavírus (COVID-19) no Brasil.'),
    html.H2('Gráficos sobre COVID-19 no Brasil entre Janeiro e Abril de 2022.'),
    html.H3('Escolha o Gráfico referente ao dado desejado.'),
    dcc.Dropdown(
        ['Obitos Acumulados por Região', 'Casos Acumulados por Região', 'Casos Novos por Estado', 'Casos Acumulados por Estado', 'Obitos Novos por Estado', 'Obitos Acumulados por Estado'], 
        value='NYC', 
        id='Grafico-1', 
        className='dccDropdown'
    ),
    dcc.Graph(id='graph1', className='dccGraph'),
    html.H2('Casos Acumulados de COVID19 no Brasil por Região'),
    html.H3('Escolha qual região deseja ver os dados'),
    dcc.Dropdown(
        ['Sudeste', 'Sul', 'Centro-Oeste', 'Norte', 'Nordeste'], 
        value='NYC', 
        id='Grafico-2', 
        className='dccDropdown',
    ),
    dcc.Graph(id='graph2', className='dccGraph'),
    html.H2('Óbitos Acumulados de COVID19 no Brasil por Região'),
    html.H3('Escolha qual região deseja ver os dados'),
    dcc.Dropdown(
        ['Sudeste', 'Sul', 'Centro-Oeste', 'Norte', 'Nordeste'], 
        value='NYC', 
        id='Grafico-3', 
        className='dccDropdown'
    ),
    dcc.Graph(id='graph3', className='dccGraph')
])

# CALLBACKS

# Callback para o Gráfico 1
@app.callback(Output('graph1', 'figure'), Input('Grafico-1', 'value'))
def update_graph1(value):
    if value == 'Obitos Acumulados por Região':
        fig = px.pie(
            df_piedataset1_agg, 
            names='Regiao', 
            values='Obitos Novos', 
            title="Óbitos Novos por Região", 
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        

    elif value == 'Casos Acumulados por Região':
        fig = px.pie(
            df_piedataset_agg, 
            names='Region', 
            values='Casos Novos', 
            title="Casos Novos por Região", 
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        

    elif value == 'Casos Novos por Estado':
        fig = px.line(
            dfdataset, 
            x='Data', 
            y='Casos Novos', 
            color='Estado', 
            markers=True, 
            title="Casos Novos por Estado"
        )
        fig.update_yaxes(title='Quantidade de Casos Novos',
                         title_font_color='red', ticks='outside', tickfont_color='green', showgrid=False)   
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green', showgrid=False)

    elif value == 'Casos Acumulados por Estado':
        fig = px.line(
            whiledataset, 
            x='Data1', 
            y='Casos Acumulados', 
            color='Estado', 
            markers=True, 
            title="Casos Acumulados por Estado"
        )
        fig.update_yaxes(title='Quantidade de Casos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green', showgrid=False)
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green', showgrid=False)

    elif value == 'Obitos Novos por Estado':
        fig = px.line(
            dfdataset, 
            x='Data', 
            y='Obitos Novos', 
            color='Estado', 
            markers=True, 
            title="Óbitos Novos por Estado"
        )
        fig.update_yaxes(title='Quantidade de Óbitos Novos',
                         title_font_color='red', ticks='outside', tickfont_color='green', showgrid=False)
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green', showgrid=False)

    elif value == 'Obitos Acumulados por Estado':
        fig = px.line(
            whiledataset, 
            x='Data1', 
            y='Obitos Acumulados', 
            color='Estado', 
            markers=True, 
            title='Óbitos Acumulados por Estado'
        )
        fig.update_yaxes(title='Quantidade de Óbitos Acumulados',
                         title_font_color='red', ticks='outside', tickfont_color='green', showgrid=False)
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green', showgrid=False)

    else:
        fig = px.line(title="Região não especificada")
        fig.update_yaxes(title_font_color='red', ticks='outside', tickfont_color='green', showgrid=False)
        fig.update_xaxes(title_text='Dias do ano', title_font_color='red',
                         ticks='outside', tickfont_color='green', showgrid=False)
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    return fig

# Callback para o Gráfico 2
@app.callback(Output('graph2', 'figure'), Input('Grafico-2', 'value'))
def update_graph2(value):
    datasets = {
        'Sudeste': df_sudeste, 
        'Sul': df_sul, 
        'Norte': df_norte, 
        'Nordeste': df_nordeste, 
        'Centro-Oeste': df_centrooeste
    }
    df = datasets.get(value, pd.DataFrame())

    if not df.empty:
        fig = px.line(
            df, 
            x='Data', 
            y='Casos_Acumulados', 
            color='Estado', 
            markers=True, 
            title=f"Casos Acumulados de Covid19 no Brasil no {value}"
        )
    else:
        fig = px.line(title="Região não especificada")
    
    # Personalização do plano de fundo
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    
    return fig

# Callback para o Gráfico 3
@app.callback(Output('graph3', 'figure'), Input('Grafico-3', 'value'))
def update_graph3(value):
    datasets = {
        'Sudeste': df_sudeste, 
        'Sul': df_sul, 
        'Norte': df_norte, 
        'Nordeste': df_nordeste, 
        'Centro-Oeste': df_centrooeste
    }
    df = datasets.get(value, pd.DataFrame())

    if not df.empty:
        fig = px.line(
            df, 
            x='Data', 
            y='Obitos_Acumulados', 
            color='Estado', 
            markers=True, 
            title=f"Óbitos Acumulados de Covid19 no Brasil no {value}"
        )
    else:
        fig = px.line(title="Região não especificada")
    
    # Personalização do plano de fundo
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    
    return fig

# Executar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)