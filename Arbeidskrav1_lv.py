"""
Arbeidskrav 1 - PY1010-1 25H Python-programmering

Kode som beregner og presenterer de årlige kostnadene for elbil og bensinbil. 

Av Lene Valle

Sist oppdatert: 2025 09 26
"""

#%% Hente inn årlig kjørelengde fra bruker

km_aar = float(input('Legg inn en årlig kjørelengde (km):\n'))

#%% Forsikringskostnader

fors_eb = 5000  # Forsikringskostnader elbil (eb) per år
fors_bb = 7500  # Forsikringskostnader bensinbil (bb) per år

#%% Trafikkforsikringsavgift

tfa = 8.38*365  # Trafikkforsikringsavgift per år (likt for eb og bb)

#%% Drivstofforbruk

driv_eb = (0.2*km_aar)*2.0  # Drivstofforbruk elbil basert på 0,2 kWh/km og en pris på 2,0 kr/kWh
driv_bb = 1.0*km_aar  # Drivstofforbruk bensinbil anslått til 1,0 kr/km

#%% Bomavgift

bom_eb = 0.1*km_aar  # Bomavgift elbil 
bom_bb = 0.3*km_aar  # Bomavgift bensinbil 

#%% Totale utgifter

tot_eb = fors_eb+tfa+driv_eb+bom_eb  # Totale utgiter elbil
tot_bb = fors_bb+tfa+driv_bb+bom_bb  # Totale utgifter bensinbil 

#%% Utskrift
print('\n')
print('Den totale årlige kostnaden for elbil basert på din årlige kjørelengde: \t', tot_eb, 'kr.')
print('Den totale årlige kostnaden for bensinbil basert på din årlige kjørelengde:\t', tot_bb, 'kr.')
print('\n')
print('Basert på din årlige kjørelengde sparer du', tot_bb-tot_eb, 'kr årlig på å kjøpe elbil.')






