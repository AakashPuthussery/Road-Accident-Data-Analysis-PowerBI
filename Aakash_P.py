import pandas as pd
import numpy as np

# Load the provided sample dataset
data = pd.read_csv("F:\population_syntesize\Data.csv")

# Calculate proportions of each category in the sample dataset
total_samples = data.shape[0]
sex_proportions = data['Sex'].value_counts(normalize=True)
age_proportions = data['Age_category'].value_counts(normalize=True)
edu_proportions = data['Highest_education_level'].value_counts(normalize=True)

# Define population characteristics from Table 2
population_characteristics = {
    'Sex': {1: 25324, 2: 24676},
    'Age_category': {1: 17955, 2: 29642, 3: 2403},
    'Highest_education_level': {0: 7490, 1: 5655, 2: 24400, 3: 12455}
}

# Synthesize the population
synthesized_population = pd.DataFrame()

# Loop over each variable (sex, age category, highest education level)
for var, characteristics in population_characteristics.items():
    synthesized_category = pd.DataFrame()
    # Loop over each category within the variable
    for category, frequency in characteristics.items():
        # Calculate number of individuals needed to synthesize for each category
        num_samples = int(frequency * (50000 / total_samples))
        
        # Sample individuals from the dataset for each category
        sampled_individuals = data[data[var] == category].sample(n=num_samples, replace=True)
        
        # Concatenate sampled individuals
        synthesized_category = pd.concat([synthesized_category, sampled_individuals])
    
    # Concatenate synthesized individuals for each variable
    synthesized_population = pd.concat([synthesized_population, synthesized_category])

# Compute frequencies for each variable in the synthesized population
synthesized_frequencies = {
    'Sex': synthesized_population['Sex'].value_counts(),
    'Age_category': synthesized_population['Age_category'].value_counts(),
    'Highest_education_level': synthesized_population['Highest_education_level'].value_counts()
}

# Print the frequencies for the synthesized population
for var, frequencies in synthesized_frequencies.items():
    print(f"{var}:\n{frequencies}\n")
# Save frequencies for the synthesized population into a .txt file
with open('Aakash_P.txt', 'w') as f:
    for var, frequencies in synthesized_frequencies.items():
        f.write(var + ':\n')
        f.write(frequencies.to_string() + '\n\n')