import pytest
import sqlite3


from SQL_005_corr import *
from crancee_eliott_tp_14 import *

def generate_test(nb):
    for n in range(1,nb+1):
        print("def test_Q"+str(n)+"_res ():")
        print("    assert sol_Q"+str(n)+"_res ==  Q"+str(n)+"_res")
        print()
        print("def test_Q"+str(n)+"_req ():")
        print("    assert requete(sol_Q"+str(n)+"_req) == requete(Q"+str(n)+"_req)")
        print() 
def generate_go(nb):
    for n in range(1,nb+1):
        print("test_Q"+str(n)+"_res ()")
        print("test_Q"+str(n)+"_req ()")


def requete (req):
    conn = sqlite3.connect('veekun-pokedex.sqlite')
    c=conn.cursor()
    c.execute(req)
    rep = c.fetchall()
    conn.close()
    return rep
    
def test_Q1_res ():
    assert sol_Q1_res ==  Q1_res

def test_Q2_res ():
    assert sol_Q2_res ==  Q2_res

def test_Q3_res ():
    assert sol_Q3_res ==  Q3_res

def test_Q4_res ():
    assert sol_Q4_res ==  Q4_res

def test_Q4_req ():
    assert requete(sol_Q4_req) == requete(Q4_req)

def test_Q5_res ():
    assert sol_Q5_res ==  Q5_res

def test_Q5_req ():
    assert requete(sol_Q5_req) == requete(Q5_req)

def test_Q6_req ():
    assert requete(sol_Q6_req) == requete(Q6_req)

def test_Q7_req ():
    assert requete(sol_Q7_req) == requete(Q7_req)

def test_Q8_res ():
    assert sol_Q8_res ==  Q8_res

def test_Q8_req ():
    assert requete(sol_Q8_req) == requete(Q8_req)

def test_Q9_res ():
    assert sol_Q9_res ==  Q9_res

def test_Q9_req ():
    assert requete(sol_Q9_req) == requete(Q9_req)

def test_Q10_res ():
    assert sol_Q10_res ==  Q10_res

def test_Q10_req ():
    assert requete(sol_Q10_req) == requete(Q10_req)

def test_Q11_res ():
    assert sol_Q11_res ==  Q11_res

def test_Q11_req ():
    assert requete(sol_Q11_req) == requete(Q11_req)

def test_Q12_res ():
    assert sol_Q12_res ==  Q12_res

def test_Q12_req ():
    assert requete(sol_Q12_req) == requete(Q12_req)

def test_Q13_req ():
    assert requete(sol_Q13_req) == requete(Q13_req)

def test_Q14_res ():
    assert sol_Q14_res ==  Q14_res

def test_Q14_req ():
    assert requete(sol_Q14_req) == requete(Q14_req)

def test_Q15_req ():
    assert requete(sol_Q15_req) == requete(Q15_req)

def test_Q16_res ():
    assert sol_Q16_res ==  Q16_res

def test_Q16_req ():
    assert requete(sol_Q16_req) == requete(Q16_req)

def test_Q17_res ():
    assert sol_Q17_res ==  Q17_res

def test_Q17_req ():
    assert requete(sol_Q17_req) == requete(Q17_req)

def test_Q18_req ():
    assert requete(sol_Q18_req) == requete(Q18_req)

def test_Q19_res ():
    assert sol_Q19_res ==  Q19_res

def test_Q19_req ():
    assert requete(sol_Q19_req) == requete(Q19_req)

def test_Q20_res ():
    assert sol_Q20_res ==  Q20_res

def test_Q20_req ():
    assert requete(sol_Q20_req) == requete(Q20_req)





def go():
    test_Q1_res ()
    test_Q1_req ()
    test_Q2_res ()
    test_Q2_req ()
    test_Q3_res ()
    test_Q3_req ()
    test_Q4_res ()
    test_Q4_req ()
    test_Q5_res ()
    test_Q5_req ()
    test_Q6_res ()
    test_Q6_req ()
    test_Q7_res ()
    test_Q7_req ()
    test_Q8_res ()
    test_Q8_req ()
    test_Q9_res ()
    test_Q9_req ()
    test_Q10_res ()
    test_Q10_req ()
    test_Q11_res ()
    test_Q11_req ()
    test_Q12_res ()
    test_Q12_req ()
    test_Q13_res ()
    test_Q13_req ()
    test_Q14_res ()
    test_Q14_req ()
    test_Q15_res ()
    test_Q15_req ()
    test_Q16_res ()
    test_Q16_req ()
    test_Q17_res ()
    test_Q17_req ()
    test_Q18_res ()
    test_Q18_req ()
    test_Q19_res()
    test_Q19_req()
    test_Q20_res()
    test_Q20_req()