from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "zip_recruiter"],
    search_term="software engineer",
    location="Dallas, TX",
    results_wanted=10,
    country_indeed='USA'  # only needed for indeed
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("jobs.csv", index=False)

# output to Excel
# jobs.to_xlsx('jobs.xlsx', index=False)
