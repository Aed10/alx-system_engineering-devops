#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    users = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(f"{users}/{id}").json()
    todos = f"{users}/{id}/todos"
    name = response.get("name")
    data = requests.get(todos).json()

    total_tasks = len(data)
    completed = [task for task in data if task.get("completed")]
    print(
        f"Employee {name} is done with tasks({len(completed)}/{total_tasks})"
    )
    for task in completed:
        print("\t {}".format(task.get("title")))
