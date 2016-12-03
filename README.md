# Final-Project
Final project of Xinzhu Zhang, Xiaoyu Gao and Tao Chen


Our project studies which possible factors are affecting country's life expectancy.  

Data source(links included in the page):
1:WHO: 2013 Global Health Observatory (GHO) Data

2:World Bank: 2013 World Development Indicator (WDI)


After you finished pulling our file into where you want to save it. You can download the data through collect_data.py, merge and clean the data through merge.py and open the website through manage.py (We have saved the merged and clean data into 'Final-Project/static/myapp/', if you don't want to repeat the process of downloading and merging, you can skip step one and two.)

Step one: download the raw data.
We wrote data_collect.py to download data through API and observe the plot for the varaibe we are interested. 

The variables that can be downloaded in data_collect.py are: 

        national_income     Adjusted net national income per capita of 2013
        density             population density of each country of 2013
        pm_pollution        pm2.5 pollution of each country of 2013
        sanitation          Improved sanitation facilities (% of population with access)
        carbon_emission     CO2 emissions (metric tons per capita)
        urban_population    Urban population (% of total)
        health_expenditure  Health expenditure per capita (current US$)
        water_source        Improved water source (% of population with access)
        education_expenditure Adjusted savings: education expenditure (% of GNI)

you can download data and check the plot of the variable you are interested in by entering the code `python collect_data.py 'variable name you are interested in'` in _terminal_. eg: `python collect_data.py national_income`

Step two: after you download all data you want, you can use merge.py to merge and clean them by entering the code `python merge.py` in _terminal.

Step three: launch the website.

1. Open the directory of 'Final-project'
2. Enter the code `python manage.py runserver` in _terminal_
3. Load the page ‘http://127.0.0.1:8000/myapp/project’ to the starting page
4. click on the interested title in the navigation bar and you will be directed to that page. 


