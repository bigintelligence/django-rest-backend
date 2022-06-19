from csv import DictReader
from .serializers import InmuebleSerializer
import logging

logger = logging.getLogger(__name__)


def save_inmueble_on_db(inmueble_as_dic):
    """save an inmueble in db
    :inmueble dictionary representation of a model inmueble
    """
    try:
        serializer = InmuebleSerializer(data=inmueble_as_dic)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
    except Exception as e:
        logger.exception(e)
    return None


class CsvFileInmueblesSaver:
    """read a csv file and save each in a db
    :param path_filename: File to upload
    """
    def __init__(self, path_filename):
        self.path_filename = path_filename
        self.response = {'upload_state': 'Ok', 'saved_result': ''}
        self.data_saved = 0
        self.data_readed = 0
        self.data_list_of_dic = None

    def read_save_file(self):
        try:
            with open(self.path_filename, 'r', encoding='Latin-1') as file:
                self.data_list_of_dic = DictReader(file)
                self.__save_data()
            return self
        except Exception as e:
            logger.exception(e)
            self.response['upload_state'] = 'Error'
            self.response['saved_result'] = e.__str__()

    def __save_data(self):
        try:
            for row in self.data_list_of_dic:
                self.data_readed = self.data_readed + 1
                row_converted = self.csv_adapter_rowdic(row)
                if save_inmueble_on_db(row_converted):
                    self.data_saved = self.data_saved + 1
            self.response['saved_result'] = 'rows saved: {}/{}'.format(self.data_saved, self.data_readed)
            return self
        except Exception as e:
            logger.exception(e)
            self.response['upload_state'] = 'Error'
            self.response['saved_result'] = e.__str__()

    @staticmethod
    def csv_adapter_rowdic(row_dict):
        """Adapter for coordinates on csv file to set type to Point
        :row_dict csv row dic readed from file
        """
        row_dict['coordinates'] = {
            'type': 'Point',
            'coordinates': [float(coord) for coord in row_dict['coordinates'].split(',')]
        }
        return row_dict

