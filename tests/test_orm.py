import pytest
from decimal import *
from src import *

@pytest.fixture()
def build_categories():
    drop_all_tables(test_conn, test_cursor)
    category = Category()
    category.name = 'Taco Places'
    save(category, test_conn, test_cursor)

    category = Category()
    category.name = 'Asian Fusion'
    save(category, test_conn, test_cursor)
    yield

    drop_all_tables(test_conn, test_cursor)

def test_find_all(build_categories):
    categories = find_all(Category, test_cursor)
    assert [category.name for category in categories] == ['Taco Places', 'Asian Fusion']
