from datetime import datetime
import math

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]


IMPOST = 0.36
DAYTIME_IMPOST = 0.09
DAY = 6
NIGHT = 22


def calculate_price_call(inicial_call, end_call):
    inicial_call = datetime.fromtimestamp(inicial_call)
    end_call = datetime.fromtimestamp(end_call)

    if (inicial_call.hour >= NIGHT or end_call.hour < DAY):
        return IMPOST
    if (end_call.hour >= NIGHT):
        end_call = datetime(end_call.year, end_call.month, end_call.day, 22)

    if (inicial_call.hour < DAY):
        inicial_call = datetime(inicial_call.year, inicial_call.month, inicial_call.day, 6)
    time_call = math.floor((end_call - inicial_call).seconds / 60)
    final_price = (time_call * DAYTIME_IMPOST) + IMPOST

    return final_price


def classify_by_phone_number(records):
    new_records = []
    for record in records:
        aux = 0
        for new_record in new_records:

            if new_record['source'] == record['source']:
                aux = 1
                old_price = new_record['total']
                price = round(calculate_price_call(record['start'], record['end']), 2)
                new_price = round((old_price + price), 2)
                new_record['total'] = new_price

        if aux == 0:
            price_rounded = round(calculate_price_call(record['start'], record['end']), 2)
            new_records.append({'source': record['source'], 'total': price_rounded})
    final_records = sorted(new_records, key=lambda new_record: new_record['total'], reverse=True)
    return final_records


classify_by_phone_number(records)
