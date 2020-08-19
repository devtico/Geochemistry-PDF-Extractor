""" Esse cara aqui cola as coordenadas nas amostras que possuem análises químicas"""
import pandas as pd
abra_solos = pd.read_csv("bd_solos.csv")
abra_localizacao_solos = pd.read_csv("loc_solos.csv", delimiter=';')
localizacao = pd.DataFrame(abra_localizacao_solos)
solos = pd.DataFrame(abra_solos)
solos = solos.drop(columns=['Unnamed: 0']) #deleta um cara que fiz sem querer
print(localizacao, solos)
#print(localizacao.loc[1, 'Sample'] == solos.loc[0, 'Samples']) # usei pra testar o conteúdo 
completo = solos.merge(localizacao, left_on="Samples", right_on="Sample").reindex(columns=["Samples", "x", "y", "Maturidade", "SiO2", "TiO2", "Sc", "V", "La", "Ce", "Al2O3", "Cr2O3", "FeO", "MnO", "MgO", "CaO", "Na2O", "K2O", "P2O5", "S", "Co", "Ni", "Ba", "Sr", "Hf","Ta", "Th", "U", "K", "Nd", "Sm", "Eu", "Tb", "Dy", "Ho", "Tm", "Yb", "Lu", "Zr", "Ir", "Au", "O", "Cr", "Mn"])
salva = completo.to_csv("completo.csv")





