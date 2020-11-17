import json
import csv
from datetime import datetime


results = {}

with open('results.json', 'r') as f:
    results = json.load(f)
    # print(results)

with open('results.csv', 'w') as f:
    writer = csv.DictWriter(f, delimiter=";", fieldnames=[
                            'id', 'time', 'caption'])

    writer.writeheader()

    for (k, v) in results.items():
        dt_object = datetime.fromtimestamp(v['time'])
        newtime = dt_object.strftime("%d/%m/%Y")

        writer.writerow({
            'id': v['id'],
            'time': newtime,
            'caption': v['caption'].strip().replace("\n", ""),
        })v