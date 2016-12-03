# Final-Project
Final project of Xinzhu Zhang, Xiaoyu Gao and Tao Chen

------------------------------------------------------------------------------------------
The goal of our project is to study the factors that may affect a country's life expectancy.  

The 2 Data sources we have used are :

1:WHO: 2000 and 2013 Global Health Observatory (GHO) Data 
http://www.who.int/gho/mortality_burden_disease/life_tables/en/

2:World Bank: 2013 World Development Indicators (WDI)
http://data.worldbank.org/products/wdi

-------------------------------------------------------------------------------------------
In our project folder, you can find data_collect.py. This is the code we wrote to download the data from API. 
	For Example, if run the code 'python collect_data.py national _ncome' in _terminal_, it will download both the data from World Bank and the life expectancy data,
	 and also generate a plotted graph showing the correlation between national income per capita and life expectancy. 
	
There is also a file called 'python merge.py' in the folder, which contains the code we wrote to merge all the variables we downloaded for each country. 
-------------------------------------------------------------------------------------------
Here is what you need to do launch our website:

	1. Cd to our 'Final-Project' directory in _terminal_
	2. Type in the code 'python manage.py runserver' 
	3. Copy this address 'http://127.0.0.1:8000/myapp/project°Ø to your browser, and you will see the home page of our website!	
-------------------------------------------------------------------------------------------
A brief description on the content of our website:	

   1. The _Homepage_ shows you the question we were trying to explore and our group members.
   2. If you click on _Life Expectancy at Birth_ in the _Overview_ dropdown menu, it will take you to our second page 
   	  which has a brief definition on life expectanct, a GeoPanda map showing the life expectancy of each country in 2013, 
	  and a table with the top 10 countries that have the longest life expectancy. 
   3. If you click on _Change in Life Expectancy_ in the _Overview_ dropdown menu, it will take you to our third page which 
   	  presents a GeoPanda map showing the change in life expentancy for each country from 2000 to 2013. 
	  The changes range from -8 to +18 (2 countries had a negative change, which are Iraq and Syria).
   4. On the _Influencing Factors_ page, you will be able to see the data for each country by selecting the country you are 
   	  interested in in the dropdown bar.
   5. The _Plot and Regression_ page will show you the plot on a variable of your choice and life expectancy.
   5. The final page _Data Sources_ has the links to the two data sources we used in the project.    
---------------------------------------------------------------------------------------------

Thank you, and have a great winter break! 
	   



