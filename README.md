# Trabalho final de Data Warehousing
Os dados que foram utilizados nas análises estão na pasta *dados_trabalhados*. Os gráficos com as análises estão na pasta *graficos*. O script utilizado para geração dos gráficos está dentro da pasta *scripts*.

## Geração dos gráficos
Para gerar os gráficos, basta rodar o script `gera_graficos.py`. As imagens com os gráficos serão salvas dentro da pasta *graficos*.

## ETL
O modelo lógico do banco de dados, o schema utilizado no banco de dados, o banco com alguns dos dados inseridos e o arquivo de transformação do petaho utilizado para o ETL, podem ser visto dentro da pasta *etl*.

## Limitações
Alguns dados não foram inseridos no banco de dados pois o processo de carga estava demorando muito com o PDI (Pentaho Data Integration). Com isso, para gerar as análises, utilizamos os dados desnormalizados que estão dentro da pasta *dados_trabalhados*.