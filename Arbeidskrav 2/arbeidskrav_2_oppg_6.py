"""

Arbeidskrav 2 - Oppgave 6

Løsning på oppgave: Skriv en kode som plotter funksjonen f(x) = -x^2 - 5 for x på intervallet [-10,10]  

Av: Lene Valle

2025 11 03

"""



import numpy as np
import matplotlib.pyplot as plt

#%% Definerer x og y

x = np.linspace(-10, 10, 200)  # Oppretter en array med 200 punkter i intervallet -10 til 10
y = - x**2 - 5

#%% Plotting av funksjonen

plt.close('all')
fig = plt.figure(1, figsize = (12, 9))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('$f(x) = - x^2 - 5$' )  # Bruker latex-kode for å få en fin tittel på figuren
plt.grid()
plt.show()