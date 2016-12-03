import pandas as pd
import numpy as np

try:
    import pycountry
except:
    os.system('pip install pycountry')
    import pycountry


###create life expenctancy 2013
df12 = pd.read_csv('whohlve.csv')
df12=df12.drop(['Unnamed: 0','Display Value','SEX','PUBLISHSTATE','YEAR','Low','High','Comments'], axis=1)
df12.to_csv('life 2013.csv',index = False)

###create change from 2000 to 2013
df11 = pd.read_csv('whohlve_origin_2000.csv')
df11 = df11.rename(columns=lambda x: x.strip())
df11 = df11.rename(columns={'COUNTRY':'Country','Numeric':'life expectancy 2000'})
df11=df11.drop(['Display Value','SEX','GHO','REGION','PUBLISHSTATE','YEAR','Low','High','Comments'], axis=1)
df11['Country'] = df11['Country'].apply(lambda x:pycountry.countries.get(alpha_3=x).name)

df11=pd.merge(df12,df11)
df11 = df11.rename(columns={'Numeric':'life expectancy 2013'})
df11['change'] = df11['life expectancy 2013']-df11['life expectancy 2000']
df11.to_csv('change.csv',index = False)

####create merged data
df = pd.read_csv('whohlve.csv')
df2 = pd.read_csv('national_income.csv')
df3 = pd.read_csv('density.csv')
df4 = pd.read_csv('pm_pollution.csv')
df5 = pd.read_csv('sanitation.csv')
df6 = pd.read_csv('education_expenditure.csv')
df7 = pd.read_csv('water_source.csv')
df8 = pd.read_csv('health_expenditure.csv')
df9 = pd.read_csv('urban_population.csv')
df10 = pd.read_csv('carbon_emission.csv')

df = pd.merge(df,df2)
df = pd.merge(df,df3)
df = pd.merge(df,df4)
df = pd.merge(df,df5)
df = pd.merge(df,df6)
df = pd.merge(df,df7)
df = pd.merge(df,df8)
df = pd.merge(df,df9)
df = pd.merge(df,df10)

###clean
df = df.rename(columns={'national_income':'national income per capita', 'density': 'population density','Numeric':'life expectancy', 'pm_pollution':'air pollution'})
df = df.rename(columns={'sanitation':'sanitation facility','education_expenditure':'education expenditure','water_source':'clean water source','health_expenditure':'health expenditure'})
df = df.rename(columns={'urban_population':'urban population percentage','carbon_emission':'carbon dioxide emission','Country':'country'})
df=df.drop(['SEX','Display Value','Unnamed: 0','PUBLISHSTATE','YEAR','Low','High','Comments','year'], axis=1)

df.to_csv('merged.csv',index = False)
