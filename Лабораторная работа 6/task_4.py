from pprint import pprint
import json

INPUT_FILE = "input.csv"
count_dicts = 4
def csv_to_list_dict(filename='') -> list[dict]:
    with open(INPUT_FILE) as f:  # TODO реализовать конвертер из csv в json
        listik_for_dicts = []
        headers = [f.readline()]
        headers = headers[0].split(',')
        headers[len(headers)-1]=headers[len(headers)-1][:-1]

        all_values = [f.read()]
        all_values = all_values[0].split()
        all_values.extend(all_values)

        listik_for_dicts_1 = all_values[0].split(',')
        listik_for_dicts_2 = all_values[1].split(',')
        listik_for_dicts_3 = all_values[2].split(',')
        listik_for_dicts_4 = all_values[3].split(',')

        dic1 = {headers[i]: listik_for_dicts_1[i] for i in range(0, len(listik_for_dicts_1))}
        dic2 = {headers[i]: listik_for_dicts_2[i] for i in range(0, len(listik_for_dicts_2))}
        dic3 = {headers[i]: listik_for_dicts_3[i] for i in range(0, len(listik_for_dicts_3))}
        dic4 = {headers[i]: listik_for_dicts_4[i] for i in range(0, len(listik_for_dicts_4))}
        listik_for_dicts.append(dic1)
        listik_for_dicts.append(dic2)
        listik_for_dicts.append(dic3)
        listik_for_dicts.append(dic4)
    return listik_for_dicts

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4, ensure_ascii=False))
