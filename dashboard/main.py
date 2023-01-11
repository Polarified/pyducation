import pandas as pd
import numpy as np
import streamlit as st
import csv
from datetime import datetime
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# st.title('Dashboard')

file = open('satellite.csv')
data = pd.read_csv(file)
# st.dataframe(data)

PLANET_REQUESTS_CSV_PATH = "planet_test.csv"


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == PLANET_REQUESTS_CSV_PATH:  # in this example, we only care about this one file
            print("The csv changed!")
            output_csv_path = predicted_requests(PLANET_REQUESTS_CSV_PATH)


def predicted_requests(path_to_requests_csv):
    file = open(path_to_requests_csv)
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)
    todays_date = datetime.today().strftime('%d.%m')
    todays_date_column = header.index(todays_date)
    print(todays_date)
    print(todays_date_column)
    print(type(todays_date_column))
    for request in csvreader:
        if request[todays_date_column:todays_date_column + 3].count("X") < 3:
            print("There was a prediction!")
            print(request[todays_date_column:todays_date_column + 3])

    # return output_csv_path


def main():
    # observer = Observer()
    # observer.schedule(Handler(), ".")  # watch the local directory
    # observer.start()
    #
    # try:
    #     while True:
    #         sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    #
    # observer.join()
    predicted_requests(PLANET_REQUESTS_CSV_PATH)


main()
