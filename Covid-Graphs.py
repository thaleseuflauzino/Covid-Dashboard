import pandas as pd
import plotly.express as px

dataset = pd.read_csv('dataBase.csv', sep = ",")
tabela = dataset.values.tolist()

dataset.head(5)

##GRAPH 1

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

fig = px.pie(piedataset, values="Casos Novos", names="Region", color="Region", title='Porcentagem de Casos Acumulados de Covid19 por Região em relação ao Brasil',
             color_discrete_map={'Nordeste':'red',
                                 'Norte':'darkorange',
                                 'Centro-Oeste':'deeppink',
                                 'Sul':'yellow',
                                 'Sudeste':'darkred'})
fig.update_traces(textposition = 'inside', textinfo = 'percent+label')
fig.show()

##GRAPH 2
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
    piedataset1.append({"Regiao": tablepie1[i][0], "Obitos Novos": tablepie1[i][1]})
    i += 1

fig = px.pie(piedataset1, values = 'Obitos Novos', names = 'Regiao', color = 'Regiao', title = 'Porcentagem de Óbitos Acumulados de Covid19 por Região em relação ao Brasil',
             color_discrete_map={'Nordeste':'red',
                                 'Norte':'darkorange',
                                 'Centro-Oeste':'deeppink',
                                 'Sul':'yellow',
                                 'Sudeste':'darkred'})
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()

##GRAPH 3
Estado = []
Data = []
CasosNovos = []
ObitosNovos = []
TabelaNova = []
dfdataset = []

for row in tabela:
  Estado = row[1]
  Data = row[2]
  CasosNovos = row[3]
  ObitosNovos = row[5]
  if not row[2] == '':
    # na linha abaixo usamos para restringir estados desejados
    # if Estado == 'São Paulo' or Estado == 'Rio de Janeiro' or Estado == 'Espírito Santo' or Estado == 'Minas Gerais':
       TabelaNova.append([Data, Estado, CasosNovos, ObitosNovos])

for i in TabelaNova:
  dfdataset.append({"Data": i[0], "Estado": i[1], "Casos Novos": i[2], "Obitos Novos": i[3]})

x = px.line(dfdataset, x = 'Data', y = 'Casos Novos',title= 'Casos Novos de Covid19 no Brasil por Estado em Relação a Região Sudeste', color= 'Estado', markers=True)
x.update_yaxes(title= 'Quantidade de Casos Novos',title_font_color = 'red', ticks = 'outside', tickfont_color='green')
x.update_xaxes(title_text='Dias do ano', title_font_color='red', ticks='outside',tickfont_color='green')
x.show()

## GRAPH 4

Estado = []
Data1 = []
CasosAcumulados = []
ObitosAcumulados = []
tablewhile = []
whiledataset = []
print(tabela)

i = 0
tamanholista = len(tabela)
while i < tamanholista:
  row = tabela[i]
  Estado = row[1]
  Data1 = row[2]
  CasosAcumulados = row[4]
  ObitosAcumulados = row[6]

  if not row[2] == '':
    if Estado == 'São Paulo' or Estado == 'Rio de Janeiro' or Estado == 'Espírito Santo' or Estado == 'Minas Gerais':
      if row[4] >= 1:
        tablewhile.append([Data1, Estado, CasosAcumulados, ObitosAcumulados])
  i += 1

i = 0
tamanho = len(tablewhile)
while i < tamanho:
    whiledataset.append({"Data1": tablewhile[i][0], "Estado": tablewhile[i][1], "Casos Acumulados": tablewhile[i][2], "Obitos Acumulados": tablewhile[i][3]})
    i += 1

fig = px.line(whiledataset, x = 'Data1', y = 'Casos Acumulados',title= 'Casos Acumulados de Covid19 no Brasil por Estado em Relação a Região Sudeste', color= 'Estado', markers=True)
fig.update_yaxes(title= 'Quantidade de Casos Acumulados',title_font_color = 'red', ticks = 'outside', tickfont_color='green')
fig.update_xaxes(title_text='Dias do ano', title_font_color='red',ticks='outside',tickfont_color='green')
fig.show()