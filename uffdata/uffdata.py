#%config IPCompleter.greedy = True
import pymysql
conn=pymysql.connect(host="localhost", user="uffdata", passwd="uffdata123", db="dwebd152")
uffdata = conn.cursor()

sqlCurso = 'SELECT * from BI_DMCURSO;'
curso = uffdata.execute(sqlCurso)
print("Number of Curses at UFF: ", curso)

data = uffdata.fetchone()
print(data)
