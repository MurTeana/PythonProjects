import pandas as pd
import json
from datetime import datetime

# Чтение CSV файла
csv_file_path = 'D:\\Coding\\PYTHON\\CSVtoJSON\\data\\csv\\Canada_16_11_23_sample.csv'
df = pd.read_csv(csv_file_path, sep='\t')
print(df.columns)

# Сопоставление столбцов CSV с полями в JSON
json_data = []
for index, row in df.iterrows():
    parcel = {
         "parcelType": "103",
         "parcels": [
             {
                "additionalServices": [
                    {"code": "DOB", "amount": 0.0},
                    {"code": "V", "amount": row.get("item-price")},
                    {"code": "ODK", "amount": row.get("item-tax")}
                ],
                "parcelNumber": "",
                "weight": "",
                "volume": 0.0,
                "cn23": None,
                "international": None,
                "parcelDate": ""
             }
         ],
        "commonServices": None,
        "addressee": {
            "addresseeName1": row.get("buyer-name", ""),
            "addresseeName2": "",
            "addresseeAddress": row.get("ship-address-1", ""),
            "addresseePostId": row.get("ship-postal-code", ""),
            "addresseePost": row.get("ship-city", ""),
            "addresseeCountryId": row.get("ship-country", ""),
            "addresseePhone": row.get("ship-phone-number", ""),
            "addresseeEmail": row.get("buyer-email", "")
        },
        "upn": None,
        "comment1": row["purchase-date"],
        "comment2": row["delivery-Instructions"],
        "recordNumber": row["order-item-id"]
    }

    json_data.append(parcel)

# Преобразование списка в JSON
json_result = json.dumps(json_data, indent=2, ensure_ascii=False)

# Сохранение JSON в файл
json_output_file_path = 'resultJSON.json'
with open(json_output_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_result)

print(f'Преобразование завершено. Результат сохранен в {json_output_file_path}')