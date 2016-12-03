import requests
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import sqlite3
import sys
import os
try:
    import pycountry
except:
    os.system('pip install pycountry')
    import pycountry
warnings.filterwarnings('ignore')

import IPython


def get_who(indicators, param_name):
    params = {
        'date': '2013:2013',
        'format': 'json'
    }
    rsp = r.get('http://api.worldbank.org/countries/all/indicators/'+indicators,
                params=params)
    j = rsp.json()
    total = j[0]['total']
    params = {
        'date': '2013:2013',
        'per_page': total,
        'format': 'json'
    }
    rsp = r.get('http://api.worldbank.org/countries/all/indicators/'+indicators,
                params=params)
    j = rsp.json()
    j = j[1]

    with open(param_name+'.csv', 'w') as f:
        f.write(','.join(['Country', 'year', param_name])+'\n')
        for jd in j:
            try:
                f.write(','.join(
                    [comma(jd['country']['value']), comma(jd['date']),
                     comma(jd['value'])])+'\n')
            except:
                continue


def comma(strs):
    return '"'+strs+'"'


if len(sys.argv) < 2:
    print(
'''\
Usage:      reg_data.py [data_name]
data_name:
        national_income     Adjusted net national income per capita of 2013
        density             population density of each country of 2013
        pm_pollution        pm2.5 pollution of each country of 2013
        sanitation          Improved sanitation facilities (% of population with access)
        carbon_emission     CO2 emissions (metric tons per capita)
        urban_population    Urban population (% of total)
        health_expenditure  Health expenditure per capita (current US$)
        water_source        Improved water source (% of population with access)
        education_expenditure Adjusted savings: education expenditure (% of GNI)

'''
)
    sys.exit()

r = requests.session()
# WHO life expectancy
rsp = r.get(
    'http://apps.who.int/gho/athena/api/GHO/WHOSIS_000001?format=csv&filter=COUNTRY:*;YEAR:2013;SEX:BTSX&x-sideaxis=COUNTRY')
with open('whohlve_origin.csv', 'w') as f:
    f.write(rsp.text)


# Adjusted net national income per capita NY.ADJ.NNTY.PC.CD
get_who('NY.ADJ.NNTY.PC.CD', 'national_income')

# population density EN.POP.DNST
get_who('EN.POP.DNST', 'density')

# PM2.5 air pollution, mean EN.ATM.PM25.MC.M3
get_who('EN.ATM.PM25.MC.M3', 'pm_pollution')

# Improved sanitation facilities SH.STA.ACSN
get_who('SH.STA.ACSN', 'sanitation')

#CO2 emissions (metric tons per capita)
get_who('EN.ATM.CO2E.PC', 'carbon_emission')

#Urban population (% of total)
get_who('SP.URB.TOTL.IN.ZS', 'urban_population')

#Health expenditure per capita (current US$)
get_who('SH.XPD.PCAP','health_expenditure')

#Improved water source (% of population with access)
get_who('SH.H2O.SAFE.ZS','water_source')

#Adjusted savings: education expenditure (% of GNI)
get_who('NY.ADJ.AEDU.GN.ZS','education_expenditure')


configlist = [
                ('NY.ADJ.NNTY.PC.CD', 'national_income'),
                ('EN.POP.DNST', 'density'),
                ('EN.ATM.PM25.MC.M3', 'pm_pollution'),
                ('SH.STA.ACSN', 'sanitation'),
                ('NY.ADJ.AEDU.GN.ZS','education_expenditure'),
                ('SH.H2O.SAFE.ZS','water_source'),
                ('SH.XPD.PCAP','health_expenditure'),
                ('SP.URB.TOTL.IN.ZS', 'urban_population'),
                ('EN.ATM.CO2E.PC', 'carbon_emission')

]


con = sqlite3.connect('database.sqlite')

df1 = pd.read_csv('whohlve_origin.csv')
df1 = df1.rename(columns=lambda x: x.strip())
df1 = df1.rename(columns={'COUNTRY':'Country'})
del(df1['GHO'])
del(df1['REGION'])
df1['Country'] = df1['Country'].apply(lambda x:pycountry.countries.get(alpha_3=x).name)
df1.to_csv('whohlve.csv')
df1.to_sql('who_hlve', con, if_exists='replace')


df1['Numeric'] = df1['Numeric'].astype(float)

for indicators, table_name in configlist:
    df = pd.read_csv(table_name+'.csv')
    df.to_sql('table_name', con, if_exists='replace')

if sys.argv[1] in [i[1] for i in configlist]:
    data_name = sys.argv[1]
    df2 = pd.read_csv(data_name+'.csv')
    df3 = pd.merge(df1, df2)
    # df3.to_sql(data_name, con, if_exists='replace')
    # df3[data_name] /= 1e+10
    lm = pd.ols(x=df3[data_name], y=df3['Numeric'])
    plt.plot(df3[data_name], df3['Numeric'], 'ro')
    plt.plot(df3[data_name], lm.y_fitted, 'r', linewidth=2)
    plt.ylabel('life expectancy')
    plt.xlabel(data_name)
    plt.title('life expectancy and '+sys.argv[1]+' regression')
    plt.show() # 改成 plt.savefig('regression.png')

# IPython.embed()
