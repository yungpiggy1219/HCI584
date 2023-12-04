import tkinter as tk
from tkinter import ttk
import pandas as pd
from rapidfuzz import fuzz, process
from pandastable import Table, TableModel, config
from jobspy import scrape_jobs
import pandas as pd
import time
import os.path
from jobScrape import JobScraper

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

LARGEFONT = ("Verdana", 35)


class jobSearch_app(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Job Insight")

        # Container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initializing frames
        self.frames = {}
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        for F in (Dashboard, Insight, AllJobs):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Dashboard)

    # Display Current Frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def on_closing(self):
        self.quit()
        self.destroy()

# Dashboard Frame


class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Dashboard Label
        label = ttk.Label(self, text="Dashboard", font=LARGEFONT)
        label.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

        # Read jobs.csv
        self.df = pd.read_csv("jobs.csv")

        # Read the last updated date
        self.df['date_posted'] = pd.to_datetime(self.df['date_posted'])
        self.max_date_year = self.df['date_posted'].max()

        # Format the date
        self.max_date = self.max_date_year.strftime("%b %d")
        self.max_year = self.max_date_year.strftime('%Y')

        ### Nav Bar ###
        # Dashboard Button
        dashboardBtn = ttk.Button(self, text="Dashboard",
                                  command=lambda: controller.show_frame(Dashboard))
        dashboardBtn.grid(row=1, column=0, padx=10, pady=10)

        # Insight Button
        insightBtn = ttk.Button(self, text="Insight",
                                command=lambda: controller.show_frame(Insight))
        insightBtn.grid(row=2, column=0, padx=10, pady=10)

        # All Jobs Button
        AllJobsBtn = ttk.Button(self, text="All Jobs",
                                command=lambda: controller.show_frame(AllJobs))
        AllJobsBtn.grid(row=3, column=0, padx=10, pady=10)

        ### Dashboard Content ###

        # Total Number
        label = ttk.Label(self, text="Total of")
        label.grid(row=1, column=1, columnspan=2)

        self.total_number_label = ttk.Label(
            self, text=len(self.df), font=LARGEFONT)
        self.total_number_label.grid(row=2, column=1, columnspan=2)

        label = ttk.Label(self, text="jobs")
        label.grid(row=3, column=1, columnspan=2)

        # Last Updated
        label = ttk.Label(self, text="Last Updated:")
        label.grid(row=1, column=4, columnspan=2)

        self.last_updated_label = ttk.Label(
            self, text=self.max_date, font=LARGEFONT)
        self.last_updated_label.grid(row=2, column=4, columnspan=2)

        label = ttk.Label(self, text=self.max_year)
        label.grid(row=3, column=4, columnspan=2)

        # Job Scrape Button
        self.scraper = JobScraper()
        update_button = tk.Button(
            self, text="Update", command=self.updateButton)
        update_button.grid(row=1, column=6, rowspan=3, sticky="nesw", padx=10)

        # Job Trend Chart
        fig, ax = plt.subplots()
        job_counts_monthly = self.df.resample('M', on='date_posted').size()
        ax.plot(job_counts_monthly.index, job_counts_monthly.values)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.set_xlabel('Month')
        ax.set_ylabel('Number of jobs')

        chart_frame = tk.Frame(self, background="white", height=7)
        chart_frame.grid(row=4, column=1, columnspan=6,
                         sticky="nesw", padx=10, pady=10, ipady=50)
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update_values(self):
        # Update the total number
        total_number = len(self.df)
        self.total_number_label['text'] = total_number

        # Update the last updated
        last_updated = self.max_date
        self.last_updated_label['text'] = self.df['date_posted'].max()

    def updateButton(self):
        # Scrape jobs from Linkedin
        self.scraper.scrapeJob()
        self.update_values()

# Insight Frame


class Insight(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Read jobs.csv
        self.df = pd.read_csv("jobs.csv")

        # Insigh Label
        self.label = ttk.Label(self, text="Insight", font=LARGEFONT)
        self.label.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

        ### Nav Bar ###
        # Dashboard Button
        self.dashboardBtn = ttk.Button(self, text="Dashboard",
                                       command=lambda: controller.show_frame(Dashboard))
        self.dashboardBtn.grid(row=1, column=0, padx=10, pady=10)

        # Insight Button
        self.insightBtn = ttk.Button(self, text="Insight",
                                     command=lambda: controller.show_frame(Insight))
        self.insightBtn.grid(row=2, column=0, padx=10, pady=10)

        # All Jobs Button
        self.AllJobsBtn = ttk.Button(self, text="All Jobs",
                                     command=lambda: controller.show_frame(AllJobs))
        self.AllJobsBtn.grid(row=3, column=0, padx=10, pady=10)

        ### Insiht Content ###

        # Search Bar
        self.label = ttk.Label(self, text="Search for a job:")
        self.label.grid(row=1, column=1, sticky="w")

        # Input for search
        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=2, columnspan=4, sticky="ew")

        # # Dropdown Menu
        # options = ['by Job Title', 'by Location']
        # dropdown = ttk.Combobox(self, values=options)
        # dropdown.grid(row=1, column=6)  # Adjust the row and column as needed
        # dropdown.set('by Job Title')

        # Search Button
        self.search_button = tk.Button(
            self, text="Search", command=self.start_search)
        self.search_button.grid(row=1, column=6)

        # Search Result Status
        self.result_label = ttk.Label(self, text="")
        self.result_label.grid(row=2, column=1, columnspan=2, sticky="w")

        # Select and rename columns
        self.df = self.df[['title', 'company', 'location', 'job_type', 'date_posted']].rename(
            columns={'title': 'Job Title', 'company': 'Company', 'location': 'Location', 'job_type': 'Job Type', 'date_posted': 'Date Posted'})

        # Job Trend Chart
        self.chart_frame = tk.Frame(self, background="white", height=7)
        self.chart_frame.grid(row=3, column=1, columnspan=6,
                              sticky="nesw", padx=10, pady=10, ipady=50)
        # Create the Figure and Axes objects
        self.fig, self.ax = plt.subplots()
        self.fig.set_size_inches(5, 2)  # Width, Height
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.chart_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Pandas Table
        self.table_frame = tk.Frame(self)
        self.table_frame.grid(row=6, column=1, columnspan=6,
                              rowspan=4, sticky="nesw")
        self.pandasTable = Table(self.table_frame, dataframe=self.df)
        self.pandasTable.show()

    # Start Search Function
    def start_search(self):
        search_term = self.entry.get()
        search_result = self.search(search_term, search_column="Job Title")
        print(search_result)

        # Update the chart
        search_result['Date Posted'] = pd.to_datetime(
            search_result['Date Posted'])
        job_counts_monthly = search_result.resample(
            'M', on='Date Posted').size()

        # Clear the previous plot
        self.ax.clear()

        # Plot the new data
        self.ax.plot(job_counts_monthly.index, job_counts_monthly.values)
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        self.ax.xaxis.set_major_locator(mdates.MonthLocator())
        self.ax.set_xlabel('Month')
        self.ax.set_ylabel('Number of jobs')

        # Redraw the canvas
        self.canvas.draw()

        # Pandas Table
        self.pandasTable = Table(self.table_frame, dataframe=search_result)
        self.pandasTable.show()

    # Perform fuzzy search
    def search(self, search_term, search_column):
        if search_term != '':

            max_hits = self.df.shape[0]  # the number of rows in the data frame

            # Go through all rows and find matches > 50%
            matches = process.extract(search_term, self.df[search_column],
                                      scorer=fuzz.token_set_ratio, limit=max_hits)

            index_keep_row_list = []
            for i, m in enumerate(matches):
                # text = matches[i][0]  # the text of the best match
                # the similarity score of the best match (0-100)
                match_score = matches[i][1]
                index = matches[i][2]

                # if there is a > 50% match, keep this row
                if match_score > 50:
                    index_keep_row_list.append(index)

            matched_df = self.df.iloc[index_keep_row_list]
        if len(matched_df) > 0:
            # Update the text
            self.result_label['text'] = f"There are a total of {len(matched_df)} {search_term} jobs."
            return matched_df
        else:
            # Print No Match Found
            self.result_label['text'] = f"No match found for {search_term} jobs"

            # Clear the previous plot
            self.ax.clear()
            self.ax.set_xlabel('Month')
            self.ax.set_ylabel('Number of jobs')
            self.canvas.draw()

            # Update with Empty Pandas Table
            empty_df = pd.DataFrame()
            self.pandasTable = Table(self.table_frame, dataframe=empty_df)
            self.pandasTable.show()

    def fuzzy_find(self, search_term, column_name, n=1):
        matches = process.extract(
            search_term, self.df[column_name], scorer=fuzz.token_set_ratio, limit=n)
        # print("DEBUG", search_term, matches) # DEBUG a list of tuples (text, similarity score, index)
        text = matches[0][0]  # the text of the best match
        # the similarity score of the best match (0-100)
        match_score = matches[0][1]
        index = matches[0][2]  # the index in the data frame of the best match
        return text, index, match_score

# All Jobs Frame


class AllJobs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # All Jobs Label
        label = ttk.Label(self, text="All Jobs", font=LARGEFONT)
        label.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

        ### Nav Bar ###
        # Dashboard Button
        dashboardBtn = ttk.Button(self, text="Dashboard",
                                  command=lambda: controller.show_frame(Dashboard))
        dashboardBtn.grid(row=1, column=0, padx=10, pady=10)

        # Insight Button
        insightBtn = ttk.Button(self, text="Insight",
                                command=lambda: controller.show_frame(Insight))
        insightBtn.grid(row=2, column=0, padx=10, pady=10)

        # All Jobs Button
        AllJobsBtn = ttk.Button(self, text="All Jobs",
                                command=lambda: controller.show_frame(AllJobs))
        AllJobsBtn.grid(row=3, column=0, padx=10, pady=10)

        ### All Job Content ###

        # Read jobs.csv
        self.df = pd.read_csv("jobs.csv")

        # Select and rename columns
        self.df = self.df[['title', 'company', 'location', 'job_type', 'date_posted']].rename(
            columns={'title': 'Job Title', 'company': 'Company', 'location': 'Location', 'job_type': 'Job Type', 'date_posted': 'Date Posted'})

        # Pandas Table
        table_frame = tk.Frame(self)
        table_frame.grid(row=1, column=1, columnspan=6,
                         rowspan=4, sticky="nesw")

        pandasTable = Table(table_frame, dataframe=self.df)
        pandasTable.show()


if __name__ == "__main__":
    app = jobSearch_app()
    app.mainloop()
