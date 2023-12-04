#!/usr/bin/python3
def no_c(s):
    cena = s.translate({ord(i): None for i in 'cC'})
    return cena
