## Analysis of MTA Usage Pre- and Post Pandemic

The goal of this project is to determine which stations have retained the most commuter traffic from their pre-pandemic levels, to better select high volume stations to use as COVID-19 testing centers,

I plotted the top ten stations by entry volume in 2019 as compared to entry volume in 2021, and got this figure: 

![Largest volume stations - change in volume from 2019 to 2021 ](https://github.com/saramoira/MTA-COVID-Testing-EDA/blob/main/images/largest.png)

In the figure above the 2019 entries are plotted in blue, and the 2021 entries are plotted in orange in a stacked orientation.

In order to get a better sense of stations that had a high volume of commuters throughout the pandemic, I computed to the 2021 entry totals as a percentage of the 2019 entry totals, and then sorted the top 50 results by total 2021 entry counts. 

This resulted in a similar plot as above, but with an entirely different set of stations in the top 10:

![Largest volume stations with high share of 2019 traffic in 2021](https://github.com/saramoira/MTA-COVID-Testing-EDA/blob/main/images/weighted.png)

This result suggests that optimal COVID-19 testing center placement my in fact be outside of major Manhattan MTA hubs if one wants to capture high-volume subway users. More analysis is being done using MTA fare type data and demographic info around stations to get a more granular result by week. 
