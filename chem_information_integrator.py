
import pandas as pd

input_file_1 = './data/logP_BCF_CompTox.csv'
input_file_2 = './data/processed_TOX21_PPARg_BLA_Antagonist_ch1'
output_file  = './data/Integrated_dataset.csv'


df1 = pd.read_csv(input_file_1, encoding='utf-8')
df2 = pd.read_csv(input_file_2, encoding='utf-8')


dtxsid_to_properties = df2.set_index('DTXSID').to_dict(orient='index')


new_columns = ["PPAR_Emax", "PPAR_Assay"]
for col in new_columns:
    df1[col] = pd.NA


seen_dtxsids = set()
for idx, dtxsid in enumerate(df1['DTXSID']):
    if dtxsid not in seen_dtxsids:
        seen_dtxsids.add(dtxsid)
        if dtxsid in dtxsid_to_properties:
            for col in new_columns:
                df1.at[idx, col] = dtxsid_to_properties[dtxsid][col]


df1.to_csv(output_file, index=False)

print(f"File saved as {output_file}")