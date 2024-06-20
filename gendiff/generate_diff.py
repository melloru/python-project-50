import json
import yaml
from gendiff.formats.formats import format_output


def open_file(file):
    if file.endswith('json'):
        return json.load(open(file))
    return yaml.load(open(file), Loader=yaml.FullLoader)


def is_bool(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def create_diff(file1, file2):

    diff = {}
    keys = sorted(file1.keys() | file2.keys())
    for key in keys:
        if (isinstance(file1.get(key), dict)
                and isinstance(file2.get(key), dict)):
            diff[f'  {key}'] = create_diff(file1[key], file2[key])
        elif key not in file1:
            diff[f'+ {key}'] = is_bool(file2[key])
        elif key not in file2:
            diff[f'- {key}'] = is_bool(file1[key])
        elif file1.get(key) != file2.get(key):
            diff[f'- {key}'] = is_bool(file1[key])
            diff[f'+ {key}'] = is_bool(file2[key])
        else:
            diff[f'  {key}'] = is_bool(file1[key])
    return diff


def generate_diff(file_path1, file_path2, format='stylish'):
    file1 = open_file(file_path1)
    file2 = open_file(file_path2)

    diff = create_diff(file1, file2)

    return format_output(diff, format)
