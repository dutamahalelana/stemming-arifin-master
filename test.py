import Fungsi
import re
import numpy as np


q = []
f = open("kamus.txt", "r")
for x in f:
    q.append(x)
new_list = [s.replace("\n", "") for s in q]

kata = ["katakan", "Membenci", "Mempunyai","berenang","sasaran",'berlari',"permasalahan","perjodohan","perselisihan","beterbangan","petarung","mendaki","menyaingi","terajin"]

fungsi  = Fungsi

for x in kata :
    kata_dasar  = fungsi.stemmingArifin(x,new_list)
    print(kata_dasar)

