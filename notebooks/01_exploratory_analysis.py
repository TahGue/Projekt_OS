

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Sätt stil för visualiseringar
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Ladda data
data_path = os.path.join('..', 'data', 'athlete_events.csv')
df = pd.read_csv(data_path)

print(f"Dataset shape: {df.shape}")
print(f"\nKolumner: {df.columns.tolist()}")

# --- BASIC STATISTICS ---
print("\n" + "="*50)
print("GRUNDLÄGGANDE STATISTIK")
print("="*50)

# a) Antal länder
num_countries = df['NOC'].nunique()
print(f"\na) Antal länder: {num_countries}")

# b) Lista över länder
countries = sorted(df['NOC'].unique())
print(f"\nb) Länder (första 20): {countries[:20]}")
print(f"Totalt antal unika länder: {len(countries)}")

# c) Sporter
sports = sorted(df['Sport'].unique())
print(f"\nc) Sporter: {sports}")
print(f"Totalt antal sporter: {len(sports)}")

# d) Medaljtyper
medal_types = df['Medal'].dropna().unique()
print(f"\nd) Medaljtyper: {medal_types}")
print(f"Totalt antal medaljer: {df['Medal'].notna().sum()}")

# e) Ålder - Statistik
ages = df['Age'].dropna()
print(f"\ne) Ålder - Medel: {ages.mean():.1f}, Median: {ages.median():.1f}, "
      f"Min: {ages.min()}, Max: {ages.max()}, Std: {ages.std():.1f}")

# --- VISUALIZATIONS ---
print("\n" + "="*50)
print("GENERERAR VISUALISERINGAR")
print("="*50)

# Skapa figures-mapp om den inte finns
os.makedirs('../figures', exist_ok=True)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# g) Gender distribution
gender_counts = df['Sex'].value_counts()
axes[0,0].pie(gender_counts.values, labels=gender_counts.index, 
              autopct='%1.1f%%', colors=['#FF6B6B', '#4ECDC4'])
axes[0,0].set_title('Könsfördelning - Alla idrottare')

# h) Top 10 countries by medals
medal_counts = df[df['Medal'].notna()]['NOC'].value_counts().head(10)
axes[0,1].barh(medal_counts.index, medal_counts.values, color='#2A9D8F')
axes[0,1].invert_yaxis()
axes[0,1].set_title('Topp 10 Länder - Medaljer')
axes[0,1].set_xlabel('Antal medaljer')

# i) Medals over time
medals_over_time = df[df['Medal'].notna()].groupby('Year').size()
axes[1,0].plot(medals_over_time.index, medals_over_time.values, 
               marker='o', color='#E76F51', linewidth=2, markersize=4)
axes[1,0].set_title('Medaljer över tid')
axes[1,0].set_xlabel('År')
axes[1,0].set_ylabel('Antal medaljer')
axes[1,0].grid(True, alpha=0.3)

# j) Age distribution
axes[1,1].hist(df['Age'].dropna(), bins=30, color='#264653', alpha=0.8, edgecolor='black')
axes[1,1].set_title('Åldersfördelning - Alla idrottare')
axes[1,1].set_xlabel('Ålder')
axes[1,1].set_ylabel('Frekvens')
axes[1,1].axvline(ages.mean(), color='red', linestyle='--', linewidth=2, label=f'Medel: {ages.mean():.1f}')
axes[1,1].legend()

plt.tight_layout()
plt.savefig('../figures/eda_overview.png', dpi=300, bbox_inches='tight')
print("\n✓ Sparat: figures/eda_overview.png")
plt.close()

# --- KANADA-SPECIFIK ANALYS ---
print("\n" + "="*50)
print("KANADA-SPECIFIK ANALYS")
print("="*50)

# Filtrera för Kanada
canada_df = df[df['NOC'] == 'CAN']

print(f"\nTotalt antal deltagare från Kanada: {len(canada_df)}")
print(f"Unika idrottare från Kanada: {canada_df['ID'].nunique()}")
print(f"Antal medaljer för Kanada: {canada_df['Medal'].notna().sum()}")

# Medaljfördelning
canada_medals = canada_df[canada_df['Medal'].notna()]['Medal'].value_counts()
print(f"\nMedaljfördelning för Kanada:")
print(canada_medals)

# Top sports for Canada
canada_top_sports = canada_df[canada_df['Medal'].notna()]['Sport'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(canada_top_sports.index, canada_top_sports.values, color='#E63946')
ax.invert_yaxis()
ax.set_title('Kanada - Top 10 sporter med flest medaljer', fontsize=14, fontweight='bold')
ax.set_xlabel('Antal medaljer')
plt.tight_layout()
plt.savefig('../figures/canada_top_sports.png', dpi=300, bbox_inches='tight')
print("\n✓ Sparat: figures/canada_top_sports.png")
plt.close()

# Canada medals per Olympics
canada_medals_year = canada_df[canada_df['Medal'].notna()].groupby('Year').size()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(canada_medals_year.index, canada_medals_year.values, 
        marker='o', color='#1D3557', linewidth=2, markersize=6)
ax.set_title('Kanada - Medaljer per OS', fontsize=14, fontweight='bold')
ax.set_xlabel('År')
ax.set_ylabel('Antal medaljer')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../figures/canada_medals_per_year.png', dpi=300, bbox_inches='tight')
print("\n✓ Sparat: figures/canada_medals_per_year.png")
plt.close()

# Canada age distribution
canada_ages = canada_df['Age'].dropna()

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(canada_ages, bins=30, color='#457B9D', alpha=0.8, edgecolor='black')
ax.axvline(canada_ages.mean(), color='red', linestyle='--', linewidth=2, 
           label=f'Medel: {canada_ages.mean():.1f} år')
ax.set_title('Kanada - Åldersfördelning', fontsize=14, fontweight='bold')
ax.set_xlabel('Ålder')
ax.set_ylabel('Frekvens')
ax.legend()
plt.tight_layout()
plt.savefig('../figures/canada_age_distribution.png', dpi=300, bbox_inches='tight')
print("\n✓ Sparat: figures/canada_age_distribution.png")
plt.close()

print(f"\nKanada - Åldersstatistik:")
print(f"Medel: {canada_ages.mean():.1f} år")
print(f"Median: {canada_ages.median():.1f} år")
print(f"Min: {canada_ages.min()} år")
print(f"Max: {canada_ages.max()} år")

print("\n" + "="*50)
print("ANALYS KLAR!")
print("="*50)

