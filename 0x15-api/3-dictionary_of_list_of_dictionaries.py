#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """
import json
import requests
import sys

if __name__ == "__main__":
    users = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(users).json()
    data = {}
    for user in response:
        name = user.get("username")
        id = user.get("id")
        todos = f"{users}/{id}/todos"
        data[id] = [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": name,
            }
            for task in requests.get(todos).json()
        ]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
