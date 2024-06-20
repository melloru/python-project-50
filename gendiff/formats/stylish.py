import itertools


def to_format(diff, replacer=' ', spaces_count=4):

    def walk(diff, depth):
        res = []

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth

        for key, value in diff.items():
            if isinstance(value, dict):
                res.append(f'{deep_indent}{key}: '
                           f'{walk(value, deep_indent_size)}'
                           )
            else:
                res.append(f'{deep_indent}{key}: {value}')

        result = itertools.chain("{", res, [current_indent + "}"])
        return '\n'.join(result)

    return walk(diff, 0)
