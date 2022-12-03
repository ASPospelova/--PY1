from pprint import pprint
import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimiter=',') -> list[dict]:
    with open(INPUT_FILE) as f:  # TODO реализовать конвертер из csv в json
        listik_for_dicts = []
        headers = [f.readline()]
        headers = headers[0].split(delimiter)
        headers[len(headers)-1] = headers[len(headers)-1][:-1]

        all_values = [f.read()]
        all_values = all_values[0].split()

        for i in range(len(all_values)):
            listik_with_values = all_values[i].split(delimiter)
            dict_ = {headers[i]: listik_with_values[i] for i in range(len(listik_with_values))}
            listik_for_dicts.append(dict_)
        return listik_for_dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4, ensure_ascii=False))
