#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    users = "https://jsonplaceholder.typicode.com/users"
    todos = f"{users}/{id}/todos"
    response = requests.get(f"{users}/{id}").json()
    name = response.get("username")
    data = requests.get(todos).json()

    with open(f"{id}.json", "w") as jsonfile:
        json.dump(
            {
                id: [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": name,
                    }
                    for task in data
                ]
            },
            jsonfile,
        )
    print(f"File saved as {id}.json")
    print(f"data: {type(data)}")
