import pytest

from src.collection_utils import list_max_index_value, list_min_index_value, dict_min_key_value, dict_max_key_value


@pytest.fixture
def initialize_dictionary():
    print('Init dict')
    return {
        'a': 10,
        'b': 9,
        'c': 2,
        'd': 40
    }


@pytest.fixture
def initialize_list():
    return [-55, -55, -7, 15, 2, 1, -7, 4]


def test_min_dictionary(initialize_dictionary):
    result = dict_min_key_value(initialize_dictionary)
    expected = 'c', 2
    assert result == expected


def test_max_dictionary(initialize_dictionary):
    result = dict_max_key_value(initialize_dictionary)
    expected = 'd', 40
    assert result == expected

def test_min_list(initialize_list):
    result = list_min_index_value(initialize_list)
    expected = [0, 1], -55
    assert result == expected
