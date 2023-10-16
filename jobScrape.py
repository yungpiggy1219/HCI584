from jobspy import scrape_jobs
import pandas as pd 
import time
import os.path

# Scrape UX jobs from from Linkedin
print("Scraping UX jobs from Linkedin...")
LIuxJobs = scrape_jobs(
    site_name=["linkedin"],
    search_term="ux",
    location="HI",
    results_wanted="1000",
    # location='USA',
    # country_indeed='USA'  # only needed for indeed
)
print(f"Found {len(LIuxJobs)} UX jobs on Linkedin")

# Check if file exists
if not os.path.isfile("jobs.csv"):
    # Create file if doesn't exist
    print("Results saved to a new file jobs.csv")
    LIuxJobs.to_csv("jobs.csv", index=False)
else:
    # Add results to existing file
    print("Adding results in existing file jobs.csv")
    LIuxJobs.to_csv("jobs.csv", mode="a", index=False, header=False)

# Read jobs.csv
df_state = pd.read_csv("jobs.csv")
print("Total number of jobs: ",  len(df_state))

# Find Duplicated rows
Dup_Rows = df_state[df_state.duplicated()]
print("Number of duplicate Rows: ", len(Dup_Rows))

DF_RM_DUP = df_state.drop_duplicates(keep='first')
print('Number of job after duplicate removed: ', len(DF_RM_DUP))
DF_RM_DUP.to_csv("jobs.csv", index=False)

""" 
# Scrape HCI jobs from from Linkedin
print("Scraping HCI Jobs...")
time.sleep(10)
LIhciJobs = scrape_jobs(
    site_name=["linkedin"],
    search_term="human computer interaction",
    results_wanted="100",
    location='USA',
    country_indeed='USA'  # only needed for indeed
)
print(f"Found {len(LIhciJobs)} HCI jobs")
LIhciJobs.to_csv("jobs.csv", index=False)

# Scrape HF jobs from from Linkedin
print("Scraping Human Factors Jobs on Linkedin...")
time.sleep(10)
LIhfJobs = scrape_jobs(
    site_name=["linkedin"],
    search_term="human factors",
    results_wanted="100",
    location='USA',
    country_indeed='USA'  # only needed for indeed
)
print(f"Found {len(LIhfJobs)} Human Factors jobs")
LIhfJobs.to_csv("jobs.csv", index=False) """