"""

Arbeidskrav 2 - Oppgave 4

Løsning på oppgave: 
a) Opprett en dictionary med ulike land som nøkkel og hovedstad og antall inbyggere som verdier.
b) Lag et program som ber brukeren skrive inn et land og på bakgrunn av dette skriver ut en setning om hovedstad og innbyggertall.
c) Lag et program som lar brukeren legge inn ny informasjon i dictionaryen for deretter å skrive ut den nye dictionaryen til skjerm.

Av: Lene Valle

2025 10 24

"""

#%% Oppretter dictionary med nøkler og verdier

data = {
    'Norge': ['Oslo', 0.634],
    'England': ['London', 8.982],
    'Frankrike': ['Paris', 2.161],
    'Italia': ['Roma', 2.873]
    }

#%% Program som tar inn et land fra dictionaryen og skriver ut resultatet

land = input(f'Oppgi hvilket av disse landene ({', '.join(data.keys())}) du ønsker mer informasjon om: ')

#%% Funksjon som sørger for at inputdataen har stor forbokstav

def stor_forbokstav(input_tekst):
    ny_tekst = input_tekst[0].upper() + input_tekst[1:].lower()
    return ny_tekst 

#%% Input fra bruker eventuelt oppdatert med stor forbokstav

land_medstorbokstav = stor_forbokstav(land)

#%% Henter ut verdiene fra dictionary

hovedstad = data[land_medstorbokstav][0]  # Henter ut første verdi av verdiene i dictionaryen
innbyggertall = data[land_medstorbokstav][1]  # Henter ut andre verdi av verdiene i dictionaryen

#%% Skriver ut informasjon om landet til skjerm

print(f'\n{hovedstad} er hovedstaden i {land_medstorbokstav} og det er {innbyggertall} mill. innbyggere i {hovedstad}.\n')

#%% Spør om bruker ønsker å oppdatere dictionary med informasjon om et nytt land

ny_info = input('Ønsker du å legge til informasjon om et nytt land (Y/N)? ')

if ny_info.upper() == 'Y':  # Gjør om til stor bokstav i tilfelle brukt liten bokstav
    
    #%% Henter inn ny informasjon fra bruker

    nytt_land = stor_forbokstav(input('\nSkriv inn navnet på det nye landet: '))
    ny_hovedstad = stor_forbokstav(input(f'Skriv inn hovedstaden i {nytt_land}: '))
    nytt_inbyggertall = float(input(f'Skriv inn innbyggertallet i {ny_hovedstad} (rundet av til millioner, husk punktum som skilletegn): '))

    #%% Oppdaterer dictionary

    data[nytt_land] = [ny_hovedstad, nytt_inbyggertall]
    
    #%% Skriver ut dictionary til skjerm

    print(f'\n{data}')
else:
    quit()