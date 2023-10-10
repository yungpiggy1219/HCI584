""" from linkedin_scraper import Job, actions
from selenium import webdriver

driver = webdriver.Chrome()
email = "yungchu1219jpn@gmail.com"
password = "HCI584password"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
input("Press Enter")
job = Job("https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3456898261", driver=driver, close_on_complete=False)
 """

from linkedin_scraper import Person, actions
from selenium import webdriver
from linkedin_scraper import Company



""" driver = webdriver.Chrome()
email = "yungchu1219jpn@gmail.com"
password = "HCI584password"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal """
""" person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver) """
company = Company("https://linkedin.com/company/google")
print("Complete")