import pandas as pd
import json

# Чтение CSV файла
csv_file_path = 'D:\Coding\PYTHON\PythonProjects\CSVtoJSON\data\csv\Сanada_test_10_from 211123.csv'
df = pd.read_csv(csv_file_path, sep='\t')
# print(df.columns)
num = 1

# Сопоставление столбцов CSV с полями в JSON
json_data = []
for index, row in df.iterrows():
    parcel = {
        "RecordNumber": num,
        "ParcelType": 329,
        "Parcels": [
            {
                "ParcelNumber": "",
                "Weight": 0,  # 800
                "Volume": 0,
                "AdditionalServices": None,
                "International": {
                    "nonDeliveryInstruction": 1,  # (1 = return to sender, 2 = sender waives its claim to the parcel)
                    "categoryType": 5,  # 5 = sale of goods
                    "categoryExplanation": "",
                    "importerReference": "",
                    "importerPhone": str(row.get("ship-phone-number", "")),
                    "importerEmail": row.get("buyer-email", ""),
                    "comments": "",
                    "licence": "",
                    "certificate": "",
                    "invoice": "",
                    "codForeign": 0,
                    "codForeignCurrency": ""
                },
                "Cn23": [
                    {
                        "Content": row.get("product-name", ""),
                        "Quantity": row.get("quantity-purchased", ""),
                        "NetWeight": 0,  # 800
                        "Value": row.get("item-price", ""),
                        "Tariff": "18069011",  # check in the price
                        "CountryOfOrigin": "705"  # SI
                    }
                ]
            }
        ],
        "CommonServices": None,
        "Addressee": {
            "AddresseeName1": row.get("recipient-name", ""),
            "AddresseeName2": row.get("buyer-name", ""),
            "AddresseeAddress": row.get("ship-address-1", ""),
            "AddresseePostId": row.get("ship-postal-code", ""),
            "AddresseePost": row.get("ship-city", ""),
            "AddresseeCountryId": "124",  # for Canada
            "AddresseeCountryAreaId": "",
            "AddresseePhone": str(row.get("ship-phone-number", "")),
            "AddresseeEmail": row.get("buyer-email", "")
        },
        "Upn": None,
        "Comment1": "",
        "Comment2": ""
    }
    num = num + 1

    json_data.append(parcel)

# Преобразование списка в JSON
json_result = json.dumps(json_data, indent=2, ensure_ascii=False)

# Сохранение JSON в файл
json_output_file_path = 'resultJSON.json'
with open(json_output_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_result)

print(f'Преобразование завершено. Результат сохранен в {json_output_file_path}')
