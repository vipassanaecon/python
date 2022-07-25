#import packages
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

#extract data and create dataframe
df = pd.read_csv(r"C:\Users\straw\vipassanaecon projects\vipassanaecon\Website\python\infertility_trap\World Bank Data\API_SP.DYN.TFRT.IN_DS2_EN_csv_v2_4353441\API_SP.DYN.TFRT.IN_DS2_EN_csv_v2_4353441.csv", delimiter=",", skiprows=4, encoding= 'unicode_escape')
df.head()

df.loc['total'] = df[0:].mean(numeric_only=True) #take each column starting at row index 0 thru last row index 
df

dftotal = pd.DataFrame(df.loc['total'])
dftotal

dftotal.head() #view head of dataframe

print(dftotal.dtypes) 

# Drop first four rows
dftotal.drop(index=dftotal.index[0:4], 
        axis=0, 
        inplace=True)
dftotal

print(dftotal.dtypes) 

#dftotal['total'] = dftotal['total'].astype(int)

dftotal.plot.line()

plt.figure(figsize=(100,40))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(dftotal) 
plt.title("Global Average Fertility Rate")
plt.xlabel("Year")
plt.ylabel("Average Fertility Rate")
plt.axis([0,50, 2.5, 6])
plt.show()
