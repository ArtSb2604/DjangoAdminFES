from datetime import date
from datetime import timedelta

def graph_data():
    data = []
    today = date.today()
    for i in range(7):
        d = today - timedelta(days=i)
        if d.weekday() < 7:  # Here
            data.append(d)

    return data