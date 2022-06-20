import os
import pytest
from django.conf import settings
from .utils import save_inmueble_on_db, CsvFileInmueblesSaver


@pytest.mark.django_db
class TestUtils:
    def test_save_inmueble_on_db(self):
        """test for save one row in DB"""
        inmueble = {
            'build_status': 1,
            'is_active': False,
            'start_month': 19212,
            'construction_type': 2,
            'date_diff': 0,
            'description': 'test',
            'date_in': '2020-06-29T00:00:00.000Z',
            'property_type': 2,
            'end_week': 15188,
            'typology_type': 2,
            'coordinates': {
                'type': 'Point',
                'coordinates': [43.53820000000000334239302901551127433777, -5.6673400000000002663114173628855496645]
            },
            'boundary_id': 75666,
            'id_uda': '27-99196812134_515750',
            'title': 'test',
            'listing_type': 1,
            'date_out': '2020-06-30T00:00:00.000Z',
            'start_week': 15136,
            'end_quarter': 82,
            'last_activity': 326,
            'start_quarter': 78,
            'end_month': 19213
        }
        result = save_inmueble_on_db(inmueble)
        print(result)
        assert result['id_uda'] == '27-99196812134_515750'

    def test_save_csvfile_on_db(self):
        """test for save the csv file assets.csv in DB"""
        file_path = os.path.join(settings.BASE_DIR, 'assets.csv')
        csv_saver = CsvFileInmueblesSaver(file_path)
        csv_saver.read_save_file()
        print(csv_saver.response)
        assert csv_saver.response['upload_state'] == 'Ok'

