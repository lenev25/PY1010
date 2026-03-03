"""

Prosjektoppgave PY1010 - 2026

Løsning på oppgave: Support Dashboard

6 deloppgaver som henter inn data fra excelfil med data (for uke 24) loggført 
for supportavdelingen ved telefonselskapet MORSE. 

Deloppgave a)
Skriv et program som leser inn filen og lagrer datene i kolonner.

Deloppgave b)
Skriv et program som finner antall henvendelser for hver av de 5 ukedagene 
(visualiser med søylediagram).

Deloppgave c)
Finn minste og lengste samtaletid som er loggført for uke 24. Skriv svaret 
til skjerm med informativ tekst.

Deloppgave d)
Skriv et program som regner ut gjennomsnittlig samtaletid basert på alle 
henvendelser i uke 24

Deloppgave e)
Skriv et program som finner det totale antall henvendelser supportavdelingen 
mottok for hver av 2-timersbolkene (vakter).

Vis resultatet med et kakediagram.

Deloppgave f)
Overfør kundetilfredshet til NPS-systemet (Net Promoter Score).   

Komplett oppgavetekst finnes i vedlagte filer ("prosjektoppgave_tekst.pdf")

Av: Lene Valle

2026 03 03

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leser ut data fra excel-fil ved hjelp av pandas

filnavn = 'support_uke_24.xlsx'
data = pd.read_excel(filnavn)

# Deloppgave a): Henter ut verdiene i de ulike kolonnene i "data" og 
# konverterer dem til Numpy-arrays

u_dag = data['Ukedag'].values
kl_slett = data['Klokkeslett'].values
varighet = data['Varighet'].values
score = data['Tilfredshet'].values

print('\n\nDeloppgave a)')
print('\nVerdiene hentet ut fra excel og konvertert til numpy arrays. Verdiene benyttes videre i oppgaven.')

# Deloppgave b): Finner antall henvendelser for de 5 ukedagene

# Oppretter en dictionary for å ta vare på tellingene

ukedag_dict = {
    'Mandag': 0,
    'Tirsdag': 0,
    'Onsdag': 0,
    'Torsdag': 0,
    'Fredag': 0
}

# Teller antall ganger hver ukedag forekommer i u_dag og oppdaterer ukedag_dict

for dag in u_dag:
    ukedag_dict[dag] += 1

# Plotter dataene i et stolpediagram

dag = list(ukedag_dict.keys())
antall = list(ukedag_dict.values())

plt.close()
plt.figure(1, figsize = (12, 9))
plt.bar(dag, antall, width = 0.9, color = ('red', 'green', 'yellow', 'blue', 'orange'))

# Skriver ut antallet på toppen av hver stolpe

offset_y = 0.5

for k in range(0, len(dag)):
    plt.text(dag[k], antall[k] + offset_y, str(antall[k]))

plt.title('Antall henvendelser i uke 24')
plt.xlabel('Ukedag')
plt.ylabel('Antall henvendelser')

plt.show()    

print('\n\nDeloppgave b)')
print('\nDet dukket forhåpentligvis opp et stolpediagram her.')

# Deloppgave c) Finner lengste og korteste samtaletid og skriver resultatet 
# til skjerm

#Konveerterer dataene i arrayen "varighet" til en varighet på antall sekunder

def konverter_hms_to_sek(tid):
    h, m, s = [int(x) for x in tid.split(':')]
    sekunder = s + m*60 + h*3600
    return sekunder

# Funksjon som konverterer sekunder tilbake til time, minutt og sekund-format
# Bruker modulo for å hente ut rest etter divisjon og numpy sin floor for å
# hente laveste heltall

def konverter_sek_to_hms(sekunder):
    h = int(np.floor(sekunder/3600))
    m = int(np.floor((sekunder % 3600)/60))
    s = int(sekunder % 60)
    return h, m, s

# Lager en ny array som holder antall sekunder per samtale

varighet_sek = np.zeros(len(varighet))

for j in range(len(varighet)):
    varighet_sek[j] += konverter_hms_to_sek(varighet[j])

# Finner minste og lengste samtaletid

maks_varighet = konverter_sek_to_hms(max(varighet_sek))
min_varighet = konverter_sek_to_hms(min(varighet_sek))

# Skriver ut resultatet til skjerm

print('\n\nDeloppgave c)')

print(f'\nDen lengste samtalen hadde en varighet på {maks_varighet[0]} timer, ' 
    f'{maks_varighet[1]} minutter og {maks_varighet[2]} sekunder.'
)

print(f'\nDen korteste samtalen hadde en varighet på {min_varighet[0]} timer, '
    f'{min_varighet[1]} minutter og {min_varighet[2]} sekunder.'
)

# Deloppgave d) bruker funksjonene fra forrige deloppgave til å finne 
# gjennomsnittlig samtaletid

gjennomsnittlig = sum(varighet_sek)/len(varighet_sek)

gjen_varighet = konverter_sek_to_hms(np.floor(gjennomsnittlig))

print('\n\nDeloppgave d)')

print(f'\nGjennomsnittlig samtaletid i uke 24 var {gjen_varighet[0]} timer, '
    f'{gjen_varighet[1]} minutter og {gjen_varighet[2]} sekunder.'
)

# Deloppgave e) Finner antall henvendelser i uke 24 fordelt på tidsbolker og 
# presenterer i et kakediagram

# Lager en dictionary for å telle antall henvendelser per tidspunkt

tidsbolk_dict = {
    'kl 08-10': 0,
    'kl 10-12': 0,
    'kl 12-14': 0,
    'kl 14-16': 0
}

# Looper igjennom klokkeslettene for å oppdatere dictionaryen

for kl in kl_slett:
    timetall = int(kl.split(':')[0])
    if timetall >= 8 and timetall < 10:
        tidsbolk_dict['kl 08-10'] += 1
    elif timetall >= 10 and timetall < 12:
        tidsbolk_dict['kl 10-12'] += 1
    elif timetall >= 12 and timetall < 14:
        tidsbolk_dict['kl 12-14'] += 1
    elif timetall >=14 and timetall < 16:
        tidsbolk_dict['kl 14-16'] += 1
    else:
        print(f'{kl} er utenfor åpningstid.')

# Plotter dataene i et kakediagram

antall_henvendelser = np.array(list(tidsbolk_dict.values()))
antall_henvendelser_norm = antall_henvendelser/sum(antall_henvendelser)
my_labels = []

for tid in tidsbolk_dict:
    my_labels.append(f'{tid}: {tidsbolk_dict[tid]}')

plt.close('all')

plt.figure(1, figsize = (12, 9))

plt.rc('font', size = 12)

# Plotter dataene: Velger å sette startposisjonen til 90 (rett opp) og å endre rekkefølgen til å 
# følge klokka i stedet for counterclockwise som er standard for pie charts med pyplot.

plt.pie(antall_henvendelser_norm, labels = my_labels, autopct = '%.1f%%', 
    startangle = 90, counterclock = False
)

plt.title('\nAntall henvendelser per tidsbolk')

plt.show()

print('\n\nDeloppgave e)')
print('\nDet dukket forhåpentligvis opp et kakediagram her.'
)

# Deloppgave f) Beregner selskapets NPS.

# Oppretter en dictionary for å ta vare på tellingene

nps_dict = {
    '1-6': 0,
    '7-8': 0,
    '9-10': 0
}

# Looper igjennom score for å telle antall henvendelser av hver type. 
# NaN sorteres ut ved hjelp av isnan-funksjonen i numpy. 

for sc in score:
    if np.isnan(sc):
        continue
    else:
        if int(sc) < 7:
            nps_dict['1-6'] += 1
        elif int(sc) >= 7 and int(sc) < 9:
            nps_dict['7-8'] += 1
        else:
            nps_dict['9-10'] += 1

svar = list(nps_dict.values())

antall_svar = sum(svar)

#Beregner NPS

nps = (svar[2]-svar[0])/antall_svar*100

#Skriver svaret til skjerm

print('\n\nDeloppgave f)')

print(f'\nSelskapets Net Promoter Score er {int(np.round(nps))} basert på {antall_svar} henvendelser.'
    f' {len(score)-antall_svar} gav ingen tilbakemelding.'
)



