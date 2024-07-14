from gendiff.generate_diff import generate_diff
import pytest


@pytest.mark.parametrize('file1, file2, result', [
    ('tests/fixtures/json/file1.json',
     'tests/fixtures/json/file2.json',
     'tests/fixtures/json/result1_json')
])
def test_json(file1, file2, result):
    assert generate_diff(file1, file2) == open(result).read()


@pytest.mark.parametrize('file1, file2, result', [
    ('tests/fixtures/yaml/file1.yaml',
     'tests/fixtures/yaml/file2.yaml',
     'tests/fixtures/yaml/result_yaml')
])
def test_yaml(file1, file2, result):
    assert generate_diff(file1, file2) == open(result).read()


@pytest.mark.parametrize('file1, file2, result', [
    ('tests/fixtures/json/file3.json',
     'tests/fixtures/json/file4.json',
     'tests/fixtures/json/result2_json')
])
def test_stylish(file1, file2, result):
    assert generate_diff(file1, file2) == open(result).read()
