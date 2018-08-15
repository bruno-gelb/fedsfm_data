import json

from data import gather

if __name__ == "__main__":
    data = gather()
    
    with open("data.json", "w") as f:
        json.dump(data, f, ensure_ascii=False)
