import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib as mpl
import datetime
import pandas

pathTabela = 'C:/Users/Max Ziller/OneDrive/Documents/TCC Glória/indicadores_trajetoria_educacao_superior_2010_2019.csv'

registros = []

def leLinha(line):
    linha = line.strip()
    linha = linha.split(";")
    return linha


def fazDecimal(numero):
    n = numero.replace(",",".")
    if (n!=''):
        return float(n)
    else:
        return None

def fazInteiro(numero):
    try:
        n = int(numero)
    except:
        n = 0
    return n

def medialista(lista):
    i = 0
    for item in lista:
        i += item
    res = float(i)/len(lista)
    return res

def tadaporano(lista):

    anos = dict()
    medias = []
    datas = []
    
    publica = (1,2,3)
    for item in lista:
        if ( (item.TP_CATEGORIA_ADMINISTRATIVA != None and item.TP_CATEGORIA_ADMINISTRATIVA != '' and item.TADA != None and item.TADA != '' and item.ANO_REFERENCIA != None and item.ANO_REFERENCIA != '' and item.QT_INGRESSANTE > 0) and (int(item.TP_CATEGORIA_ADMINISTRATIVA) not in publica)):
            if item.ANO_REFERENCIA not in anos.keys():
                anos[item.ANO_REFERENCIA] = []
            anos[item.ANO_REFERENCIA].append(item.TADA)

    for k in anos.keys():
        datas.append(k)
        medias.append(medialista(anos[k]))
        
    plt.plot(datas,medias, c = "blue")
    plt.title("Média da TADA das Universidades Privadas por ano")
    plt.show()


def tcanporano(lista):

    anos = dict()
    medias = []
    datas = []
    
    publica = (1,2,3)
    for item in lista:
        if ( (item.TP_CATEGORIA_ADMINISTRATIVA != None and item.TP_CATEGORIA_ADMINISTRATIVA != '' and item.TCAN != None and item.TCAN != '' and item.ANO_REFERENCIA != None and item.ANO_REFERENCIA != '' and item.QT_INGRESSANTE > 0) and (int(item.TP_CATEGORIA_ADMINISTRATIVA) in publica)):
            if item.ANO_REFERENCIA not in anos.keys():
                anos[item.ANO_REFERENCIA] = []
            anos[item.ANO_REFERENCIA].append(item.TCAN)

    for k in anos.keys():
        datas.append(k)
        medias.append(medialista(anos[k]))
        
    plt.plot(datas,medias, c = "red")
    plt.title("Média da TCAN das Universidades Públicas por ano")
    plt.show()

class Curso:
    def __init__(self,CO_OCDE,No_OCDE,TAP,TCA,TDA,TCAN,TADA,QT_CONCLUINTE, QT_DESISTENCIA):
        self.CO_OCDE,self.No_OCDE,self.TAP,self.TCA,self.TDA,self.TCAN,self.TADA = CO_OCDE,No_OCDE,[],[],[],[],[]
        self.QT_CONCLUINTE, self.QT_DESISTENCIA = fazInteiro(QT_CONCLUINTE), fazInteiro(QT_DESISTENCIA)
        self.TAP.append(TAP)
        self.TCA.append(TCA)
        self.TDA.append(TDA)
        self.TCAN.append(TCAN)
        self.TADA.append(TADA)

    def addtaxas(self,TAP,TCA,TDA,TCAN,TADA,QT_CONCLUINTE, QT_DESISTENCIA):
        self.TAP.append(TAP)
        self.TCA.append(TCA)
        self.TDA.append(TDA)
        self.TCAN.append(TCAN)
        self.TADA.append(TADA)
        if (QT_CONCLUINTE != None):
            self.QT_CONCLUINTE += fazInteiro(QT_CONCLUINTE)
        if (QT_DESISTENCIA != None):
            self.QT_DESISTENCIA += fazInteiro(QT_DESISTENCIA)

    def imprimetotais(self):
        if (self.QT_DESISTENCIA > 0):
            razao = float(self.QT_CONCLUINTE)/self.QT_DESISTENCIA
            razao = "{:.2f}".format(razao)
        else:
            razao = "Não se aplica"
        print(self.No_OCDE + " & " + str(self.QT_CONCLUINTE) + " & " + str(self.QT_DESISTENCIA) + " & " + razao + "\\\\\\hline")
        


class Area:
    def __init__(self,CO_OCDE_AREA_GERAL,NO_OCDE_AREA_GERAL,TAP,TCA,TDA,TCAN,TADA,QT_CONCLUINTE, QT_DESISTENCIA):
        self.CO_OCDE_AREA_GERAL,self.NO_OCDE_AREA_GERAL,self.TAP,self.TCA,self.TDA,self.TCAN,self.TADA = CO_OCDE_AREA_GERAL,NO_OCDE_AREA_GERAL,[],[],[],[],[]
        self.TAP.append(TAP)
        self.TCA.append(TCA)
        self.TDA.append(TDA)
        self.TCAN.append(TCAN)
        self.TADA.append(TADA)
        self.QT_CONCLUINTE, self.QT_DESISTENCIA = fazInteiro(QT_CONCLUINTE), fazInteiro(QT_DESISTENCIA)

    def addtaxas(self,TAP,TCA,TDA,TCAN,TADA,QT_CONCLUINTE, QT_DESISTENCIA):
        self.TAP.append(TAP)
        self.TCA.append(TCA)
        self.TDA.append(TDA)
        self.TCAN.append(TCAN)
        self.TADA.append(TADA)
        if (QT_CONCLUINTE != None):
            self.QT_CONCLUINTE += fazInteiro(QT_CONCLUINTE)
        if (QT_DESISTENCIA != None):
            self.QT_DESISTENCIA += fazInteiro(QT_DESISTENCIA)

    def imprimetotais(self):
        if (self.QT_DESISTENCIA > 0):
            razao = float(self.QT_CONCLUINTE)/self.QT_DESISTENCIA
            razao = "{:.2f}".format(razao)
        else:
            razao = "Não se aplica"
        print(self.NO_OCDE_AREA_GERAL + " & " + str(self.QT_CONCLUINTE) + " & " + str(self.QT_DESISTENCIA) + " & " + razao + "\\\\\\hline")

class UF:
    def __init__(self,CO_UF,TAP,TCA,TDA,TCAN,TADA,QT_CONCLUINTE, QT_DESISTENCIA):
        self.CO_UF,self.TAP,self.TCA,self.TDA,self.TCAN,self.TADA = CO_UF,[],[],[],[],[]
        self.TAP.append(TAP)
        self.TCA.append(TCA)
        self.TDA.append(TDA)
        self.TCAN.append(TCAN)
        self.TADA.append(TADA)
        self.QT_CONCLUINTE, self.QT_DESISTENCIA = fazInteiro(QT_CONCLUINTE), fazInteiro(QT_DESISTENCIA)

    def addtaxas(self,TAP,TCA,TDA,TCAN,TADA,QT_CONCLUINTE, QT_DESISTENCIA):
        self.TAP.append(TAP)
        self.TCA.append(TCA)
        self.TDA.append(TDA)
        self.TCAN.append(TCAN)
        self.TADA.append(TADA)
        if (QT_CONCLUINTE != None):
            self.QT_CONCLUINTE += fazInteiro(QT_CONCLUINTE)
        if (QT_DESISTENCIA != None):
            self.QT_DESISTENCIA += fazInteiro(QT_DESISTENCIA)

    def imprimetotais(self):
        if (self.QT_DESISTENCIA > 0):
            razao = float(self.QT_CONCLUINTE)/self.QT_DESISTENCIA
            razao = "{:.2f}".format(razao)
        else:
            razao = "Não se aplica"
        print(self.CO_UF + " & " + str(self.QT_CONCLUINTE) + " & " + str(self.QT_DESISTENCIA) + " & " + razao + "\\\\\\hline")

class CatAdm:
    def __init__(self,TP_CATEGORIA_ADMINISTRATIVA,TAP,TCA,TDA,TCAN,TADA,QT_CONCLUINTE, QT_DESISTENCIA):
        self.TP_CATEGORIA_ADMINISTRATIVA,self.TAP,self.TCA,self.TDA,self.TCAN,self.TADA = TP_CATEGORIA_ADMINISTRATIVA,[],[],[],[],[]
        self.TAP.append(TAP)
        self.TCA.append(TCA)
        self.TDA.append(TDA)
        self.TCAN.append(TCAN)
        self.TADA.append(TADA)
        self.QT_CONCLUINTE, self.QT_DESISTENCIA = fazInteiro(QT_CONCLUINTE), fazInteiro(QT_DESISTENCIA)

    def addtaxas(self,TAP,TCA,TDA,TCAN,TADA,QT_CONCLUINTE, QT_DESISTENCIA):
        self.TAP.append(TAP)
        self.TCA.append(TCA)
        self.TDA.append(TDA)
        self.TCAN.append(TCAN)
        self.TADA.append(TADA)
        if (QT_CONCLUINTE != None):
            self.QT_CONCLUINTE += fazInteiro(QT_CONCLUINTE)
        if (QT_DESISTENCIA != None):
            self.QT_DESISTENCIA += fazInteiro(QT_DESISTENCIA)

    def imprimetotais(self):
        if (self.QT_DESISTENCIA != None and self.QT_DESISTENCIA > 0):
            razao = float(self.QT_CONCLUINTE)/self.QT_DESISTENCIA
            razao = "{:.2f}".format(razao)
        else:
            razao = "Não se aplica"
        print(self.TP_CATEGORIA_ADMINISTRATIVA + " & " + str(self.QT_CONCLUINTE) + " & " + str(self.QT_DESISTENCIA) + " & " + razao + "\\\\\\hline")
        

class Registro:
    def __init__(self,CO_IES, NO_IES, TP_CATEGORIA_ADMINISTRATIVA, TP_ORGANIZACAO_ACADEMICA, CO_CURSO, NO_CURSO, CO_REGIAO, CO_UF, CO_MUNICIPIO, TP_GRAU_ACADEMICO, TP_MODALIDADE_ENSINO, CO_CINE_ROTULO, NO_CINE_ROTULO, CO_CINE_AREA_GERAL, NO_CINE_AREA_GERAL, NU_ANO_INGRESSO, NU_ANO_REFERENCIA, NU_PRAZO_INTEGRALIZACAO, NU_ANO_INTEGRALIZACAO, NU_PRAZO_ACOMPANHAMENTO, NU_ANO_MAXIMO_ACOMPANHAMENTO, QT_INGRESSANTE, QT_PERMANENCIA, QT_CONCLUINTE, QT_DESISTENCIA, QT_FALECIDO, TAP, TCA, TDA, TCAN, TADA):
        self.CO_IES, self.NO_IES, self.TP_CATEGORIA_ADMINISTRATIVA, self.TP_ORGANIZACAO_ACADEMICA, self.CO_CURSO, self.NO_CURSO, self.CO_REGIAO, self.CO_UF, self.CO_MUNICIPIO, self.TP_GRAU_ACADEMICO, self.TP_MODALIDADE_ENSINO, self.CO_CINE_ROTULO, self.NO_CINE_ROTULO, self.CO_CINE_AREA_GERAL, self.NO_CINE_AREA_GERAL, self.ANO_INGRESSO, self.ANO_REFERENCIA, self.PRAZO_INTEGRALIZACAO, self.ANO_INTEGRALIZACAO, self.PRAZO_ACOMPANHAMENTO, self.ANO_MAXIMO_ACOMPANHAMENTO, self.QT_INGRESSANTE, self.QT_PERMANENCIA, self.QT_CONCLUINTE, self.QT_DESISTENCIA, self.QT_FALECIDO, self.TAP, self.TCA, self.TDA, self.TCAN, self.TADA  = CO_IES, NO_IES, TP_CATEGORIA_ADMINISTRATIVA, TP_ORGANIZACAO_ACADEMICA, CO_CURSO, NO_CURSO, CO_REGIAO, CO_UF, CO_MUNICIPIO, TP_GRAU_ACADEMICO, TP_MODALIDADE_ENSINO, CO_CINE_ROTULO, NO_CINE_ROTULO, CO_CINE_AREA_GERAL, NO_CINE_AREA_GERAL, NU_ANO_INGRESSO, NU_ANO_REFERENCIA, NU_PRAZO_INTEGRALIZACAO, NU_ANO_INTEGRALIZACAO, NU_PRAZO_ACOMPANHAMENTO, NU_ANO_MAXIMO_ACOMPANHAMENTO, QT_INGRESSANTE, QT_PERMANENCIA, QT_CONCLUINTE, QT_DESISTENCIA, QT_FALECIDO, TAP, TCA, TDA, TCAN, TADA
        self.ANO_INGRESSO = fazInteiro(self.ANO_INGRESSO)
        self.ANO_REFERENCIA = fazInteiro(self.ANO_REFERENCIA)
        self.PRAZO_INTEGRALIZACAO = fazInteiro(self.PRAZO_INTEGRALIZACAO)
        self.PRAZO_ACOMPANHAMENTO = fazInteiro(self.PRAZO_ACOMPANHAMENTO)
        self.ANO_INTEGRALIZACAO = fazInteiro(self.ANO_INTEGRALIZACAO)
        self.ANO_MAXIMO_ACOMPANHAMENTO = fazInteiro(self.ANO_MAXIMO_ACOMPANHAMENTO)
        self.QT_INGRESSANTE = fazInteiro(self.QT_INGRESSANTE)
        self.QT_PERMANENCIA = fazInteiro(self.QT_PERMANENCIA)
        self.QT_CONCLUINETE = fazInteiro(self.QT_CONCLUINTE)
        self.QT_DESISTENCIA = fazInteiro(self.QT_DESISTENCIA)
        self.QT_FALECIDO = fazInteiro(self.QT_FALECIDO)
        self.TAP = fazDecimal(self.TAP)
        self.TCA = fazDecimal(self.TCA)
        self.TDA = fazDecimal(self.TDA)
        #self.TMS = float(self.TMS)
        self.TCAN = fazDecimal(self.TCAN)
        self.TADA = fazDecimal(self.TADA)
        #self.TMC = int(self.TMC)
        #self.TEF = int(self.TEF)
        #self.TAS = int(self.TAS)

linhas = []
cursos = dict()
areas = dict()
ufs = dict()
catadms = dict()
items = []
i = 0
with open(pathTabela, 'r') as f:
    for line in f:
        linha = leLinha(line)
        if (i < 8):
            i += 1
        elif( i < 9):
            titulos = linha
            i += 1
        else:
            novo = Registro(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7],linha[8],linha[9],linha[10],linha[11],linha[12],linha[13],linha[14],linha[15],linha[16],linha[17],linha[18],linha[19],linha[20],linha[21],linha[22],linha[23],linha[24],linha[25],linha[26],linha[27],linha[28],linha[29],linha[30])
            items.append(novo)
            if novo.CO_UF not in ufs.keys():
                ufs[novo.CO_UF] = UF(novo.CO_UF,novo.TAP,novo.TCA,novo.TDA,novo.TCAN,novo.TADA,novo.QT_CONCLUINTE, novo.QT_DESISTENCIA)
            else:
                ufs[novo.CO_UF].addtaxas(novo.TAP,novo.TCA,novo.TDA,novo.TCAN,novo.TADA,novo.QT_CONCLUINTE, novo.QT_DESISTENCIA)
            if novo.CO_CINE_ROTULO not in cursos.keys():
                cursos[novo.CO_CINE_ROTULO] = Curso(novo.CO_CINE_ROTULO,novo.NO_CINE_ROTULO,novo.TAP,novo.TCA,novo.TDA,novo.TCAN,novo.TADA,novo.QT_CONCLUINTE, novo.QT_DESISTENCIA)
            else:
                cursos[novo.CO_CINE_ROTULO].addtaxas(novo.TAP,novo.TCA,novo.TDA,novo.TCAN,novo.TADA,novo.QT_CONCLUINTE, novo.QT_DESISTENCIA)
            if novo.CO_CINE_AREA_GERAL not in areas.keys():
                areas[novo.CO_CINE_AREA_GERAL] = Area(novo.CO_CINE_AREA_GERAL,novo.NO_CINE_AREA_GERAL,novo.TAP,novo.TCA,novo.TDA,novo.TCAN,novo.TADA,novo.QT_CONCLUINTE, novo.QT_DESISTENCIA)
            else:
                areas[novo.CO_CINE_AREA_GERAL].addtaxas(novo.TAP,novo.TCA,novo.TDA,novo.TCAN,novo.TADA,novo.QT_CONCLUINTE, novo.QT_DESISTENCIA)
            if novo.TP_CATEGORIA_ADMINISTRATIVA not in catadms.keys():
                catadms[novo.TP_CATEGORIA_ADMINISTRATIVA] = CatAdm(novo.TP_CATEGORIA_ADMINISTRATIVA,novo.TAP,novo.TCA,novo.TDA,novo.TCAN,novo.TADA,novo.QT_CONCLUINTE, novo.QT_DESISTENCIA)
            else:
                catadms[novo.TP_CATEGORIA_ADMINISTRATIVA].addtaxas(novo.TAP,novo.TCA,novo.TDA,novo.TCAN,novo.TADA,novo.QT_CONCLUINTE, novo.QT_DESISTENCIA)


#for c in catadms.keys():
#    catadms[c].imprimetotais()

tcanporano(items)



