"""

Arbeidskrav 2 - Oppgave 3

Løsning på oppgave: Lag et program med en funksjon som regner om fra grader til radianer. 

Av: Lene Valle

2025 10 24

"""

import numpy as np

#%% Henter inn gradtallet fra bruker

v_grad = float(input('Skriv inn gradtallet: ')) 

#%% Funksjon som regner om fra grader til radianer

def grader_til_radianer(grad):
    rad = grad*np.pi/180
    return rad

#%% Henter ut resultatet fra funksjonen

v_rad = grader_til_radianer(v_grad)

#%% Skriver ut resultatet til skjerm 

print(f'\nEn vinkel på {v_grad} grader tilsvarer {v_rad:.3f} radianer.')  #  radianene skrives ut med 3 desimaler. Bruker \n for å få mellomrom mellom input og utskriften.

