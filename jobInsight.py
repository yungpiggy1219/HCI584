import tkinter as tk
import pandas as pd
from rapidfuzz import fuzz, process
import requests
from bs4 import BeautifulSoup

class jobSearch_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Job Insight")

        self.label = tk.Label(self, text="Insight for UX jobs on Linkedin within the United States")
        # Create a "Insight for UX jobs on Linkedin" Label and place it on the left (column 0)
        # self.label = tk.Label(self, text="Insight for UX jobs on Linkedin")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="e") 

        # Create an Entry Widget for Job Title with a specific width (e.g., 30 characters)
        # self.entry = tk.Entry(self)
        # self.entry.grid(row=0, column=1, columnspan=4, padx=10, pady=10, sticky="ew") 

        # Create a "Within" Label and place it on the left (column 0)
        # self.label = tk.Label(self, text="within: ")
        # self.label.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Create an Entry Widget for Radius with a specific width (e.g., 30 characters)
        # self.entry = tk.Entry(self, width=15)
        # self.entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Create a "of" Label and place it on the left (column 0)
        # self.label = tk.Label(self, text="of zipcode")
        # self.label.grid(row=1, column=2, padx=10, pady=10, sticky="e")

        # Create an Entry Widget for Zipcode with a specific width (e.g., 30 characters)
        # self.entry = tk.Entry(self, width=15)
        # self.entry.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        # Create a Search Button and place it on the right (column 2)
        self.search_button = tk.Button(self, text="Show Insight", command=self.start_search)
        self.search_button.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        # Create a Text widget that spans all three columns and is 30 lines tall
        # wrap="word" to wrap on word boundaries only
        self.text_widget = tk.Text(self, height=30, wrap="word") 
        self.text_widget.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        self.df = pd.read_csv('jobs.csv')   #  read the csv file into a data frame

    def start_search(self):
        # search_text = self.entry.get()
        search_text = "UX Designer"
        self.search(search_text, search_column="title")

    def search(self, search_term, search_column):
        if search_term != '':
            text, index, match = self.fuzzy_find(search_term, search_column)
            print(f"Best match for {search_term} is {text} with a score of {match}%")
            self.text_widget.delete("1.0", "end") # Optional: clear the text widget
            
            # if there is a > 50% match, print the job information,
            if match > 50:
                row = self.df.iloc[index]# get the row of the best match using the index
                jobTitle = row['title']     # get the title from the row  
                location = row['location'] # get the location of the job
                jobType = row['job_type'] # get the job type
                datePosted = row['date_posted'] # get the date posted
                # Radius = "Placeholder"


                # Present the total number of job found
                # If no zipcode set
                self.text_widget.insert("end", f"The total number of {jobTitle} jobs availble today is: ")

                # If zipcode set
                # self.text_widget.insert("end", f"The total number of {jobTitle} jobs in {Zipcode} availble today is: ")

                # If zipcode and radius set
                # self.text_widget.insert("end", f"The total number of {jobTitle} jobs {Radius} miles within {Zipcode} availble today is: ")

                # Compare the number today to prvious days
                # If higher
                # self.text_widget.insert("end", f"It is {jobTitle} more than yesterday.")
                # If lower
                # self.text_widget.insert("end", f"It is {jobTitle} less than yesterday. ")

                # Add chart of change in daily number of jobs available.

            else:
                self.text_widget.insert("end", f"No match found for {search_term} jobs")

    def fuzzy_find(self, search_term, column_name, n=1):
        matches = process.extract(search_term, self.df[column_name], scorer=fuzz.token_set_ratio, limit=n)
        #print("DEBUG", search_term, matches) # DEBUG a list of tuples (text, similarity score, index)
        text = matches[0][0] # the text of the best match
        match_score = matches[0][1] # the similarity score of the best match (0-100)
        index = matches[0][2] # the index in the data frame of the best match
        return text, index, match_score
    
    # Convert City to Zipcode
    def City_to_Zipcode(self, search_city: str) -> str: 
        return
    
    # Calculate Radius
    def Calculate_Radius(self, search_radius: int, search_city: str) -> int:
        return
    
    # Plot result (https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/)
    def Draw_Graph(self, total_number: list, range: str) -> None:
        return
    

        
if __name__ == "__main__":
    app = jobSearch_app()
    app.mainloop()