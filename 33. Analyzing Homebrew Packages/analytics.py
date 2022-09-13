import requests
import json
import time

r = requests.get("https://formulae.brew.sh/api/formula.json")
packages_json = r.json()

results = []
# timing the loop
t1 = time.perf_counter()  # a way to get accurate timings in python 

for package in packages_json:
    package_name = package["name"]
    package_desc = package["desc"]

    package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"

    r = requests.get(package_url)
    package_json = r.json()

    # get the installs_on_request for 30, 90 and 365 days
    installs_30 = package_json["analytics"]["install_on_request"]["30d"][package_name]
    installs_90 = package_json["analytics"]["install_on_request"]["90d"][package_name]
    installs_365 = package_json["analytics"]["install_on_request"]["365d"][package_name]

    data = {
        "name": package_name,
        "desc": package_desc,
        "analytics": {
            "30d": installs_30,
            "90d": installs_90,
            "365": installs_365
        }
    }

    results.append(data)

    # sleep for the amount of time it took to get the response
    time.sleep(r.elapsed.total_seconds())

    print(f"Got the {package_name} in {r.elapsed.total_seconds()} seconds")


t2 = time.perf_counter()
print(f"Finished in {t2-t1} seconds")

with open("package_info.json", "w") as file:
    json.dump(results, file, indent=2)