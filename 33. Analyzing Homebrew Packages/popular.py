import json

def install_sort(package):
    return package["analytics"]["30d"]

with open("package_info.json", "r") as file:
    data = json.load(file)

# data = [item for item in data if "video" in item["desc"]]

data.sort(key=install_sort, reverse=True)  # reverse, to sort from top down

data_str = json.dumps(data[:5], indent=2)
# use list slicing to access up to the 5th item
print(data_str)