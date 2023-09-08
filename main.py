import pandas as pd
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def pagInicial():
  tabela = pd.read_csv('tabela.csv')
  tabela_vendas = tabela['Vendas'].sum()

  resposta = {'O TOTAL DE VENDAS ': tabela_vendas}

  return jsonify(resposta)

app.run(host='0.0.0.0')


# tabela = pd.read_csv('tabela.csv')
# print(tabela)