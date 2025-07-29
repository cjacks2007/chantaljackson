
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load US dataset
us_jobs = pd.read_csv('us_job_market_trend_analysis.csv')
us_jobs['Date_Posted'] = pd.to_datetime(us_jobs['Date_Posted'])

# Set seaborn style
sns.set(style="whitegrid")

# 1. Most In-Demand Job Titles
plt.figure(figsize=(10, 6))
job_counts = us_jobs['Job_Title'].value_counts()
sns.barplot(x=job_counts.values, y=job_counts.index, palette='Blues_d')
plt.title('Most In-Demand Job Titles (US)')
plt.xlabel('Number of Listings')
plt.ylabel('Job Title')
plt.tight_layout()
plt.savefig('us_job_titles_demand.png')
plt.close()

# 2. Average Salary by Job Title
plt.figure(figsize=(10, 6))
avg_salary = us_jobs.groupby('Job_Title')['Salary'].mean().sort_values()
sns.barplot(x=avg_salary.values, y=avg_salary.index, palette='Oranges')
plt.title('Average Salary by Job Title (US)')
plt.xlabel('Average Salary (USD)')
plt.ylabel('Job Title')
plt.tight_layout()
plt.savefig('us_avg_salary_by_title.png')
plt.close()

# 3. Job Listings by Location
plt.figure(figsize=(8, 5))
loc_counts = us_jobs['Location'].value_counts()
sns.barplot(x=loc_counts.index, y=loc_counts.values, palette='Purples')
plt.title('Job Listings by Location (US)')
plt.xlabel('Location')
plt.ylabel('Number of Listings')
plt.tight_layout()
plt.savefig('us_job_listings_by_location.png')
plt.close()

# 4. Job Postings Over Time
plt.figure(figsize=(10, 5))
job_trend = us_jobs.groupby(us_jobs['Date_Posted'].dt.to_period('W')).size()
job_trend.index = job_trend.index.to_timestamp()
job_trend.plot(marker='o', color='darkred')
plt.title('Job Postings Over Time (US)')
plt.xlabel('Week')
plt.ylabel('Number of Postings')
plt.grid(True)
plt.tight_layout()
plt.savefig('us_job_posting_trends.png')
plt.close()
