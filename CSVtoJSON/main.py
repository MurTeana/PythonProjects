import pandas as pd
import json

# Чтение CSV файла
csv_file_path = 'D:\Coding\PYTHON\PythonProjects\CSVtoJSON\data\csv\Canada_16_11_23_sample.csv'
df = pd.read_csv(csv_file_path, sep='\t')
print(df.columns)

# Сопоставление столбцов CSV с полями в JSON
json_data = []
for index, row in df.iterrows():
    parcel = {
        "parcelType": 103,
        "parcels": [{
            "parcelNumber": row.get("order-item-id"),
            "weight": None,
            "volume": None,
            "additionalServices": [
                {"code": "ODK", "amount": None},
                {"code": "V", "amount": row.get("item-price")},
                {"code": "PR", "amount": None}],
            "cn23": None,
            "international": {
                "nonDeliveryInstruction": 1,  # (1 = return to sender, 2 = sender waives its claim to the parcel)
                "categoryType": 5,  # 5 = sale of goods
                "categoryExplanation": None,
                "importer": None,
                "importerPhone": None,
                "importerEmail": None,
                "comments": None,
                "license": None,
                "certificate": None,
                "invoice": None,
                "codForeign": None,
                "codForeignCurrency": row.get("currency")
            },
            "parcelContent": 1  # for goods (1) or documents (0).
        }],
        "commonServices": None,
        "addressee": {
            "addresseeName1": row.get("recipient-name", ""),
            "addresseeName2": row.get("buyer-name", ""),
            "addresseeAddress": row.get("ship-address-1"),
            "addresseePostId": row.get("ship-postal-code"),
            "addresseePost": row.get("ship-city"),
            "addresseeCountryId": "124",  # for Canada
            "addresseePhone": row.get("ship-phone-number"),
            "addresseeEmail": row.get("buyer-email")
        },
        "upn": None,
        "comment1": row.get("ship-state"),
        "comment2": row.get("sku"),
        "recordNumber": row.get("order-id")
    }

    json_data.append(parcel)

# Преобразование списка в JSON
json_result = json.dumps(json_data, indent=2, ensure_ascii=False)

# Сохранение JSON в файл
json_output_file_path = 'resultJSON.json'
with open(json_output_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_result)

print(f'Преобразование завершено. Результат сохранен в {json_output_file_path}')
