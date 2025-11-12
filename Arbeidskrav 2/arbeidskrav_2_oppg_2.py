"""

Arbeidskrav 2 - Oppgave 2

Løsning på oppgave: Lag et program som beregner hvor mange pizzaer som skal handles inn til en klassefest. 
Man antar at hver elev spiser 1/4 pizza. 

Av: Lene Valle

2025 10 10

"""

import math

#%% Henter inn antall elever i klassen fra brukeren

antall_elever = int(input('Skriv inn antall elever: '))

#%% Beregner antall pizzaer som må bestilles

antall_pizzaer = math.ceil(antall_elever/4)  # Antar 1/4 pizza per elev

#%% Skriver ut resultatet

print('\nDu bør bestille', int(antall_pizzaer), 'pizzaer til festen.')


