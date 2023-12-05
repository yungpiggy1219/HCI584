# HCI584 - Job Post Insight Developer's Guide

The app will be a job post analyzing tool where it will analyze the current job posts available and give insights. The app will scrape job websites, currently only Linkedin, to find new job opportunities and collect data to keep track of hiring trends.

## Install/deployment/admin issues:

N/a

## User Interaction

The application is divided into three main sections: Dashboard, Insight, and All Jobs.

1. **Dashboard**: This is the first screen that users see when they open the application. It displays a trend of job numbers for UX related jobs. Users can click the "Update" button to scrape new jobs from LinkedIn. The application will be unresponsive until the scraping is completed.
   <img width="786" alt="Dashboard Screen" src="https://github.com/yungpiggy1219/Job-Post-Insight-HCI584/assets/43735672/c21d1916-a4fe-45cb-ae7a-42cf3e987dda">

2. **Insight**: In this section, users can search for specific keywords such as "UX Designer", "Human Computer Interaction", etc. After the search, the list of jobs and the trend chart will be updated to reflect the search results.
   <img width="788" alt="Insight Screen" src="https://github.com/yungpiggy1219/Job-Post-Insight-HCI584/assets/43735672/4d5dfce3-889f-498b-9a94-2bef7a502250">

3. **All Jobs**: This section displays all the jobs stored in the CSV file. Users can view all the job postings that have been scraped from LinkedIn.
   <img width="785" alt="All Job Screen" src="https://github.com/yungpiggy1219/Job-Post-Insight-HCI584/assets/43735672/0be64777-a840-417b-8d47-0aeb92dc2c7f">

The application starts by displaying the Dashboard. Users can navigate to the Insight and All Jobs sections by clicking the corresponding buttons or tabs in the application.

The code starts with the class `jobSearch_app`.
The `jobSearch_app` is the main application class in a Tkinter-based GUI application.
The class inherit from tk.Tk and is responsible for initializing the application, creating and managing the main window, and handling individual frames/pages, and managing the interactions between them.
