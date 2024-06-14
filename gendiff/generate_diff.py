import json
import yaml


def is_bool(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value
def open_file(file):
    if file.endswith('json'):
        return json.load(open(file))
    return yaml.load(open(file), Loader=yaml.FullLoader)

def generate_diff(file_path1, file_path2):
    diff = []
    file1 = open_file(file_path1)
    file2 = open_file(file_path2)
    for key in sorted(set(file1.keys() | file2.keys())):

        if key not in file1:
            diff.append(f'  + {key}: {is_bool(file2[key])}')
        elif file1.get(key) and file2.get(key):
            if file1[key] != file2[key]:
                diff.append(f'  - {key}: {is_bool(file1[key])}')
                diff.append(f'  + {key}: {is_bool(file2[key])}')
            else:
                diff.append(f'    {key}: {is_bool(file1[key])}')
        else:
            diff.append(f'  - {key}: {is_bool(file1[key])}')
    return "{\n" + "\n".join(diff) + "\n}"
