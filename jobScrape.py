from jobspy import scrape_jobs
import pandas as pd 
import time
import os.path

# Scrape UX jobs from from Linkedin
print("Scraping UX jobs from Linkedin")

offset = 0
chunk_size = 50
chunk = 0
num_chunks = 3  # change this to get more

#for chunk in range(0, num_chunks):
while True:
    try:
        print(f"Scraping chunk {chunk+1}...")
        jobs = scrape_jobs(
            site_name=["Linkedin"],  # neither linkedin nor indeed worked for me
            search_term="ux",
            # location="60640",
            results_wanted=chunk_size,
            offset=offset,
            # location='USA',
            # country_indeed='USA'  # only needed for indeed
        )
    except:
        print("End of Search. Scraping Stopped.")
        break

    else:
        print(f"Found {len(jobs)} UX jobs on Linkedin in chunk {chunk+1}")
        offset += chunk_size
        chunk += 1

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