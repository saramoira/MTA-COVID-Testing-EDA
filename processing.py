import pandas as pd
import datetime as dt
import sqlite3
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database/mta_data.db')

print(f"reading from mta_turnstile_data")                         
turnstiles_df = pd.read_sql('SELECT * FROM mta_turnstile_data', engine) 

# Create a single datetime column
print(f"creating a datetime column") 
import datetime

turnstiles_df['DATE_TIME'] = pd.to_datetime(turnstiles_df.DATE + ' ' + turnstiles_df.TIME, 
                                            format='%m/%d/%Y %H:%M:%S')

# Get rid of the duplicate entries
print(f"getting rid of duplicates")  
turnstiles_df.sort_values(['C/A', 'UNIT', 'SCP', 'STATION', 'DATE_TIME'], 
                          inplace=True, ascending=False)
turnstiles_df.drop_duplicates(subset=['C/A', 'UNIT', 'SCP', 'STATION', 'DATE_TIME'], inplace=True)

# get maximum entries per day per turnstile
print(f"calculating daily entries per turnstile") 
turnstiles_daily = (turnstiles_df
                        .groupby(['C/A', 'UNIT', 'SCP', 'STATION', 'DATE'], as_index=False)
                        .ENTRIES.first())
                        
# get entries per day per turnstile                      
turnstiles_daily[['PREV_DATE', 'PREV_ENTRIES']] = (turnstiles_daily
                                                       .groupby(['C/A', 'UNIT', 'SCP', 'STATION'])[['DATE', 'ENTRIES']]
                                                       .shift(1))
                                                       
# Drop the rows for the earliest date in the df
turnstiles_daily.dropna(subset=['PREV_DATE'], axis=0, inplace=True)   

def get_daily_counts(row, max_counter):
    '''
    Initial attempt at dealing with reversed counters
    '''
    
    counter = row['ENTRIES'] - row['PREV_ENTRIES']
    
    if counter < 0:
        counter = -counter  # adjust for "reverse" counter
        
    if counter > max_counter:
        # If counter (daily count) is > 20,000, then the counter might have been reset. 
        # Note that 200,000 works out to approximately 2.3 counts per second, still a bit high 
        # Set count to zero as different counters have different cycle limits
        print(f"ENTRIES: {row['ENTRIES']} <-- {row['PREV_ENTRIES']}")

        return 0
    
    return counter


_ = turnstiles_daily.apply(get_daily_counts, axis=1, max_counter=20000)   

#Write to SQL database
print(f"writing to mta_turnstiles_daily") 
turnstiles_daily.to_sql('mta_turnstiles_daily', engine)                                             
