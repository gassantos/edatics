"""
docs 
"""

import pymysql as psql

import pandas as pd
from pandas import *
from seaborn import *
from matplotlib.pyplot import *

import numpy as np
from statsmodels.formula.api import *
#%matplotlib inline 

pd.options.display.max_columns = None
pd.options.display.max_seq_items = None
np.set_printoptions(threshold=np.inf)

# Conjunto de Dados com os Alunos Formados
conn=psql.connect(host="localhost", user="uffdata", passwd="uffdata123", db="dwebd152")
df = pd.read_sql('SELECT * from BI_DMALUNO WHERE CODSITUACAOALUNO=0 && (CODSTATUSALUNO=8 || CODSTATUSALUNO=21);', conn)
print('Números de registros:', len(df))
conn.close()

# Listando todos os campos do dataframe
df.all()

# Uma amostra de apresentação do Dataframe
df.head(20)

# Descrição do Dataframe com Número de registros e Colunas
df.shape

# Distribuição dos Valores de Coeficiente de Rendimento dos alunos formados.
df.CR.values

# Avaliação descritiva com o resumo de tendência central, dispersão e a distribuição do dataset.
df.CR.describe().round(2)

# O CR Médio dos Alunos formados
round(df.CR.mean(), 2)

# Construção de Gráficos com base no COEFICIENTE DE RENDIMENTO
df.CR.plot.hist();

# Construção de Gráficos
df.CR.plot.density();
distplot(df.CR, hist=False);

scatter(df.CR, df.CODCURSO, s=10, c='blue', marker='+', data=df);
df.groupby('SEXO').CR.describe()
df.groupby("SEXO").COR.describe()