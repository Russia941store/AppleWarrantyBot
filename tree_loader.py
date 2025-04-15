import os
import json

def load_tree():
    file_path = os.path.join(os.path.dirname(__file__), "decision_tree.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)