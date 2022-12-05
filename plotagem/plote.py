import matplotlib.pyplot as plt
import matplotlib.gridspec as grids
import matplotlib.figure as fig
import numpy as np
import firebirdsql
con = firebirdsql.connect(user = "SYSDBA", password = "masterkey",database = "C:\BD\CHAT.FDB",host = "localhost",charset = "ANSI")
x = [0,1,2,3];
#Gra
gs = grids.GridSpec(3, 3)
plt.subplot(gs[0, :])

plt.title('Estado Bom', color = 'black', fontweight= 'bold', fontsize=12)
#plt.xlabel('Eixo X', fontsize=16)
#plt.ylabel('Eixo Y', fontsize=16)


#ALIMENTO
curALIMENTO = con.cursor()
curALIMENTO.execute("SELECT CONTADOR FROM ANALISE_GRAFICA WHERE TABELA = 'ALIMENTO' AND ESTADO = 'alimento bom' ORDER BY REFERENCIA ASC")
contALIMENTO = curALIMENTO.fetchall()
plt.plot(contALIMENTO , c='r', ls = '-', lw='1', marker='o', label ='Alimento')
#HUMOR
curHUMOR = con.cursor()
curHUMOR.execute("SELECT CONTADOR FROM ANALISE_GRAFICA WHERE TABELA = 'HUMOR' AND ESTADO = 'humor bom' ORDER BY REFERENCIA ASC")
contHUMOR = curHUMOR.fetchall()
plt.plot(contHUMOR, c='g',ls ='-', lw='1', marker='^', fillstyle='right', label='Humor')
#SONO
curSONO = con.cursor()
curSONO.execute("SELECT CONTADOR FROM ANALISE_GRAFICA WHERE TABELA = 'SONO' AND ESTADO = 'sono bom' ORDER BY REFERENCIA ASC")
contSONO = curSONO.fetchall()
plt.plot(contSONO, c='b', ls = '-', lw='1', marker='s', label='Sono')
#print (x)

#EIXO Y
curY = con.cursor()
curY.execute("SELECT DISTINCT extract(day from REFERENCIA) ||'/'|| extract(month from REFERENCIA) ||'/'|| extract(year from REFERENCIA) as DATAS FROM ANALISE_GRAFICA ORDER BY REFERENCIA ASC")
contY = curY.fetchall()

#CONT Y
curY2 = con.cursor()
curY2.execute("SELECT ROW_NUMBER() OVER(ORDER BY REFERENCIA) FROM ( SELECT DISTINCT REFERENCIA FROM ANALISE_GRAFICA) TB1 ORDER BY REFERENCIA ASC")
contY2 = curY2.fetchall()


y = contY
plt.xticks(x, y)
#plt.plot(x1, c='r', ls = '-', lw='1', marker='o', label ='Paciente.1')

#Grafico2
plt.subplot(gs[1, :])
plt.title('Estado Moderado', color = 'black', fontweight= 'bold', fontsize=12)
#plt.xlabel('Eixo X', fontsize=16)
#plt.ylabel('Eixo Y', fontsize=16)


#ALIMENTO
curALIMENTO = con.cursor()
curALIMENTO.execute("SELECT CONTADOR FROM ANALISE_GRAFICA WHERE TABELA = 'ALIMENTO' AND ESTADO = 'alimento moderado' ORDER BY REFERENCIA ASC")
contALIMENTO = curALIMENTO.fetchall()
plt.plot(contALIMENTO , c='r', ls = '-', lw='1', marker='o', label ='Alimento')
#HUMOR
curHUMOR = con.cursor()
curHUMOR.execute("SELECT CONTADOR FROM ANALISE_GRAFICA WHERE TABELA = 'HUMOR' AND ESTADO = 'humor moderado' ORDER BY REFERENCIA ASC")
contHUMOR = curHUMOR.fetchall()
plt.plot(contHUMOR, c='g',ls ='-', lw='1', marker='^', fillstyle='right', label='Humor')
#SONO
curSONO = con.cursor()
curSONO.execute("SELECT CONTADOR FROM ANALISE_GRAFICA WHERE TABELA = 'SONO' AND ESTADO = 'sono moderado' ORDER BY REFERENCIA ASC")
contSONO = curSONO.fetchall()
plt.plot(contSONO, c='b', ls = '-', lw='1', marker='s', label='Sono')
#print (x)

#EIXO Y
curY = con.cursor()
curY.execute("SELECT DISTINCT extract(day from REFERENCIA) ||'/'|| extract(month from REFERENCIA) ||'/'|| extract(year from REFERENCIA) as DATAS FROM ANALISE_GRAFICA ORDER BY REFERENCIA ASC")
contY = curY.fetchall()

#CONT Y
curY2 = con.cursor()
curY2.execute("SELECT ROW_NUMBER() OVER(ORDER BY REFERENCIA) FROM ( SELECT DISTINCT REFERENCIA FROM ANALISE_GRAFICA) TB1 ORDER BY REFERENCIA ASC")
contY2 = curY2.fetchall()


y = contY
plt.xticks(x, y)


#Grafico3
plt.subplot(gs[2, :])
plt.title('Estado Ruim', color = 'black', fontweight= 'bold', fontsize=12)
#plt.xlabel('Eixo X', fontsize=16)
#plt.ylabel('Eixo Y', fontsize=16)


#ALIMENTO
curALIMENTO = con.cursor()
curALIMENTO.execute("SELECT CONTADOR FROM ANALISE_GRAFICA WHERE TABELA = 'ALIMENTO' AND ESTADO = 'alimento ruim' ORDER BY REFERENCIA ASC")
contALIMENTO = curALIMENTO.fetchall()
plt.plot(contALIMENTO , c='r', ls = '-', lw='1', marker='o', label ='Alimento')
#HUMOR
curHUMOR = con.cursor()
curHUMOR.execute("SELECT CONTADOR FROM ANALISE_GRAFICA WHERE TABELA = 'HUMOR' AND ESTADO = 'humor ruim' ORDER BY REFERENCIA ASC")
contHUMOR = curHUMOR.fetchall()
plt.plot(contHUMOR, c='g',ls ='-', lw='1', marker='^', fillstyle='right', label='Humor')
#SONO
curSONO = con.cursor()
curSONO.execute("SELECT CONTADOR FROM ANALISE_GRAFICA WHERE TABELA = 'SONO' AND ESTADO = 'sono ruim' ORDER BY REFERENCIA ASC")
contSONO = curSONO.fetchall()
plt.plot(contSONO, c='b', ls = '-', lw='1', marker='s', label='Sono')
#print (x)

#EIXO Y
curY = con.cursor()
curY.execute("SELECT DISTINCT extract(day from REFERENCIA) ||'/'|| extract(month from REFERENCIA) ||'/'|| extract(year from REFERENCIA) as DATAS FROM ANALISE_GRAFICA ORDER BY REFERENCIA ASC")
contY = curY.fetchall()

#CONT Y
curY2 = con.cursor()
curY2.execute("SELECT ROW_NUMBER() OVER(ORDER BY REFERENCIA) FROM ( SELECT DISTINCT REFERENCIA FROM ANALISE_GRAFICA) TB1 ORDER BY REFERENCIA ASC")
contY2 = curY2.fetchall()


y = contY
plt.xticks(x, y)

plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)

'''mng = plt.get_current_fig_manager()
mng.resize(1920, 1080)'''
plt.legend(["Alimento","Humor", "Sono"], 
           bbox_to_anchor = (-0.04, 3.743)) 
plt.show()
