import os
import subprocess
import random
from datetime import datetime, timedelta

start_date = datetime(2025, 1, 5)
end_date = datetime(2025, 1, 20)
total_commits = 20

# List of files to slightly touch in each commit
files_to_touch = [
    "EDA_Regional_Sales_Analysis.ipynb",
    "PPT --- Regional Sales Analysis.pptx",
    "README.md",
    "Regional Sales Dataset.xlsx",
    "SALES REPORT.pbix",
    "Sales_data(EDA Exported).csv"
]

for i in range(total_commits):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    commit_date = start_date + timedelta(days=random_days)
    formatted_date = commit_date.strftime("%Y-%m-%dT%H:%M:%S")

    # Modify all files slightly by appending a space or comment (without breaking content)
    for file in files_to_touch:
        if file.endswith(".md"):
            with open(file, "a") as f:
                f.write(f"\n<!-- commit {i+1} -->\n")
        elif file.endswith(".ipynb") or file.endswith(".csv"):
            with open(file, "a") as f:
                f.write(f"# Commit {i+1}\n")
        elif file.endswith(".pptx") or file.endswith(".xlsx") or file.endswith(".pbix"):
            with open(file, "ab") as f:
                f.write(b" ")  # Binary append a space

    # Add a log for tracking
    with open("commit_log.txt", "a") as f:
        f.write(f"Commit #{i + 1} on {formatted_date}\n")

    subprocess.run(["git", "add", "."], check=True)
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = formatted_date
    env["GIT_COMMITTER_DATE"] = formatted_date
    subprocess.run(["git", "commit", "-m", f"Commit #{i + 1}"], env=env, check=True)

print("✅ All commits done with fake history across all files.")
