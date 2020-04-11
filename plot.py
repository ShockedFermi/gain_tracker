import numpy as np
import pandas as pd
import log
import matplotlib.pyplot as pl
import matplotlib.dates as mdates
import datetime

DATAFRAME = pd.DataFrame.from_dict(log.DATA, orient='index')
#print(DATAFRAME)
#print(DATAFRAME["push_ups"])


def str_to_datenums( str_dates ):
    datenums = []
    for date_str in str_dates:
        datenums.append( datetime.datetime.strptime( date_str, "%d/%m/%Y" ) )
    return datenums
    
def get_exercise_data(exercise_name):
    exercise_data = DATAFRAME["push_ups"].dropna()
    dates  = exercise_data.keys()
    values = np.array(exercise_data.values.tolist())
    return dates, values

def plot_exercise_progress(exercise_name):
    dates, values = get_exercise_data(exercise_name)
    fig, ax = pl.subplots( 1 )
    formatter = mdates.ConciseDateFormatter( mdates.AutoDateLocator() )
    ax.xaxis.set_major_formatter( formatter )
    ax.plot( str_to_datenums( dates ),
             values[:, 0])
    pl.show()

plot_exercise_progress( "push_ups" )
