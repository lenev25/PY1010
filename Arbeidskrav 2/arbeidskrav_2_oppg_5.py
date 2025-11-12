"""

Arbeidskrav 2 - Oppgave 5

Løsning på oppgave: Lag et program med en funksjon som tar a og b som inn-argumenter, 
og som så regner ut arealet og ytre omkrets til en figur satt sammen av en rettvinklet trekant og en halvsirkel. 
Arealet og ytre omkrets skal skrives til skjerm med passende tekst. 

Av: Lene Valle

2025 10 24

"""

import numpy as np

#%% Henter inn a og b fra bruker

a = float(input('Oppgi lengden på trekantens kortside/sirkelens diameter (cm): '))
b = float(input('Oppgi lengden på trekantens langside (cm): '))

#%% Funksjon som beregner omkrets for figuren

def beregn_omkrets(x, y):
    hypotenus = np.sqrt(x**2 + y**2)  # Regner ut hypotenusen til trekanten
    
    omkrets_halvsirkel = (2*np.pi*(x/2))/2  # Regner ut omkretsen til halvsirkelen (omkretsen av en sirkel delt på 2)
    omkrets_trekant = (y + hypotenus)  # Regner ut omkretsen til den delen av trekanten som er en del av omkretsen til figuren (ikke kortsiden (a))

    omkrets_figur = omkrets_halvsirkel + omkrets_trekant  # Regner ut omkretsen til figuren ved å addere omkretsen av halvsirkelen og trekanten (minus a)
    return omkrets_figur

#%% Funksjon som beregner arealet av figuren

def beregn_areal(x, y):
    areal_halvsirkel = (np.pi*(x/2)**2)/2  # Regner ut av arealet av halvsirkelen (arealet av en sirkel delt på 2)
    areal_trekant = (y*x)/2  # Regner ut arealet av trekanten 

    areal_figur = areal_halvsirkel + areal_trekant
    return areal_figur

#%% Skriver ut resultatet til skjerm

omkrets = beregn_omkrets(a, b)
areal = beregn_areal(a, b)

print(f'\nFigurens ytre omkrets er {omkrets:.3f} cm, og figurens areal er {areal:.3f} cm\u00b2.') # Skrevet ut med tre desimaler. Koden \u00b brukes for å heve to-tallet i cm2. 

