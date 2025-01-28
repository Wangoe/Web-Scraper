# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:08:45 2025

@author: Win 10 Pro
"""

# Import Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define websites
job_sites = [
    "https://www.linkedin.com/jobs/nairobi-jobs/",
    "https://www.brightermonday.co.ke/jobs/software-data"
]

# Set headers for requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Store job data
all_jobs = []

for site in job_sites:
    response = requests.get(site, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Update selectors based on the actual website structure
        job_elements = soup.find_all("div", class_="job-card-container")  # Adjust this

        for job in job_elements:
            try:
                title = job.find("h3", class_="job-card-title").text.strip()  # Adjust this
                company = job.find("h4", class_="job-card-company-name").text.strip()  # Adjust this
                location = job.find("span", class_="job-card-location").text.strip()  # Adjust this
                link = job.find("a", class_="job-card-link")["href"]  # Adjust this

                all_jobs.append({
                    "Title": title,
                    "Company": company,
                    "Location": location,
                    "Link": link
                })
            except AttributeError:
                continue  # Skip if any data is missing

# Save to CSV if jobs were found
if all_jobs:
    df = pd.DataFrame(all_jobs)
    df.to_csv("C:/Users/Win 10 Pro/Desktop/JOB SKRAPER/jobs.csv", index=False)
    print("Job data saved to jobs.csv!")
else:
    print("No jobs found. Please check the website structure.")
