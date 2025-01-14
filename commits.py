import os
import subprocess
import random
from datetime import datetime, timedelta

# SETTINGS
start_date = datetime(2025, 1, 5)
end_date = datetime(2025, 1, 20)
total_commits = 20

# Create or modify a dummy file to track commits
filename = "commit_log.txt"

for i in range(total_commits):
    # Random date generation
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    commit_date = start_date + timedelta(days=random_days)
    formatted_date = commit_date.strftime("%Y-%m-%dT%H:%M:%S")

    # Write to file
    with open(filename, "a") as f:
        f.write(f"Commit #{i + 1} on {formatted_date}\n")

    # Git commands
    subprocess.run(["git", "add", "."], check=True)
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = formatted_date
    env["GIT_COMMITTER_DATE"] = formatted_date
    subprocess.run(["git", "commit", "-m", f"Commit #{i + 1}"], env=env, check=True)

print(f"✅ Successfully created {total_commits} commits from Jan 5 to Jan 20, 2025.")
