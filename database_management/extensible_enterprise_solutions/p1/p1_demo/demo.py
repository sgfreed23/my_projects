#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

import datetime
import matplotlib.pyplot as pit
import pandas_datareader as pdr
from matplotlib import style


def get_requirements():
    print("Data Analysis 1\n")
    print("Developer: Samuel Freed\n")
    print("Program Requirements:\n"
        + "1. Run demo.py\n"
        + "2. If errors, more than likely missing installations.\n"
        + "3. Test Python Package Installer: pip freeze\n"
        + "4. Research how to do the following installations:\n"
        + "\ta. pandas (only if missing)\n"
        + "\tb. pandas-datareader (only if missing)\n"
        + "\tc. matplotlib (only if missing).\n"
        + "5. Create at least three functions that are called by the program:\n"
        + "\ta. main(): calls at least two other functions.\n"
        + "\tb. get_requirements(): displays program requirements.\n"
        + "\tc. data_analysis_1(): displays the following data."
        )

def data_analysis_1():
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime(2018, 10, 23)

    df = pdr.DataReader("XOM","yahoo",start,end)

    print("\nPrint number of records: ")
    print(df.shape[0])

    print("\nPrint columns: ")
    print(df.columns)

    print("\nPrint data frame: ")
    print(df)

    print("\nPrint first five lines: ")
    print(df.head(5))

    print("\nPrint last five lines: ")
    print(df.tail(5))

    print("\nPrint first two lines: ")
    print(df.head(2))

    print("\nPrint last two lines: ")
    print(df.tail(2))

    style.use('ggplot')

    df['High'].plot()
    df['Adj Close'].plot()
    pit.legend()
    pit.show()


