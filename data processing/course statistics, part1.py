import urllib.request
import json
def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    statistics = json.loads(data)
    for stats in statistics:
        print(stats["fullName"],stats["name"],stats["year"],stats["exercises"])
if __name__ == "__main__":
    retrieve_all()
