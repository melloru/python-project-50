from gendiff.formats.stylish import to_format as stylish_format
from gendiff.formats.json import to_format as json_format


FORMATS = {
    'stylish': stylish_format,
    'json': json_format,
}


def format_output(diff, style):
    style = FORMATS[style]
    return style(diff)
