from src.orm import *
from src.db_utilities import *

class Venue():
    __table__ = 'venues'
    columns = ['id', 'foursquare_id', 'name', 'price',
            'rating', 'likes', 'menu_url']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in columns: {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find_by_foursquare_id(self, foursquare_id, test_cursor):
        test_cursor.execute(
            "SELECT * FROM venues WHERE foursquare_id = '%s'" % foursquare_id)
        record = test_cursor.fetchone()
        venue = build_from_record(self, record)

        return venue
