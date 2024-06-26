from gendiff.formats.stylish import to_format as stylish_format
from gendiff.formats.plain import to_format as plain_format


FORMATS = {
    'stylish': stylish_format,
    'plain': plain_format,
}


def format_output(diff, style):
    style = FORMATS[style]
    return style(diff)
