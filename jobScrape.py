from jobspy import scrape_jobs
import pandas as pd
import time
import os.path

# Scrape UX jobs from from Linkedin


class JobScraper:
    def __init__(self):
        self.offset = 0
        self.chunk_size = 50
        self.chunk = 0
        self.num_chunks = 3  # change this to get more

    def scrapeJob(self):
        print("Scraping UX jobs from Linkedin")

        self.offset = 0
        self.chunk_size = 50
        self.chunk = 0
        self.num_chunks = 3  # change this to get more

        # for chunk in range(0, num_chunks):
        while self.chunk < self.num_chunks:
            try:
                print(f"Scraping chunk {self.chunk+1}...")
                jobs = scrape_jobs(
                    # neither linkedin nor indeed worked for me
                    site_name=["Linkedin"],
                    search_term="ux",
                    # location="60640",
                    results_wanted=self.chunk_size,
                    offset=self.offset,
                    # location='USA',
                    # country_indeed='USA'  # only needed for indeed
                )
            except:
                print("End of Search. Scraping Stopped.")
                break

            else:
                print(
                    f"Found {len(jobs)} UX jobs on Linkedin in chunk {self.chunk+1}")
                print("offset: ", self.offset)
                print("chunk size: ", self.chunk_size)
                self.offset += self.chunk_size
                self.chunk += 1

            # Check if file exists
            if not os.path.isfile("jobs.csv"):
                # Create file if doesn't exist
                print("Results saved to a new file jobs.csv")
                jobs.to_csv("jobs.csv", index=False)
            else:
                # Add results to existing file
                print("Adding results in existing file jobs.csv")
                jobs.to_csv("jobs.csv", mode="a", index=False, header=False)
            time.sleep(5)

        # Read jobs.csv
        df_state = pd.read_csv("jobs.csv")
        print("Total number of jobs: ",  len(df_state))

        # Find Duplicated rows
        Dup_Rows = df_state[df_state.duplicated()]
        print("Number of duplicate Rows: ", len(Dup_Rows))

        DF_RM_DUP = df_state.drop_duplicates(keep='first')
        print('Number of jobs after duplicate removed: ', len(DF_RM_DUP))
        DF_RM_DUP.to_csv("jobs.csv", index=False)
