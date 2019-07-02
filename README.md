# Pipelines Project

For this project I've decided to use a world population dataset (available at https://www.kaggle.com/gemartin/world-bank-data-1960-to-2016). It contains population data for every country from 1960 until 2016. The dataset is saved in the "Input" folder inside "my-code". The project contains the following .py files:

**0. get.py:** reads the data from the .csv file and saves it into a dataframe.

**1. clean.py:** takes the dataframe and cleans it for further analysis.

**2. filter_fix.py:** takes in parameters (country, year from, year to) and filters the clean data following these parameters. Also, it modifies the structure of the dataframe to make the analysis more simple.

**3. analyse.py:** takes the filtered and fixed dataframe and calculates the population growth rate for the country and years selected. Also, it creates plots of the population and growth rates for the selected country during the selected years. The plots are saved as .png files in the "Output" folder.

**4. api_enrich.py:** takes the dataframe, identifies country name and country code and uses them to get information from the following API: https://restcountries.eu/. Obtains basic information about the selected country to enrich the information that will be included in the report.

**5. pdf.py:** takes the basic information obtained from the API along with the plots generated with *analyse.py* and creates a PDF report containing all the info. Saves the pdf report in the "Output" folder.

**6. main.py:** imports all other .py files and executes them in order. It takes the arguments for the *analyse.py* as parse arguments and ensures they're valid before executing all other files.

***FUTURE IMPROVEMENTS:*** generating a more professional looking pdf report with more insights and tables. Enrich the pipeline with information from other sources (possibly using web scraping). Create feature that sends the pdf report as an email attachment to the desired email account.




