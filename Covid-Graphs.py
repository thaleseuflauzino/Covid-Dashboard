# Grupo G - Coronavírus (COVID-19) in Brazil

### Membros

|Matrícula|Nome Completo|
|:---|:---|
|200061143|Calebe Cardoso de Aragão|
|222008468|Danilo Sarmento Barros|
|222029243|Victor Hugo dos Santos Bernardes |
|222006178|Thales Henrique Euflauzino dos Santos |
|222008922|Júlio César da Costa Santos |
|222023590|João Victor Fonseca Reis |

import pandas as pd
from numpy.lib.function_base import average
import io
_str = '''|Grafico|O|LO|CD|CG|CC|
|Gráfico de porcentagem de casos acumulados de COVID-19 no Brasil| 10|10|10|10|10|
|Grafico de porcentagem de óbitos acumulados de COVID-19 no Brasil| 10|10|10|10|10|
|Gráfico dos Casos Novos de COVID-19 no Brasil por estado em relação a região Sudeste| 10|10|10|10|10|
|Gráfico dos Casos Acumulados de COVID-19 no Brasil por estado em relação a região Sudeste| 10|10|10|10|10|
|Gráfico dos Óbitos Novos de COVID-19 no Brasil por estado em relação a região Sudeste| 10|10|10|10|10|
|Gráfico dos Óbitos Acumulados de COVID-19 no Brasil por estado em relação a região Sudeste| 10|10|10|10|10|
'''
strIO = io.StringIO(_str)
df = pd.read_csv(strIO, sep='|', ).iloc[:, 1:-1]
df['N'] = df['CC']*(df['O']+ 2*df['LO']+4*df['CD']+3*df['CG'])/10
display(df)
print(f'AGP = {df[["N"]].mean()[0]}')

## Objetivo

O intuito desse projeto é analisar os dados refentes ao inicio do contágio do vírus SARS-CoV-2, o coronavírus (COVID-19) no Brasil no período entre o início de 2020 até o dia 14 de abril do mesmo ano, tendo em vista como foi dado contágio por meio dos casos além de analisar os óbitos que pesaram o país.

## Bases de Dados


|Nome|Descrição|Colunas| Amostras|
|:---|:---|--:|--:|
|[Base 1](https://drive.google.com/file/d/1WJKA-2bSywKdDnU6Bv547qXIYwgm_urs/view?usp=share_link)|Dados sobre a pandemia de Covid19 no Brasil|7|2052|


### Base 1

import pandas as pd
import plotly.express as px

from google.colab import drive
drive.mount('/content/drive')

dataset = pd.read_csv('/content/drive/MyDrive/COVID19ee.csv', sep = ",")
tabela = dataset.values.tolist()

dataset.head(5)

## Gráficos

1. Gráfico de porcentagem de casos acumulados de COVID-19 no Brasil.
2. Grafico de porcentagem de óbitos acumulados de COVID-19 no Brasil.
3. Gráfico dos Casos Novos de COVID-19 no Brasil por estado em relação a região Sudeste.
4.  Gráfico dos Casos Acumulados de COVID-19 no Brasil por estado em relação a região Sudeste.
5. Gráfico dos Óbitos Novos de COVID-19 no Brasil por estado em relação a região Sudeste.
6. Gráfico dos Óbitos Acumulados de COVID-19 no Brasil por estado em relação a região Sudeste.

### Gráfico de porcentagem de Casos Acumulados de COVID-19 no Brasil.

O intuito deste gráfico é apresentar a porcentagem do Casos Acumulados de Covid19 no Brasil por região.



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

### Gráfico de porcentagem de Óbitos Acumulados de COVID-19 no Brasil.

O intuito deste gráfico é apresentar a porcentagem de óbitos acumulados de Covid19 no Brasil por região.


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

### Estrutura de códigos para os gráficos de linha.

Essa estrutura tem o objetivo de gerar os dados dos gráficos de linhas filtrando pelos estados da região Sudeste.


Código usado para Casos/Óbitos novos com FOR.

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
    # if Estado == 'São Paulo' or Estado == 'Rio de Janeiro' or Estado == 'Espírito Santo' or Estado == 'Minas Gerais':
       TabelaNova.append([Data, Estado, CasosNovos, ObitosNovos])

for i in TabelaNova:
  dfdataset.append({"Data": i[0], "Estado": i[1], "Casos Novos": i[2], "Obitos Novos": i[3]})

Código usado para Casos/Óbitos acumulados com WHILE.

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
    whiledataset.append({"Data1": tablewhile[i][0], "Estado": tablewhile[i][1], "Casos Acumulados": tablewhile[[i]2], "Obitos Acumulados": tablewhile[i][3]})
    i += 1

### Gráfico dos Casos Novos de COVID-19 no Brasil por estado em relação a região Sudeste.

Esse gráfico tem como função demonstrar exponencialmente o crescimento de Casos Novos de Covid19 no Brasil por estado, desde o início do ano de 2020.



x = px.line(dfdataset, x = 'Data', y = 'Casos Novos',title= 'Casos Novos de Covid19 no Brasil por Estado em Relação a Região Sudeste', color= 'Estado', markers=True)
x.update_yaxes(title= 'Quantidade de Casos Novos',title_font_color = 'red', ticks = 'outside', tickfont_color='green')
x.update_xaxes(title_text='Dias do ano', title_font_color='red', ticks='outside',tickfont_color='green')
x.show()

### Gráfico dos Casos Acumulados de COVID-19 no Brasil por estado em relação a região Sudeste.

Esse gráfico tem como função demonstrar exponencialmente o crescimento de Casos Acumulados de Covid19 no Brasil por estado, desde o início do ano de 2020.



fig = px.line(whiledataset, x = 'Data1', y = 'Casos Acumulados',title= 'Casos Acumulados de Covid19 no Brasil por Estado em Relação a Região Sudeste', color= 'Estado', markers=True)
fig.update_yaxes(title= 'Quantidade de Casos Acumulados',title_font_color = 'red', ticks = 'outside', tickfont_color='green')
fig.update_xaxes(title_text='Dias do ano', title_font_color='red',ticks='outside',tickfont_color='green')
fig.show()

###Gráfico dos Óbitos Novos de COVID-19 no Brasil por estado em relação a região Sudeste.

Esse gráfico tem como função demonstrar exponencialmente o crescimento de óbitos novos de Covid19 no Brasil por estado, desde o início do ano de 2020.



fig = px.line(dfdataset, x = 'Data', y = 'Obitos Novos',title= 'Obitos Novos de Covid19 no Brasil por Estado em Relação a Região Sudeste', color= 'Estado', markers=True)
fig.update_yaxes(title= 'Quantidade de Obitos Novos',title_font_color = 'red', ticks = 'outside', tickfont_color='green')
fig.update_xaxes(title_text='Dias do ano', title_font_color='red',ticks='outside',tickfont_color='green')
fig.show()

###Gráfico dos Óbitos Acumulados de COVID-19 no Brasil por estado em relação a região Sudeste.

Esse gráfico tem como função demonstrar exponencialmente o crescimento de óbitos acumulados de Covid19 no Brasil por estado, desde o início do ano de 2020.


fig = px.line(whiledataset, x = 'Data1', y = 'Obitos Acumulados',title= 'Obitos Acumulados de Covid19 no Brasil por Estado em Relação a Região Sudeste', color= 'Estado', markers=True)
fig.update_yaxes(title= 'Quantidade de Obitos Acumulados',title_font_color = 'red', ticks = 'outside', tickfont_color='green')
fig.update_xaxes(title_text='Dias do ano', title_font_color='red',ticks='outside',tickfont_color='green')
fig.show()
