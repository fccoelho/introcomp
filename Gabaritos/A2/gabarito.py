"""
Gabarito da A2.
"""

import pandas as pd
import numpy as np
from pysus.preprocessing.decoders import decodifica_idade_SINAN
import matplotlib.pyplot as plt

SIGLAS = {11: 'RO',
          12: 'AC',
          13: 'AM',
          14: 'RR',
          15: 'PA',
          16: 'AP',
          17: 'TO',
          21: 'MA',
          22: 'PI',
          23: 'CE',
          24: 'RN',
          25: 'PB',
          26: 'PE',
          27: 'AL',
          28: 'SE',
          29: 'BA',
          31: 'MG',
          32: 'ES',
          33: 'RJ',
          35: 'SP',
          41: 'PR',
          42: 'SC',
          43: 'RS',
          50: 'MS',
          51: 'MT',
          52: 'GO',
          53: 'DF',
          'nan': 'outro'}

munestado = {11: 52,
             12: 22,
             13: 62,
             14: 15,
             15: 144,
             16: 16,
             17: 139,
             21: 217,
             22: 224,
             23: 184,
             24: 167,
             25: 223,
             26: 184,
             27: 102,
             28: 75,
             29: 417,
             31: 853,
             32: 78,
             33: 92,
             35: 645,
             41: 399,
             42: 295,
             43: 497,
             50: 79,
             51: 141,
             52: 246,
             53: 1}

munestados = pd.read_csv('Municípios por Estado.csv', sep=';')


def questao_1(df):
    return len(df)


def questao_2(df):
    return df.ID_MUNICIP.value_counts().to_dict()


def questao_3(df):
    return df.CS_SEXO.value_counts().sort_values().index[-1], df.groupby('CS_SEXO').count()['ID_MUNICIP'].to_dict()


def questao_4(df):
    try:
        df['idade'] = decodifica_idade_SINAN(df.NU_IDADE_N, 'Y')
    except ValueError:
        df['idade'] = decodifica_idade_SINAN(df.NU_IDADE_N.fillna(0), 'Y') # ignora os valores nulos
    return df.idade.mean()


def questao_5(df):
    df['siglas'] = [SIGLAS.get(int(np.nan_to_num(c)),'outro') for c in df.SG_UF_NOT]
    return df.siglas.value_counts().to_dict()


def questao_6(df):
    df['siglas'] = [SIGLAS.get(int(np.nan_to_num(c)),'outro') for c in df.SG_UF_NOT]
    g = df[df.CS_SEXO == 'M'].groupby('siglas').count()['TP_NOT'].to_dict()
    return g


def questao_7(df):
    resposta = {}
    for uf in df.SG_UF_NOT.unique():
        if uf == 'nan':
            continue
        resposta[uf] = (df[df.SG_UF_NOT == uf].ID_MUNICIP.value_counts() > 0).sum() / munestado[int(uf)]

    return resposta


def questao_8(df):
    try:
        df['DT_NOTIFICACAO'] = pd.to_datetime(df.DT_NOTIFIC, format='%Y%m%d')
        df['DT_SINTOMAS'] = pd.to_datetime(df.DT_SIN_PRI, format='%Y%m%d')
    except ValueError:
        df['DT_NOTIFICACAO'] = pd.to_datetime(df.DT_NOTIFIC.fillna(0), format='%Y-%m-%d')
        df['DT_SINTOMAS'] = pd.to_datetime(df.DT_SIN_PRI, format='%Y-%m-%d')
    df['ATRASO_NOT'] = (df.DT_NOTIFICACAO - df.DT_SINTOMAS).dt.days

    return df[['DT_NOTIFICACAO', 'DT_SINTOMAS', 'ATRASO_NOT']]


def questao_9(df):
    try:
        df['DT_NOTIFICACAO'] = pd.to_datetime(df.DT_NOTIFIC, format='%Y%m%d')
        df['DT_SINTOMAS'] = pd.to_datetime(df.DT_SIN_PRI, format='%Y%m%d')
    except ValueError:
        df['DT_NOTIFICACAO'] = pd.to_datetime(df.DT_NOTIFIC.fillna(0), format='%Y-%m-%d')
        df['DT_SINTOMAS'] = pd.to_datetime(df.DT_SIN_PRI, format='%Y-%m-%d')
    except AttributeError:
        df['DT_NOTIFICACAO'] = pd.to_datetime(df.DT_NOTIFICACAO.fillna(0), format='%Y-%m-%d')
        df['DT_SINTOMAS'] = pd.to_datetime(df.DT_SIN_PRI, format='%Y-%m-%d')
    df['ATRASO_NOT'] = (df.DT_NOTIFICACAO - df.DT_SINTOMAS).dt.days
    return {SIGLAS.get(int(c),'outro'): (df[df.SG_UF_NOT == c].ATRASO_NOT.mean(), df[df.SG_UF_NOT == c].ATRASO_NOT.std()) for c in
            df.SG_UF_NOT.unique()}


def questao_10(df):
    df['DT_NOTIFICACAO'] = pd.to_datetime(df.DT_NOTIFIC, format='%Y%m%d')
    df['DT_SINTOMAS'] = pd.to_datetime(df.DT_SIN_PRI, format='%Y%m%d')
    df['ATRASO_NOT'] = (df.DT_NOTIFICACAO - df.DT_SINTOMAS).dt.days

    atraso_médio = df.groupby('ID_MUNICIP').agg({'ATRASO_NOT': pd.np.mean})
    casos = df.ID_MUNICIP.value_counts()

    plt.plot(casos, atraso_médio, 'o')
    plt.xlabel('Casos')
    plt.ylabel('Atraso médio')
    # plt.show()
    return atraso_médio['ATRASO_NOT']



