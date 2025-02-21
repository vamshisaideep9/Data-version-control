import pandas as pd
import os

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]

}

df = pd.DataFrame(data)



# Adding new row to df

new_row_loc = {'name': 'GF1', "Age": 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc


# adding another row

new_row_loc2 = {'name': 'GF2', "Age": 21, "City": 'City2'}
df.loc[len(df.index)] = new_row_loc2




data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")