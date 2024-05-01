#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    response = requests.get(f"{url}/users/{id}").json()
    name = response.get("name")
    data = requests.get(f"{url}/todos?userId={id}").json()

    total_tasks = len(data)
    completed = [task for task in data if task.get("completed")]
    print(
        f"Employee {name} is done with tasks({len(completed)}/{total_tasks})"
    )
    for task in completed:
        print("\t {}".format(task.get("title")))
