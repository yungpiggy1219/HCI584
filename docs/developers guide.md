# HCI584 - Job Post Insight Developer's Guide

The app will be a job post analyzing tool where it will analyze the current job posts available and give insights. The app will scrape job websites, currently only Linkedin, to find new job opportunities and collect data to keep track of hiring trends.

## Install/deployment/admin issues:

N/a

## User Interaction

The application is divided into three main sections: Dashboard, Insight, and All Jobs.
The application starts by displaying the Dashboard. Users can navigate to the Insight and All Jobs sections by clicking the corresponding buttons or tabs in the application.

### jobSearch_app
The `jobSearch_app` is the main application class in a Tkinter-based GUI application. It is a subclass of `tk.Tk`, which is the root window of a Tkinter GUI application. Here's what it does:

- The `__init__` method initializes the application window and sets its title to "Job Insight". It also creates a container frame that will hold other frames (Dashboard, Insight, AllJobs).

- The `self.frames` dictionary is used to store these frames. Each frame is associated with its class (Dashboard, Insight, AllJobs).

- The `for` loop in the `__init__` method creates an instance of each frame and adds it to the `self.frames` dictionary. It also positions each frame in the grid layout of the container.

- The `show_frame` method is used to bring a frame to the front of the window. It takes a class (Dashboard, Insight, AllJobs) as an argument and raises the associated frame to the top of the window.

- The `on_closing` method is called when the window is about to be closed. It quits the application and destroys the window.

This class is essentially a framework for a multi-frame Tkinter application. It allows you to switch between different frames (Dashboard, Insight, AllJobs) in the same window.

All frames includes a navigation bar with buttons to switch between frames. Each button is associated with a command that calls the `show_frame` method of the `jobSearch_app` class with the appropriate argument (Dashboard, Insight, AllJobs).

### Dashboard
The `Dashboard` class represents the dashboard frame in the application. It is a subclass of `tk.Frame`. This is the first screen that users see when they open the application. It displays a trend of job numbers for UX related jobs. 

The Dashboard class contains several key components:

- A set of labels to display information to the user.
- A set of methods to scrape job data from LinkedIn, using JobSpy.
- An "Update" button that triggers the job scraping process when clicked. The application will be unresponsive until the scraping is completed.
- A method to read the scraped job data from the CSV file and updating the labels to display this data.
- A line graph that shows the number of jobs in each month.

The Dashboard class is responsible for initiating the job scraping process, displaying the scraped job data.
<img width="786" alt="Dashboard Screen" src="https://github.com/yungpiggy1219/Job-Post-Insight-HCI584/assets/43735672/c21d1916-a4fe-45cb-ae7a-42cf3e987dda">

### Insight
The `Insight` class represents the insight frame in the application. It is a subclass of `tk.Frame`. In this section, users can search for specific keywords such as "UX Designer", "Human Computer Interaction", etc. After the search, the list of jobs and the trend chart will be updated to reflect the search results.

The Insight class contains several key components:

- A set of labels to display information to the user.
- A method to read the scraped job data from the CSV file and updating the labels to display this data.
- A search bar where users can enter specific keywords. This is implemented using a `tk.Entry` widget.
- A "Search" button that triggers the search process when clicked. This could involve calling a method that performs a search on the job data using the keywords entered in the search bar.
- A method to perform a fuzzy search on the job data. This could involve using a library like `fuzzywuzzy` to find jobs that match the search keywords, even if the match is not exact.
- A line graph created using `matplotlib` that shows the number of jobs in each month.
- A table that shows the search result, using `pandastable`.

The Insight class is responsible for allowing the user to search the job data, displaying the search results.
<img width="788" alt="Insight Screen" src="https://github.com/yungpiggy1219/Job-Post-Insight-HCI584/assets/43735672/4d5dfce3-889f-498b-9a94-2bef7a502250">

### AllJobs Class
The `AllJobs` class represents the all jobs frame in the application. It is a subclass of `tk.Frame`. This section displays all the jobs stored in the CSV file. Users can view all the job postings that have been scraped from LinkedIn.

The AllJobs class likely contains several key components:

- A label or set of labels to display information to the user.
- A method to read the scraped job data from the CSV file and updating the labels to display this data.
- A table that shows the search result, using `pandastable`.

The AllJobs class is responsible for displaying all the scraped job data.
<img width="785" alt="All Job Screen" src="https://github.com/yungpiggy1219/Job-Post-Insight-HCI584/assets/43735672/0be64777-a840-417b-8d47-0aeb92dc2c7f">

## Known Issue
- The UI is not responsive. It does not resize the content if the window is resized.
- The window freeze when scraping data. A fresh start would freeze because it need to scrape and create a csv file in order for the entire program to run.
- The current navigation bar is copied three time.

## Future Work
In my initial plan, I envisioned the program to be highly interactive, allowing users to perform targeted searches using specific keywords for data scraping. However, implementing keyword-specific scraping has proven challenging, primarily due to the time-intensive nature of data retrieval. The presence of anti-scraping mechanisms on job post websites further complicates the process, making it difficult to efficiently gather a large volume of data.

As a workaround, I am considering a Plan B, which involves pre-scraping data and storing it in a CSV file. This approach would help mitigate the challenges posed by real-time scraping, providing users with a faster and more responsive experience during their interactions with the program.

Additionally, I initially intended to provide users with a broader range of filter options such as filter by Date Posted, City, Job Type, and etc., on the Insight page. Unfortunately, due to time constraints, the successful implementation of these additional filters has not been achieved as of yet.

## Ongoing deployment/development
At its current stage, the project is not mature enough for deployment. However, the intention is to further develop and refine the application to address its current limitations and enhance overall functionality. To ensure ongoing development, I plan to prioritize the completion of the unfinished features mentioned earlier.