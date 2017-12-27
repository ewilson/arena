from collections import namedtuple

import pytest

from . import util


def test_convert_dictionary_to_namedtuple():
    Person = namedtuple('Person', 'name,age')
    bob_dict = {'name': 'Bob', 'age': 55}

    bob_nt = util.row_to_namedtuple(Person, bob_dict)

    assert bob_nt.name == 'Bob'
    assert bob_nt.age == 55


def test_failed_conversion_missing_field():
    Person = namedtuple('Person', 'name,age')
    bob_dict = {'name': 'Bob'}

    with pytest.raises(KeyError):
        util.row_to_namedtuple(Person, bob_dict)
