# Job Post Insight

The app will be a job post analyzing tool where it will analyze the current job posts available and give insights. The app will scrape job websites, such as Indeed and Linkedin to find new job opportunities and collect data to keep track of hiring trends. It will analyze the level of experience, key qualifications, salary range, benefit, and number of new posts, repost of a certain job function.

## Potential User

My primary user would be someone who is actively looking for a job. The secondary user may be someone who is still in school and deciding their career.

## Problem

Job hunting can be tough. It is even harder when job posts are not standardized. Each job board has its own standards and there is no perfect one that allows an user to find the exact match.
This app will help users quickly know more about the job and its match to the user without having to read through the job description, and more importantly, to see hiring trends and other insight.

## Workflow

I imagined this app being a dashboard, showing daily new jobs, and flag any reposts, or job posts that weren’t actually hiring. To keep the scope smaller, this tool will support providing insight for UX related jobs such as UX/UI Designers, UX Researcher, Human Factors Engineers, and any Human-Computer Interaction related jobs. The dashboard will show list of job posts, it’s sources, and an overview of the trend.

## Resources Used in this Project

[JobSpy](https://github.com/cullenwatson/JobSpy)

[Matplotlib Chart](https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/)

## Revised Project Spec

- The original plan was more customizable. The project will now be an Insight tool where it will show the number of jobs from day to day. It will calculate the number of jobs in each state. The original plan allows the user to input to search for the job title. I'm now changing it so it will only scrap UX related jobs, and possibly some developer jobs as well.

## To Run the Program

### Requirements

Python 3.10 or 3.11 is required, since JobSpy requires 3.10 or 3.11.
To install the other required packages, please run

`pip install -r requirements.txt`

To run the program, you will be running **main.py**

When you run the program for the first time, it will perform an initial scraping. The program canvas will not show until the scraping is complete.
The scraping status will be updated through terminal.

There are 3 pages to the project:
### Dashboard
- You will be able to see a job number trend for UX related jobs
- You can use the "Update" button to scrape new jobs from Linkedin
  - The program will "freeze" until the scraping is completed
  - It will update existing jobs.csv with new results.
<img width="786" alt="Dashboard Screen" src="https://github.com/yungpiggy1219/Job-Post-Insight-HCI584/assets/43735672/c21d1916-a4fe-45cb-ae7a-42cf3e987dda">

### Insight
- You can use the search bar to search for keywords such as "UX Designer", "Human Computer Interaction", or etc.
- After the search, the list of job will update, and the trend chart will update as well

#### Before Search
<img width="788" alt="Insight Screen" src="https://github.com/yungpiggy1219/Job-Post-Insight-HCI584/assets/43735672/4d5dfce3-889f-498b-9a94-2bef7a502250">

#### Search with Results Found
<img width="789" alt="Screenshot 2023-12-05 at 12 34 55 PM" src="https://github.com/yungpiggy1219/Job-Post-Insight-HCI584/assets/43735672/e538567e-6a9c-4f10-b230-86a9d5cab4cf">

#### Search with No Results Found
<img width="788" alt="Screenshot 2023-12-05 at 12 36 46 PM" src="https://github.com/yungpiggy1219/Job-Post-Insight-HCI584/assets/43735672/4ca4ffad-df1d-4506-bdba-99c7625ed843">


### All Jobs
- In this page, you will be able to see all jobs stored in the csv file.
<img width="785" alt="All Job Screen" src="https://github.com/yungpiggy1219/Job-Post-Insight-HCI584/assets/43735672/0be64777-a840-417b-8d47-0aeb92dc2c7f">
