#%config IPCompleter.greedy = True
#import pymysql
import numpy as np 

#conn=pymysql.connect(host="localhost", user="uffdata", passwd="uffdata123", db="dwebd152")
#uffdata = conn.cursor()

#sqlCurso = 'SELECT * from BI_DMCURSO;'
#curso = uffdata.execute(sqlCurso)
#print("Number of Curses at UFF: ", curso)

#data = uffdata.fetchone()
#print(data)

a = np.random.randn(2, 3) # a.shape = (2, 3)
b = np.random.randn(2, 1) # b.shape = (2, 1)
c = a + b