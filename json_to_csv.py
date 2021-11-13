import pandas as pd

# Convert json to csv
df = pd.read_json(r'E:\shinshilka\data.json')
df.to_csv(r'E:\shinshilka\data_exel.csv', index=None, )
