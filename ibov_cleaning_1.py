import pandas as pd
import numpy as np

ibov_excel_path = ('/Users/antonioelias/Desktop/Insper - Modules/Insper Q3/Finance 1 - Investments/Aplicacao_1/Ibovespa_Consolidado.xlsx')
df_main = pd.read_excel(ibov_excel_path)
print(df_main.head())