import pandas as pd
import math

# Sensibilità dello strumento (incertezza costante)
instrument_sensitivity_period = 0.01  # in secondi (per il periodo)
instrument_sensitivity_length = 0.001  # in metri (per la lunghezza)

# Leggere i dati dal file CSV
data = pd.read_csv('data.csv')

# Calcolare il periodo medio per ciascuna lunghezza
mean_period = data.groupby('lunghezza')['periodo'].mean().reset_index(name='periodo')

# Calcolare la deviazione standard per ciascun gruppo
std_dev = data.groupby('lunghezza')['periodo'].std(ddof=0).reset_index(name='deviazione_standard')

# Unire i risultati
results = mean_period.merge(std_dev, on='lunghezza')

# Calcolare l'incertezza sul periodo medio come il massimo tra deviazione standard e sensibilità dello strumento
results['incertezza_periodo'] = results['deviazione_standard'].clip(lower=instrument_sensitivity_period)

# Aggiungere una colonna per l'incertezza sulla lunghezza, che è costante
results['incertezza_lunghezza'] = instrument_sensitivity_length

# Calcolo di g e propagazione dell'incertezza
results['g'] = (4 * math.pi**2 * results['lunghezza']) / (results['periodo']**2)
results['incertezza_g'] = results['g'] * (
    (2 * results['incertezza_periodo'] / results['periodo'])**2 +
    (results['incertezza_lunghezza'] / results['lunghezza'])**2
).pow(0.5)  # Radice quadrata per la propagazione combinata

# Salvare i risultati in un nuovo file CSV
results = results[['lunghezza', 'periodo', 'g', 'incertezza_lunghezza', 'incertezza_periodo', 'incertezza_g']]
results.to_csv('processed_data.csv', index=False)

print("File processed_data.csv creato con i risultati elaborati.")
