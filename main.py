# sourcery skip: avoid-builtin-shadow
import pandas as pd

df = pd.read_csv('pokedex.csv')
f = df[df["Generation"]==1]
print(f.filter(items=["Name","Generation"]))

