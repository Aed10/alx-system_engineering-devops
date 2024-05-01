#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """
import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    users = "https://jsonplaceholder.typicode.com/users"
    todos = f"{users}/{id}/todos"
    response = requests.get(f"{users}/{id}").json()
    name = response.get("username")
    data = requests.get(todos).json()

    with open(f"{id}.csv", "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in data:
            writer.writerow(
                [id, name, task.get("completed"), task.get("title")]
            )
