import psycopg2
import pytest
from decimal import *

from src import *

@pytest.fixture()
def build_category():
    drop_all_tables(test_conn, test_cursor)
    category = Category()
    category.name = 'Taco Places'
    save(category, test_conn, test_cursor)

    yield

    drop_all_tables(test_conn, test_cursor)

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
@pytest.fixture()
def clean_tables():
    drop_all_tables(test_conn, test_cursor)
    yield

    drop_all_tables(test_conn, test_cursor)


def test_find_by_name(build_category):
    category = Category.find_by_name('Taco Places', test_cursor)
    assert category.name == 'Taco Places'

def test_find_or_create_by_creates_when_new_category(clean_tables):
    test_cursor.execute('SELECT COUNT(*) FROM categories;')
    begin_cat_num = test_cursor.fetchone()

    Category.find_or_create_by_name('Taco Places', test_conn, test_cursor)
    test_cursor.execute('SELECT COUNT(*) FROM categories;')
    end_cat_num = test_cursor.fetchone()
    assert end_cat_num[0] == begin_cat_num[0] + 1


def test_find_or_create_by_finds_when_existing_category(clean_tables):
    category = Category()
    category.name = 'Taco Places'
    save(category, test_conn, test_cursor)

    test_cursor.execute('SELECT COUNT(*) FROM categories;')
    begin_cat_num = test_cursor.fetchone()

    Category.find_or_create_by_name('Taco Places', test_conn, test_cursor)
    test_cursor.execute('SELECT COUNT(*) FROM categories;')
    end_cat_num = test_cursor.fetchone()
    assert end_cat_num == begin_cat_num

