# MTA Locations for COVID-19 Testing: Improving the Selection Model
Saramoira Shields

## Abstract
The goal of this project was to analyze the MTA’s turnstile data over the course of the COVID-19 pandemic in order to make a recommendation to a nonprofit working to set up COVID-19 testing centers at significant MTA stations/hubs. The aim was to choose a complementary set of locations to those already set up by state and city agencies, with a focus on areas where there has been a high degree of commuter and local subway usage throughout the pandemic.     

## Design 
During the most recent wave of the pandemic, New York State has set up COVID-19 testing centers in seven of the largest MTA stations. I am working with a local nonprofit that is also looking to set up mobile testing units at subway stations - the goal is to complement the reach of the state program by focusing on stations with a high degree of local/commuter usage. This project compares 2019 subway usage to 2021 subway usage and incorporates fare data to develop a proxy for concentrations of local commuters, and uses a metric based on percentage of average 2019 traffic to choose candidate stations. 

## Data
This project largely uses the [MTA Turnstile Data](http://web.mta.info/developers/turnstile.html) available on the MTA website. I also made use of the weekly [MTA Fare Data](http://web.mta.info/developers/fare.html) to create visualizations, and the [MTA Remote Complex Lookup](https://qri.cloud/nyc-transit-data/remote_complex_lookup) built by [Chris Whong](https://medium.com/qri-io/taming-the-mtas-unruly-turnstile-data-c945f5f96ba0). Matplotlib, Seaborn and Plotly are used to visualize the relative change in usage across stations.


## Algorithms
This project used SQL, SQLAlchemy, and Pandas to clean and aggregate the different datasets. Initial visualizations were done in Matplotlib and Seaborn, and Plotly was used for the final figures.
