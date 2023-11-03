# TODO решите задачу
import json


def task() -> float:
    with open("input.json", 'r') as f:
        json_data = json.load(f)
        summator = sum([value["score"] * value["weight"] for value in json_data])
        return round(summator, 3)

print(task())
