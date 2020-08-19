import PyPDF2 as p2
import re
import numpy as np
import pandas as pd
file = open("limpo.pdf", "rb") #abre pdf lendo binários
pdf = p2.PdfFileReader(file) #lê o pdf
fim = pdf.getNumPages() # define um intero que será usado nos loops, é o tamanho do pdf
c = 0 # variável pra contagem, mas não sei se foi usada... acho que não!
div = [] # Essas listas foram criadas para poderem armazenar as informações provenientes dos loop's, deve ter um jeito melhor de fazer isso...
unif= []
unilist = []
'IS/FeO' # tá aí só prá gastá memoriá...
Samples = []
Maturidade = []
SiO2 = []
TiO2 = []
Sc = []
V = []
La = []
Ce = []
Al2O3 = []
Cr2O3 = []
FeO = []
MnO = []
MgO = []
CaO = []
Na2O = []
K2O = []
P2O5 = []
S = []
Co = []
Ni = []
Ba = []
Sr = []
Hf = []
Ta = []
Th = []
U = []
K = []
Nd = []
Sm = []
Eu = []
Tb = []
Dy = []
Ho = []
Tm = []
Yb = []
Lu = []
Zr = []
Ir = []
Au = []
O = []
Cr = []
Mn = []
for pg in range(0, fim):
    pagina = pdf.getPage(pg)              #"Vira" a página
    texto = pagina.extractText().split()  # Pega o texto da página e transforma em uma lista de listas onde cada palavra é uma sublista composta por uma sting  
    txt_un = ','.join(texto)              # pega essas sublistas e junta tudo numa lista
    unido = list(txt_un.replace(',', '')) # pega as strings dentro dessa lista e transforma num stringão dentro de um listão
    c += 1
    div.insert(pg, unido)                 #monta uma lista disso pra cada página
x = list(div)                             #lista aux que não tá funcionando como eu queria (era pra fazer cópias não vinculadas da lista mas não sei pq não tá roalando)
y = list(x)                               #lista aux que não tá funcionando como eu queria (era pra fazer cópias não vinculadas da lista mas não sei pq não tá roalando
for p, v in enumerate(x):                 #loop dentro do stringão de cada página
    ant = p-1                             # essa variável faz o loop "olhar pra trás"
    if x[p][0] == "M":
        y[ant].extend(v)                  # condição q faz com que o loop cole as páginas que começam com M com a página anterior (olhar pdf "limpo" pra entender)
div = [a for a in div if a[:][0] != "M"]  # slice q deleta as páginas que começam com "M" pq agora elas estão sobrando
for i in range(0, len(div)):               #Esse loop varre cada uns dos stringão, daqui pra frente tudo é slice de string
    str = ''.join(div[i])
    unilist.insert(i, str)
    sample = unilist[i][5:10]                                                  """Cada atributo tinha suas especificidades, então foram fatiados de acordo #pas"""
    Samples.insert(i, sample)
    #print(sample, unilist[i][:].upper().index("FEO"))
    idivmat = unilist[i][:].upper().index("FEO") - 2
    idfvmat = unilist[i][:].upper().index("FEO") + 8
    maturidade = re.sub('[a-zA-Z /(,:]', "", unilist[i][idivmat:idfvmat])
    if maturidade == "9.2.":
        maturidade = "9.2"
    if maturidade == "" or maturidade == "2.":
        maturidade = np.NaN
    Maturidade.insert(i, maturidade)
    i_sio2 = unilist[i][:].index("ppm")
    f_sio2 = unilist[i][:].index("Sc")
    sio2 = re.sub('[a-zA-Z /(,:]', "", unilist[i][i_sio2:f_sio2].replace('SiO2', ""))
    if sio2 == "":
        sio2 = np.NaN
    SiO2.insert(i, sio2)
    i_tio2 = unilist[i][:].index("TiO2", unilist[i][:].index("SiO2"))
    f_tio2 = unilist[i][:].index("V", unilist[i][:].index("SiO2"))
    tio2 = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_tio2:f_tio2])
    if tio2 == "":
        tio2 = np.NaN
    if tio2[0] == "2":
        tio2 = tio2[1:]
    TiO2.insert(i, tio2)
    i_al2o3 = unilist[i][:].index('Al2')
    f_al2o3 = unilist[i][:].index('Al2')+10
    al2o3 = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_al2o3:f_al2o3].replace("Al2O3", "").replace("203", ""))
    if al2o3 == "":
        al2o3 = np.NaN
    Al2O3.insert(i, al2o3)
    i_cr2o3 = unilist[i][:].index("Cr2")
    f_cr2o3 = unilist[i][:].index("Cr2")+9
    cr2o3 = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_cr2o3:f_cr2o3].replace("Cr2O3", "").replace("203", ""))
    if cr2o3 == "":
        cr2o3 = np.NaN
    Cr2O3.insert(i, cr2o3)
    i_feo = unilist[i][:].index("FeO", unilist[i][:].index("Cr2"))
    f_feo = unilist[i][:].index("FeO", unilist[i][:].index("Cr2")) + 8
    feo = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_feo:f_feo].replace("Feo", ""))
    if feo == "":
        feo = np.NaN
    FeO.insert(i, feo)
    i_mno = unilist[i].index("MnO")
    f_mno = unilist[i].index("MnO")+7
    mno = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_mno:f_mno].replace("MnO", ""))
    if mno == "":
        mno = np.NaN
    MnO.insert(i, mno)
    i_mgo = unilist[i].index("MgO")
    f_mgo = unilist[i].index("MgO") + 8
    mgo = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_mgo:f_mgo].replace("MgO", ""))
    if mgo == "":
        mgo = np.NaN
    MgO.insert(i, mgo)
    i_cao = unilist[i].index("CaO")
    f_cao = unilist[i].index("CaO") + 8
    cao = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_cao:f_cao].replace("CaO", ""))
    if cao == "":
        cao = np.NaN
    CaO.insert(i, cao)
    i_na2o = unilist[i].index("Na2")
    f_na2o = unilist[i].index("Na2") + 8
    na2o = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_na2o:f_na2o].replace("Na2", ""))
    if na2o == "":
        na2o = np.NaN
    Na2O.insert(i, na2o)
    if "K2O" in unilist[i][:]:
        i_k2o = unilist[i][:].index("K2O", unilist[i][:].index("SiO2"))
        f_k2o = unilist[i][:].index("U", unilist[i][:].index("SiO2"))
        k2o = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_k2o:f_k2o])
        if k2o == "":
            k2o = np.NaN
        if k2o[0] == "2":
            k2o = k2o[1:]
    else:
        k2o = np.NaN
    K2O.insert(i, k2o)
    i_p2o = unilist[i].index("P2")+4
    f_p2o = unilist[i].index("P2")+9
    p2o = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_p2o:f_p2o].replace("P2", ""))
    if p2o == "":
        p2o = np.NaN
    P2O5.insert(i, p2o)
    i_s = unilist[i][:].index("S", unilist[i][:].index("P2"))
    f_s = unilist[i][:].index("S", unilist[i][:].index("P2")) + 5
    s = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_s:f_s])
    if s == "" or s == "8" or s == "1":
        s = np.NaN
    S.insert(i, s)
    i_sc = unilist[i][:].index("Sc", unilist[i][:].index("SiO2"))
    f_sc = unilist[i][:].index("La", unilist[i][:].index("SiO2"))
    sc = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_sc:f_sc])
    if sc == "":
        sc = np.NaN
    Sc.insert(i, sc)
    i_v = unilist[i][:].index("V", unilist[i][:].index("SiO2"))
    f_v = unilist[i][:].index("Ce", unilist[i][:].index("SiO2"))
    v = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_v:f_v])
    if v == "":
        v = np.NaN
    V.insert(i, v)
    i_co = unilist[i][:].index("Co", unilist[i][:].index("SiO2"))
    f_co = unilist[i][:].index("Nd", unilist[i][:].index("SiO2"))
    co = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_co:f_co])
    if co == "":
        co = np.NaN
    Co.insert(i, co)
    i_ni = unilist[i][:].index("Ni", unilist[i][:].index("SiO2"))
    f_ni = unilist[i][:].index("Sm", unilist[i][:].index("SiO2"))
    ni = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_ni:f_ni])
    if ni == "":
        ni = np.NaN
    Ni.insert(i, ni)
    i_ba = unilist[i][:].index("Ba", unilist[i][:].index("SiO2"))
    f_ba = unilist[i][:].index("Eu", unilist[i][:].index("SiO2"))
    ba = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_ba:f_ba])
    if ba == "":
        ba = np.NaN
    Ba.insert(i, ba)
    i_sr = unilist[i][:].index("Sr", unilist[i][:].index("SiO2"))
    f_sr = unilist[i][:].index("Tb", unilist[i][:].index("SiO2"))
    sr = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_sr:f_sr])
    if sr == "":
        sr = np.NaN
    Sr.insert(i, sr)
    i_hf = unilist[i][:].index("Hf", unilist[i][:].index("SiO2"))
    f_hf = unilist[i][:].index("Dy", unilist[i][:].index("SiO2"))
    hf = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_hf:f_hf])
    if hf == "":
        hf = np.NaN
    Hf.insert(i, hf)
    i_ta = unilist[i][:].index("Ta", unilist[i][:].index("SiO2"))
    f_ta = unilist[i][:].index("Ho", unilist[i][:].index("SiO2"))
    ta = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_ta:f_ta])
    if ta == "":
        ta = np.NaN
    Ta.insert(i, ta)
    i_th = unilist[i][:].index("Th", unilist[i][:].index("SiO2"))
    f_th = unilist[i][:].index("Tm", unilist[i][:].index("SiO2"))
    th = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_th:f_th])
    if th == "":
        th = np.NaN
    Th.insert(i, th)
    i_u = unilist[i][:].index("U", unilist[i][:].index("SiO2"))
    f_u = unilist[i][:].index("Yb", unilist[i][:].index("SiO2"))
    u = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_u:f_u])
    if u == "":
        u = np.NaN
    U.insert(i, u)
    if "Zr" in unilist[i][:]:
        i_zr = unilist[i][:].index("Zr", unilist[i][:].index("SiO2"))
        f_zr = unilist[i][:].index("Lu", unilist[i][:].index("SiO2"))
        zr = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_zr:f_zr])
        if zr == "":
            zr = np.NaN
    else:
        zr = np.nan
    Zr.insert(i, zr)
    if "Ir" in unilist[i][:] and "Au" in unilist[i][:]:
        i_ir = unilist[i][:].index("Ir", unilist[i][:].index("SiO2"))
        f_ir = unilist[i][:].index("Au", unilist[i][:].index("SiO2"))
        ir = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_ir:f_ir])
        if ir == "":
            ir = np.NaN
    else:
        ir = np.NaN
    Ir.insert(i, ir)
    i_la = unilist[i][:].index("La", unilist[i][:].index("SiO2"))
    f_la = unilist[i][:].index("Ti", unilist[i][:].index("SiO2"))
    la = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_la:f_la])
    if la == "":
        la = np.NaN
    La.insert(i, la)
    i_ce = unilist[i][:].index("Ce", unilist[i][:].index("SiO2"))
    f_ce = unilist[i][:].index("Al2", unilist[i][:].index("SiO2"))
    ce = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_ce:f_ce])
    if ce == "":
        ce = np.NaN
    Ce.insert(i, ce)
    i_nd = unilist[i][:].index("Nd", unilist[i][:].index("SiO2"))
    f_nd = unilist[i][:].index("Cr2", unilist[i][:].index("SiO2"))
    nd = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_nd:f_nd])
    if nd == "":
        nd = np.NaN
    Nd.insert(i, nd)
    i_sm = unilist[i][:].index("Sm", unilist[i][:].index("SiO2"))
    f_sm = unilist[i][:].index("FeO", unilist[i][:].index("SiO2"))
    sm = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_sm:f_sm])
    if sm == "":
        sm = np.NaN
    Sm.insert(i, sm)
    i_eu = unilist[i][:].index("Eu", unilist[i][:].index("SiO2"))
    f_eu = unilist[i][:].index("Mn", unilist[i][:].index("SiO2"))
    eu = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_eu:f_eu])
    if eu == "":
        eu = np.NaN
    Eu.insert(i, eu)
    i_tb = unilist[i][:].index("Tb", unilist[i][:].index("SiO2"))
    f_tb = unilist[i][:].index("Mg", unilist[i][:].index("SiO2"))
    tb = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_tb:f_tb])
    if tb == "":
        tb = np.NaN
    Tb.insert(i, tb)
    i_dy = unilist[i][:].index("Dy", unilist[i][:].index("SiO2"))
    f_dy = unilist[i][:].index("Ca", unilist[i][:].index("SiO2"))
    dy = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_dy:f_dy])
    if dy == "":
        dy = np.NaN
    Dy.insert(i, dy)
    i_ho = unilist[i][:].index("Ho", unilist[i][:].index("SiO2"))
    f_ho = unilist[i][:].index("Na2", unilist[i][:].index("SiO2"))
    ho = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_ho:f_ho])
    if ho == "":
        ho = np.NaN
    Ho.insert(i, ho)
    i_yb = unilist[i][:].index("Yb", unilist[i][:].index("SiO2"))
    f_yb = unilist[i][:].index("P2", unilist[i][:].index("SiO2"))
    yb = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_yb:f_yb])
    if yb == "":
        yb = np.NaN
    Yb.insert(i, yb)
    i_lu = unilist[i][:].index("Lu", unilist[i][:].index("P2"))
    f_lu = unilist[i][:].index("S", unilist[i][:].index("P2"))
    lu = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_lu:f_lu])
    if lu == "":
        lu = np.NaN
    Lu.insert(i, lu)
    if "K2O" in unilist[i][:]:
        i_tm = unilist[i][:].index("Tm", unilist[i][:].index("SiO2"))
        f_tm = unilist[i][:].index("K2", unilist[i][:].index("SiO2"))
        tm = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_tm:f_tm])
        if tm == "":
            tm = np.NaN
    else:
        tm = np.NaN
    Tm.insert(i, tm)
    if "Au" in unilist[i][unilist[i][:].index("SiO2", unilist[i][:].index("SiO2")):]:
        i_au = unilist[i][:].index("Au", unilist[i][:].index("SiO2"))
        f_au = unilist[i][:].index("Au", unilist[i][:].index("SiO2")+3)
        au = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_au:f_au])
        if au == "":
            au = np.NaN
    else:
        au = np.NaN
    Au.insert(i, au)
    if "O" in unilist[i][unilist[i][:].index("Lu", unilist[i][:].index("SiO2")):]:
        i_o = unilist[i][:].index("O", unilist[i][:].index("Lu"))
        f_o = unilist[i][:].index("O", unilist[i][:].index("Lu")) + 5
        o = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_o:f_o])
        if o == "":
            o = np.NaN
    else:
        o = np.NaN
    O.insert(i, o)
    if "Cr" in unilist[i][unilist[i][:].index("Th", unilist[i][:].index("SiO2")):]:
        i_cr = unilist[i][:].index("Cr", unilist[i][:].index("Th"))
        f_cr = unilist[i][:].index("Cr", unilist[i][:].index("Th")) + 5
        cr = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_cr:f_cr])
        if cr == "":
            cr = np.NaN
    else:
        cr = np.NaN
    Cr.insert(i, cr)
    if "Mn" in unilist[i][unilist[i][:].index("Th", unilist[i][:].index("SiO2")):]:
        i_mn = unilist[i][:].index("Mn", unilist[i][:].index("Th"))
        f_mn = unilist[i][:].index("Mn", unilist[i][:].index("Th")) + 5
        mn = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_mn:f_mn])
        if mn == "":
            mn = np.NaN
    else:
        mn = np.NaN
    Mn.insert(i, mn)
    if "K" in unilist[i][unilist[i][:].index("U", unilist[i][:].index("SiO2")):]:
        i_k = unilist[i][:].index("K", unilist[i][:].index("Yb"))
        f_k = unilist[i][:].index("Lu", unilist[i][:].index("Yb"))
        k = re.sub("[a-zA-Z /(,:+*<>\-]", "", unilist[i][i_k:f_k])
        if k == "":
            k = np.NaN
    else:
        k = np.NaN
    K.insert(i, k)
total = [Samples, Maturidade, SiO2, TiO2, Sc, V, La, Ce, Al2O3, Cr2O3, FeO, MnO, MgO, CaO, Na2O, K2O, P2O5, S, Co, Ni, Ba, Sr, Hf, Ta, Th, U, K, Nd, Sm, Eu, Tb, Dy, Ho, Tm, Yb, Lu, Zr, Ir, Au, O, Cr, Mn]
cru = pd.DataFrame.from_records(total, index=("Samples", "Maturidade", "SiO2", "TiO2", "Sc", "V", "La", "Ce", "Al2O3", "Cr2O3", "FeO", "MnO", "MgO", "CaO", "Na2O", "K2O", "P2O5", "S", "Co", "Ni", "Ba", "Sr", "Hf","Ta", "Th", "U", "K", "Nd", "Sm", "Eu", "Tb", "Dy", "Ho", "Tm", "Yb", "Lu", "Zr", "Ir", "Au", "O", "Cr", "Mn"))
pronto = cru.T
#print(cru)
print(pronto)
pronto.to_csv("bd_solos.csv")

