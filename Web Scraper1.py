# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 09:42:16 2025

@author: Win 10 Pro
"""
# Import Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the websites to scrape
job_sites = [
    "https://www.linkedin.com/jobs/nairobi-jobs/?currentJobId=4092535752&originalSubdomain=ke",
    "https://www.brightermonday.co.ke/jobs/software-data"
]

# Step 2: Create an empty list to store job information
all_jobs = []

# Step 3: Loop through each job site
for site in job_sites:
    response = requests.get(site)  # Visit the website
    if response.status_code == 200:  # Check if the website is reachable
        soup = BeautifulSoup(response.text, "html.parser")  # Read the website
        
        # Step 4: Find job postings (this part may vary by website structure)
        job_elements = soup.find_all("div", class_="job-listing")  # Look for job cards

        for job in job_elements:
            # Extract job title
            title = job.find("h2", class_="job-title").text.strip()

            # Extract company name
            company = job.find("div", class_="company-name").text.strip()

            # Extract job location
            location = job.find("div", class_="job-location").text.strip()

            # Extract the link to apply
            link = job.find("a", class_="apply-link")["href"]

            # Save the job as a dictionary
            all_jobs.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Link": link
            })

# Step 5: Save all jobs to a CSV file
df = pd.DataFrame(all_jobs)
df.to_csv("C:/Users/Win 10 Pro/Desktop/JOB SKRAPER/jobs.csv", index=False)

print("Job data saved to jobs.csv!")
