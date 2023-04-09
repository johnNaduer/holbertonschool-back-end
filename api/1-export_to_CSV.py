#!/usr/bin/python3
"""Using what you did in the task #0, extend your
Python script to export data in the CSV format"""

import json
import csv

# Set the user ID to extract data for
user_id = "123"

# Load the JSON data
with open("tasks.json", "r") as f:
    data = json.load(f)

# Filter the data to only include tasks for the specified user ID
user_tasks = [task for task in data if task["userId"] == user_id]

# Write the data to a CSV file
filename = f"{user_id}.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    for task in user_tasks:
        completed_status = "completed" if task["completed"] else "incomplete"
        writer.writerow([task["userId"], task["username"], completed_status, task["title"]])

print(f"Data written to {filename}")
