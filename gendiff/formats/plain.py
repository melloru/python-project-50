def to_str(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return "[complex value]"
    return f"'{value}'"


def join_path(path, key):
    return '.'.join([*path, key])


def format(diff, path):
    res = []

    for key, (status, value) in diff.items():
        if status == 'DICT':
            res.append(format(value, [*path, key])
                       )
        elif status == 'ADDED':
            res.append(f'Property {join_path(path, key)} '
                       f'was added with value: {to_str(value)}')
        elif status == 'REMOVED':
            res.append(f'Property {join_path(path, key)} was removed')
        elif status == 'UPDATED':
            old, new = value
            res.append(f'Property {join_path(path, key)} '
                       f'was updated. From {to_str(old)} to {to_str(new)}')
        else:
            res.append(f'Property {join_path(path, key)} value was unchanged')

    return '\n'.join(res)


def to_format(diff):
    return format(diff, [])
