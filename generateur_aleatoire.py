# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random as rd
import numpy as np

plt.style.use('_mpl-gallery')

seed = rd.randint(0, 1<<32)
lst_seed = [rd.randint(0, 1<<32) for k in range(10)]

#cette partie contient les différents génrateurs de nombres pseudo-aléatoires

def gen_spl(a, c, m):
    global seed
    seed = (seed*a+c)%m
    return seed/m

def gen_mlt(lsta, c, m):
    global lst_seed
    res = c
    for i in range(len(lsta)):
        res += (lsta[i]*lst_seed[i])
    lst_seed = [res%m]+lst_seed[1:]
    return lst_seed[0]/m

def gen_para(lsta, lstc, lstm):
    global lst_seed
    res = 0
    for k in range(len(lsta)):
        lst_seed[k] = (lst_seed[k]*lsta[k]+lstc[k])%lstm[k]
        res += lst_seed[k]/lstm[k]
    return res%1

def gen_para_explicite(lsta, lstc, lstm):
    global lst_seed
    for k in range(len(lsta)):
        lst_seed[k] = (lst_seed[k]*lsta[k]+lstc[k])%lstm[k]
    return tuple(lst_seed)


def gen_para_c(lsta, lstc, m, puiss):
    global seed
    res = 0
    n = len(lsta)
    pas = puiss//n
    for k in range(n):
        res += (int((seed>>k*pas)%(1<<pas))*lsta[k]+lstc[k])%(1<<pas)<<k*pas
    seed = res%m
    return seed/m

def gen_para_m(lsta, lstc, lstm):
    global lst_seed
    res = 0
    for k in range(len(lsta)):
        lst_seed[k] = (lst_seed[k]*lsta[k]+lstc[k])%lstm[k]
        res *= lst_seed[k]/lstm[k]
    return res

def gen_para_m_explicite(lsta, lstc, lstm):
    global lst_seed
    for k in range(len(lsta)):
        lst_seed[k] = (lst_seed[k]*lsta[k]+lstc[k])%lstm[k]
    return tuple(lst_seed)

#cette partie contient la fonction de test liée à chaque générateur

def test_rand(test, nbr_test) :
    success = 0
    for k in range(nbr_test) :
        f = lambda : rd.random()
        res = test(f)
        print("résultat : ", res, "\n")
        if res :
            success += 1
    print(success, " ont passé le test sur ", nbr_test, "\n")

def test_spl(test, nbr_test, puiss):
    success = 0
    for k in range(nbr_test):
        a = rd.randint(0, 1<<puiss)
        c = rd.randint(0, 1<<puiss)
        m = rd.randint(0, 1<<puiss)
        print("a = ", a, " ; c = ", c, " ; m = ", m)
        f = lambda : gen_spl(a, c, m)
        res = test(f)
        print("résultat : ", res, "\n")
        if res :
            success += 1
    print(success, " ont passé le test sur ", nbr_test, "\n")
        
def test_mlt(test, nbr_test, puiss, mult) :
    success = 0
    for k in range(nbr_test):
        lsta = [rd.randint(0, 1<<puiss) for i in range(mult)]
        c = rd.randint(0, 1<<puiss)
        m = rd.randint(0, 1<<puiss)
        print("a = ", lsta, " ; c = ", c, " ; m = ", m)
        f = lambda : gen_mlt(lsta, c, m)
        res = test(f)
        print("résultat : ", res, "\n")
        if res :
            success += 1
    print(success, " ont passé le test sur ", nbr_test, "\n")

def test_para(test, nbr_test, puiss, mult) :
    success = 0
    for k in range(nbr_test):
        lsta = [rd.randint(0, 1<<puiss) for i in range(mult)]
        lstc = [rd.randint(0, 1<<puiss) for i in range(mult)]
        lstm = [rd.randint(0, 1<<puiss) for i in range(mult)]
        print("a = ", lsta, " ; c = ", lstc, " ; m = ", lstm)
        f = lambda : gen_para(lsta, lstc, lstm)
        res = test(f)
        print("résultat : ", res, "\n")
        if res :
            success += 1
    print(success, " ont passé le test sur ", nbr_test, "\n")
    
def test_para_explicite(test, nbr_test, puiss, mult) :
    success = 0
    for k in range(nbr_test):
        lsta = [rd.randint(0, 1<<puiss) for i in range(mult)]
        lstc = [rd.randint(0, 1<<puiss) for i in range(mult)]
        lstm = [rd.randint(0, 1<<puiss) for i in range(mult)]
        print("a = ", lsta, " ; c = ", lstc, " ; m = ", lstm)
        f = lambda : gen_para_explicite(lsta, lstc, lstm)
        res = test(f)
        print("résultat : ", res, "\n")
        if res :
            success += 1
    print(success, " ont passé le test sur ", nbr_test, "\n")
    
def test_para_m(test, nbr_test, puiss, mult) :
    success = 0
    for k in range(nbr_test):
        lsta = [rd.randint(0, 1<<puiss) for i in range(mult)]
        lstc = [rd.randint(0, 1<<puiss) for i in range(mult)]
        lstm = [rd.randint(0, 1<<puiss) for i in range(mult)]
        print("a = ", lsta, " ; c = ", lstc, " ; m = ", lstm)
        f = lambda : gen_para_m(lsta, lstc, lstm)
        res = test(f)
        print("résultat : ", res, "\n")
        if res :
            success += 1
    print(success, " ont passé le test sur ", nbr_test, "\n")
    
def test_para_m_explicite(test, nbr_test, puiss, mult) :
    success = 0
    for k in range(nbr_test):
        lsta = [rd.randint(0, 1<<puiss) for i in range(mult)]
        lstc = [rd.randint(0, 1<<puiss) for i in range(mult)]
        lstm = [rd.randint(0, 1<<puiss) for i in range(mult)]
        print("a = ", lsta, " ; c = ", lstc, " ; m = ", lstm)
        f = lambda : gen_para_m_explicite(lsta, lstc, lstm)
        res = test(f)
        print("résultat : ", res, "\n")
        if res :
            success += 1
    print(success, " ont passé le test sur ", nbr_test, "\n")
    
def test_para_c(test, nbr_test, puiss, mult) :
    success = 0
    pas = 1<<puiss//mult
    for k in range(nbr_test):
        lsta = [rd.randint(0, pas) for i in range(mult)]
        lstc = [rd.randint(0, pas) for i in range(mult)]
        m = rd.randint(0, 1<<puiss)
        print("a = ", lsta, " ; c = ", lstc, " ; m = ", m)
        f = lambda : gen_para_c(lsta, lstc, m, puiss)
        res = test(f)
        print("résultat : ", res, "\n")
        if res :
            success += 1
    print(success, " ont passé le test sur ", nbr_test, "\n")
 
#cette partie contient les différents tests

def test_graphique(f, nb_pt, zoom, taille_pt, taille_fig):
    fig, ax = plt.subplots(figsize = (taille_fig, taille_fig))
    lstx = []
    lsty = []
    pre = f()
    for i in range(nb_pt):
        act = f()
        if pre < 1>>zoom & act < 1>>zoom :
            lstx.append(pre)
            lsty.append(act)
        pre = act
    ax.scatter(lstx, lsty, marker = 'o', color = 'blue', s = taille_pt)
    ax.set_xlim([0, 1>>zoom])
    ax.set_ylim([0, 1>>zoom])

def test_graphique_3d(f, nb_pt, zoom, taille_pt, taille_fig):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize = (taille_fig, taille_fig))
    lstx = []
    lsty = []
    lstz = []
    prepre = f()
    pre = ()
    for i in range(nb_pt):
        act = f()
        if prepre < 1>>zoom & pre < 1>>zoom & act < 1>>zoom :
            lstx.append(prepre)
            lsty.append(pre)
            lstz.append(act)
        prepre = pre
        pre = act
    ax.scatter(lstx, lsty, lstz, marker = 'o', color = 'blue', s = taille_pt)
    ax.set_xlim([0, 1>>zoom])
    ax.set_ylim([0, 1>>zoom])
    ax.set_zlim([0, 1>>zoom])

def test_correlation(f, nbr_point):
    arrx = [f() for k in range(nbr_point)]
    arry = arrx[1:]+[f()]
    moyx = np.mean(arrx)
    moyy = np.mean(arry)
    cov = 0
    varx = 0
    vary = 0
    for k in range(nbr_point):
        cov += (arrx[k] - moyx)*(arry[k] - moyy)
        varx += (arrx[k] - moyx)**2
        vary += (arry[k] - moyy)**2
    coef = cov/np.sqrt(varx*vary) 
    print(coef)
    return coef < 0.01

def test_period(f, lim, nbr_retenus):
    vu = {}
    act = [0 for k in range(nbr_retenus)]
    for k in range(lim):
        act.append(f())
        act = act[1:]
        if tuple(act) in vu:
            return False
        vu[tuple(act)] = 0
    return True

def test_freq(f, nbr_par_categories, dim, offset_poids):
    cumul = [0 for k in range(64)]
    nbr_atteint = 0
    i = 0
    while nbr_atteint < 0.8*64 and i< nbr_par_categories*100 :
        n = 0
        for j in range(dim):
            n += int(f()*(1<<6//dim+offset_poids))%(1<<6//dim)*(1<<6//dim)**j
        cumul[n]+=1
        if cumul[n] == nbr_par_categories:
            nbr_atteint += 1
        i+=1
    q = 0
    Np=i/64
    for k in range(64):
        q+=(cumul[k]-Np)**2/Np
    if q<82.53 :
#pour une précision à 95%, on prend 82.53, 92.01 pour 99%
        return True
    return False

def test_partition(f, d):
    cumul = [0 for k in range(9)]
    for i in range(d):
        vu = [0 for k in range(9)]
        for k in range(9):
            vu[int(f()*9)] += 1
        dif = -1
        for k in range(9):
            if vu[k] != 0:
                dif += 1
        cumul[dif] += 1
    q = 0
    stirling = [1, 255, 3025, 7770, 6951, 2646, 462, 36, 1]
    for r in range(9):
        cumul_th = 1
        for i in range(r+1):
            cumul_th *= (9-i)
        cumul_th *= stirling[r]/9**9
        cumul_th *= d
        q += (cumul[r]-cumul_th)**2/cumul_th
    if q < 15.51:
#pour une précision à 95%, on prend 15.51, 20.09 pour 99%
        return True
    print(q, "\n")
    return False
