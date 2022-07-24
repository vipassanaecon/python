#import packages
import pandas as pd
import matplotlib.pyplot as plt

#extract data and create dataframe
df = pd.read_csv(r"World Bank Data\API_SP.DYN.TFRT.IN_DS2_EN_csv_v2_4353441\API_SP.DYN.TFRT.IN_DS2_EN_csv_v2_4353441.csv", delimiter=",", skiprows=4, encoding= 'unicode_escape')
df
