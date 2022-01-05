## Exploratory Data Analysis Using MTA Turnstile Data

### What is the framing question of your analysis, or the purpose of the model/system you plan to build?

What patterns and changes in commuter behavior occcured during the COVID-19 pandemic in NYC, and how can that information be used to better position COVID-19 testing sites for MTA users?

### Who benefits from exploring this question or building this model/system?

govermentally-run COVID testing programs (both city and state led), as well as partnered testing programs and nonprofits working on increasing testing availability in NYC.

### What dataset(s) do you plan to use, and how will you obtain the data?

* MTA Turnstile Data from January 2019-December 2021. 
Range selected to capture pre-pandemic patterns for comparison purposes. <br>
Location: Updated weekly at http://web.mta.info/developers/turnstile.html

* Weekly MTA Fare Data from January 2019-December 2021. <br>
Location: Updated weekly at http://web.mta.info/developers/fare.html

* Demographic Profiles of ACS 5 Year Estimates at the Neighborhood Tabulation Area (NTA) level. <br>
Location: NYC Open Data Portal, updated annually at https://data.cityofnewyork.us/City-Government/Demographic-Profiles-of-ACS-5-Year-Estimates-at-th/8cwr-7pqn

### What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?

* For the MTA Turnstile Data, an individual sample would include all of the entrances and exits for an entire station over one day. 

* For the MTA Fare Data, and individual sample would include fare types and the associated number of swipes recorded at all entrances of an entire station over one week. 

* For the Demographic Profile data, an individual sample would include age, gender, ethnicity/race, employment and health insurance coverage estimates for a specific neighborhood in NYC.  

### If modeling, what will you predict as your target?

I expect to find a large shift in the demographic spread and income level of regular MTA users from pre-pandemic to the current date.

### How do you intend to meet the tools requirement of the project?

I plan to clean and organize the datasets using SQL and Pandas, and use Mattplotlib and Seaborn to create visualizations.

### Are you planning in advance to need or use additional tools beyond those required?

I am not currently planning to use additional tools, but may choose to do so as analysis progresses. 

### What would a minimum viable product (MVP) look like for this project?

A simple analysis showing which stations were more consistently used in entry/exit and fare paying patterns indicating commute usage post-pandemic, relative to pre-pandemic levels. 
