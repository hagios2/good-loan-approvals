import numpy as np
import pandas as pd

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 15)


read_loan_with_8C = pd.read_csv("Files/loan_approval_8_columns.csv")

read_approval_dataSet_extra = pd.read_csv("Files/loan_approval_dataset_extra.csv")

# print(read_approval_dataSet_extra.columns)

df_extra_selected = read_approval_dataSet_extra[[' no_of_dependents', ' education',
                                                 ' self_employed', ' income_annum', ' loan_amount', ' commercial_assets_value',
                                                 ' luxury_assets_value', ' bank_asset_value']]

# print(df_extra_selected)

combined_loan_dataset = pd.concat([read_loan_with_8C, df_extra_selected], axis=1)

print(combined_loan_dataset)

combined_loan_dataset.to_csv("Files/loan_approval_preprocessed.csv", index= False)