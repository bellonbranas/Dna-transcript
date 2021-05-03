#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:29:24 2020

@author: alejandrobellonbranas
"""
#from itertools import groupby

def transcribir(sec):
    return sec.replace('T', 'U')

def traducir(sec):
    codon2aa = {"AAA":"K", "AAC":"N", "AAG":"K", "AAU":"N", 
                "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T", 
                "AGA":"R", "AGC":"S", "AGG":"R", "AGU":"S", 
                "AUA":"I", "AUC":"I", 'AUG':'M', "AUU":"I", 

                "CAA":"Q", "CAC":"H", "CAG":"Q", "CAU":"H", 
                "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P", 
                "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R", 
                "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L", 

                "GAA":"E", "GAC":"D", "GAG":"E", "GAU":"D", 
                "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A", 
                "GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G", 
                "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V", 

                "UAC":"Y", "UAU":"Y", 
                "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S", 
                "UGC":"C", "UGG":"W", "UGU":"C", 
                "UUA":"L", "UUC":"F", "UUG":"L", "UUU":"F"}

    prot = ''
    n=0
    
    while n<len(sec):
        if sec[n:n+3]=='AUG':
            prot += 'M'
        n+=1
        if prot == 'M':
            break
    n+=2
    for i in range(n,len(sec),3):
        if sec[i:i+3] in codon2aa:
            prot += codon2aa[sec[i:i+3]]
        else:
            break
                
    return prot    

sec2 = ""
with open('sequence.fasta') as f_in:
    x=f_in.readlines()
    s=''.join(i.replace("\n","") for i in x)
    s.replace(" ","")
rna = transcribir(s)
prot2 = traducir(rna)
sec2= (prot2)
print('La proteína es:')
print(sec2)
   
#print(seq)