import pandas as pd

df_syn_result = pd.read_csv('syn_result.csv', index_col=0)
df_place_label = pd.read_csv('place_label.csv', index_col=0)
df_netlist = pd.read_csv('netlist.csv', index_col=0)

merged_df = pd.merge(df_syn_result, df_place_label, on='Name')
merged = pd.merge(merged_df, df_netlist, on='Name')

merged_df.to_csv('testing.csv', index=False)
