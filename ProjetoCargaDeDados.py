import pyodbc
import pandas as pd

conexao = (
    'Driver={SQL Server};'
    'Server=LAYS-GUERRA;'
    'Database = projetos;'
)

conexao_instancia = pyodbc.connect(conexao)

cursor = conexao_instancia.cursor()

df = pd.read_csv('D:\SCRIPTS\ARQUIVO.CSV')

for index,row in df.iterrows():
    cursor.execute(
        'INSERT INTO login (ID,NOME,CPF) VALUES(?,?,?)'
        ,row.ID
        ,row.NOME
        ,row.CPF
    )

conexao_instancia.commit()
cursor.close()


