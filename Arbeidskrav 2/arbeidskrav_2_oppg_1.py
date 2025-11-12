"""

Arbeidskrav 2 - Oppgave 1

Løsning på oppgave: Lag et program som henter inn fødselsår og regner ut alderen til personen. 
Oppgaveteksten sier "nå i løpet av 2024", men jeg har valgt å bruke 2025 i stedet, 
ettersom jeg antar at oppgaveteksten er gjenbrukt fra i fjor. 

Av: Lene Valle

2025 10 10

"""

#%% Henter inn fødselsår fra bruker

alder = int(input('Hvilket år er du født? '))  

#%% Beregner alder (kaller den ny_alder siden oppgaven sier at fødselsåret skal ha variabelnavn "alder")

ny_alder = 2025-alder  # (år) 

#%% Skriver ut alderen

print('\nDu fyller', ny_alder, 'år i løpet av 2025.')

