from gendiff import generate_diff
import pytest


@pytest.mark.parametrize('file1, file2, result', [
    ('tests/fixtures/json/file1.json',
     'tests/fixtures/json/file2.json',
     'tests/fixtures/json/result_json')
])
def test_json(file1, file2, result):
    assert generate_diff(file1, file2) == open(result).read()
