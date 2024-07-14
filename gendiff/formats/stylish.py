def to_str(value, depth):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value == '':
        return ''
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        result = []
        for k, v in value.items():
            result.append(f'{k}: {to_str(v, depth + 4)}')
        result = f'\n{" " * (depth + 4)}'.join(result)
        return f'{{\n{" " * (depth + 4)}{result}\n{" " * depth}}}'
    return value


def transformation(diff, depth=4):

    res = []

    for key, (status, value) in diff.items():
        def add(v, symbol):
            res.append(
                f'{" " * (depth - 2)}{symbol} {key}: {to_str(v, depth)}'
            )

        if status == 'DICT':
            res.append(
                f'{depth * " "}{key}: '
                f'{{\n{transformation(value, depth + 4)}\n{" " * depth}}}'
            )
        elif status == 'ADDED':
            add(value, '+')
        elif status == 'REMOVED':
            add(value, '-')
        elif status == 'UPDATED':
            old, new = value
            add(old, '-')
            add(new, '+')
        else:
            add(value, ' ')

    return '\n'.join(res)


def to_format(diff):
    return '{\n' + transformation(diff) + '\n}'
