import urllib.request
import json


def retrieve_all(course_name: str):
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"

    with urllib.request.urlopen(url) as my_request:
        my_data = my_request.read()
        statistics = json.loads(my_data)
        for stat in statistics:
            print(stat)


if __name__ == "__main__":
    retrieve_all("docker2019")
