import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Caminho do arquivo CSV
caminho_arquivo_valores_municipio = '../dados_trabalhados/valores_municipio/tb_valores_municipio.csv'
caminho_arquivo_beneficiarios_bf = '../dados_trabalhados/valores_beneficiarios/tb_pagamento_disponibilizado_bf.csv'
caminho_arquivo_beneficiarios_ab = '../dados_trabalhados/valores_beneficiarios/tb_pagamento_disponibilizado_ab.csv'
caminho_arquivo_beneficiarios_ae = '../dados_trabalhados/valores_beneficiarios/tb_pagamento_disponibilizado_ae.csv'
caminho_arquivo_beneficiarios_bpc = '../dados_trabalhados/valores_beneficiarios/tb_pagamento_disponibilizado_bpc.csv'


# Caminho de saída para os gráficos
caminho_saida_graficos_valores_municipio = '../graficos/'
caminho_saida_grafico_dependentes_bf = '../graficos/grafico_dependentes_bf.png'
caminho_saida_grafico_medias_beneficios = '../graficos/grafico_medias_beneficios.png'
caminho_saida_grafico_pizza_bpc = '../graficos/grafico_pizza_bpc.png'
caminho_saida_grafico_scatter_bf_bpc = '../graficos/grafico_scatter_bf_bpc.png'


# Carrega o arquivo CSV de valores do município
df_valores_municipio = pd.read_csv(caminho_arquivo_valores_municipio)

# Dicionário com os benefícios e seus respectivos nomes
beneficios = {
    'BolsaFamilia': 'Bolsa Família',
    'AuxilioEmergencial': 'Auxílio Emergencial',
    'bpc': 'BPC',
    'AuxilioBrasil': 'Auxílio Brasil'
}

# Loop sobre os benefícios
for beneficio, nome_beneficio in beneficios.items():
    # Filtra os registros do benefício atual
    df_beneficio = df_valores_municipio[df_valores_municipio['Benefício'] == nome_beneficio].copy()  # Faz uma cópia do DataFrame
    
    # Extrai o ano e o mês da coluna Mes Referência
    df_beneficio['Data'] = pd.to_datetime(df_beneficio['Mes Referência']).copy()  # Faz uma cópia da coluna
    df_beneficio.sort_values(by='Data', inplace=True)
    
    # Cria o gráfico de dispersão para o benefício atual
    plt.plot(df_beneficio['Data'], df_beneficio['Valor'], color='blue')
    plt.scatter(df_beneficio['Data'], df_beneficio['Valor'], color='blue')

    # Define os rótulos dos eixos
    plt.xlabel('Meses')
    plt.ylabel('Valor')
    
    # Define o título do gráfico
    plt.title(f'Valores disponibilizados - {nome_beneficio}')
    plt.xticks(rotation=45)
    
    # Define o path de saída para a imagem
    caminho_saida_imagem = f'{caminho_saida_graficos_valores_municipio}valores_disponibilizados_{beneficio}.png'
    plt.tight_layout()

    # Salva o gráfico como imagem
    plt.savefig(caminho_saida_imagem)
    
    # Limpa o gráfico atual
    plt.clf()


# Carrega o arquivo CSV de beneficiários do Bolsa Família
df_beneficiarios_bf = pd.read_csv(caminho_arquivo_beneficiarios_bf)

# Calcular a média da Quantidade Dependentes por mês
meses = pd.to_datetime(df_beneficiarios_bf['Mes Referência'], format='%Y-%m-%d')
df_media_dependentes_bf = df_beneficiarios_bf.groupby(meses)['Quantidade Dependentes'].mean()

# Define as coordenadas no eixo x
fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Plota o gráfico
ax.plot(df_media_dependentes_bf.index, df_media_dependentes_bf.values)
ax.scatter(df_media_dependentes_bf.index, df_media_dependentes_bf.values)
plt.xlabel('Meses')
plt.ylabel('Média')
plt.title('Média da quantidade de dependentes no Bolsa Família')
plt.gcf().set_size_inches(12, 5)
plt.tight_layout()

# Salva o gráfico como imagem
plt.savefig(caminho_saida_grafico_dependentes_bf)

plt.clf()

##################################################

# Lista dos nomes dos arquivos
nomes_arquivos = [
    caminho_arquivo_beneficiarios_ab,
    caminho_arquivo_beneficiarios_ae,
    caminho_arquivo_beneficiarios_bpc
]

nomes_beneficios_analisados = ['Auxílio Emergencial','BPC', 'Auxílio Brasil']

# Dicionário para mapear os nomes das colunas de valor por benefício
colunas_valores = {
    caminho_arquivo_beneficiarios_ab: 'Valor',
    caminho_arquivo_beneficiarios_ae: 'Valor Disponibilizado',
    caminho_arquivo_beneficiarios_bpc: 'Valor'
}

# Lista para armazenar as médias dos valores por benefício
medias_valores = []

for nome_arquivo in nomes_arquivos:
    # Carrega o arquivo CSV
    df_beneficiarios = pd.read_csv(nome_arquivo)
    
    # Obtém o nome da coluna de valores para o benefício atual
    coluna_valor = colunas_valores[nome_arquivo]
    
    # Calcula a média dos valores para o benefício atual
    media_valor = df_beneficiarios[coluna_valor].mean()
    
    # Adiciona a média à lista de médias de valores
    medias_valores.append(media_valor)

# Cria o gráfico de barras
plt.bar(nomes_beneficios_analisados, medias_valores)
plt.xlabel('Benefício')
plt.ylabel('Média dos valores (R$)')
plt.title('Média dos valores por Benefício')
plt.gcf().set_size_inches(5, 5)
plt.tight_layout()

# Salva o gráfico como imagem
plt.savefig(caminho_saida_grafico_medias_beneficios)

plt.clf()

########################################

# Carrega o arquivo CSV do benefício BPC
df_beneficiarios_bpc = pd.read_csv(caminho_arquivo_beneficiarios_bpc)

# Contar o número de registros concedidos judicialmente e não concedidos
concedido_judicialmente = df_beneficiarios_bpc['Concedido Judicialmente'].value_counts()

# Calcular as porcentagens
porcentagem_concedido = concedido_judicialmente[True] / len(df_beneficiarios_bpc) * 100
porcentagem_nao_concedido = concedido_judicialmente[False] / len(df_beneficiarios_bpc) * 100

# Criar o gráfico de pizza
labels = ['Concedido judicialmente', 'Não concedido judicialmente']
sizes = [porcentagem_concedido, porcentagem_nao_concedido]
explode = [0.1, 0]  # Explodir a primeira fatia (Concedido Judicialmente)
colors = ['lightskyblue', 'lightcoral']

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Mantém o aspecto de um círculo

# Define o título do gráfico
plt.title('Benefício BPC: Porcentagem de benefícios concedidos judicialmente')
plt.gcf().set_size_inches(8, 5)
plt.tight_layout()

# Salva o gráfico como imagem
plt.savefig(caminho_saida_grafico_pizza_bpc)

plt.clf()

###################################################

# Carrega os arquivos CSV de beneficiários do Bolsa Família e BPC
df_beneficiarios_bf = pd.read_csv(caminho_arquivo_beneficiarios_bf)
df_beneficiarios_bpc = pd.read_csv(caminho_arquivo_beneficiarios_bpc)

# Filtrar os beneficiários que receberam Bolsa Família e BPC simultaneamente
beneficiarios_simultaneos = df_beneficiarios_bf.merge(df_beneficiarios_bpc, on=['CPF Beneficiário', 'Beneficiário', 'Mes Referência'])

# Extrair o ano e o mês da coluna Mes Referência
beneficiarios_simultaneos['Data'] = pd.to_datetime(beneficiarios_simultaneos['Mes Referência'], format='%Y-%m-%d')

# Calcular a quantidade de beneficiários simultâneos por mês
beneficiarios_por_mes = beneficiarios_simultaneos.groupby('Data').size()


# Cria o gráfico de dispersão
fig, ax = plt.subplots()
ax.plot(beneficiarios_por_mes.index, beneficiarios_por_mes.values)
ax.scatter(beneficiarios_por_mes.index, beneficiarios_por_mes.values)
ax.format_xdata = mdates.DateFormatter('%H:%M:%S')

plt.yticks(fontsize=20, rotation=45)
plt.xticks(fontsize=15, rotation=45)
plt.xlabel('Meses', fontsize=20)
plt.ylabel('Quantidade de Beneficiários', fontsize=20)
plt.title('Quantidade de beneficiários que receberam o Bolsa Família e o BPC simultaneamente', fontsize=17)

plt.gcf().set_size_inches(12, 10)
plt.tight_layout()

# Salva o gráfico como imagem
plt.savefig(caminho_saida_grafico_scatter_bf_bpc)