import connexion
import six

from TimeSeriesIoT import util


def allrecords_get():  # noqa: E501
    """Retourne toutes les captures des capteurs

    Optional extended description in CommonMark or HTML. # noqa: E501


    :rtype: List[int]
    """
    return 'do some magic!'


def last_sensor_id_get(sensor_id):  # noqa: E501
    """Calculer la dernière valeur

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param sensor_id: String Id of the sensor to get
    :type sensor_id: str

    :rtype: List[int]
    """
    return 'do some magic!'


def mean_sensor_id_get(sensor_id, start_date=None, end_date=None):  # noqa: E501
    """Calculer la moyenne d&#x27;un capteur entre deux dates

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param sensor_id: String Id of the sensor to get
    :type sensor_id: str
    :param start_date: Integer/timestamp of the start date
    :type start_date: int
    :param end_date: Integer/timestamp of the end date
    :type end_date: int

    :rtype: List[int]
    """
    return 'do some magic!'


def min_sensor_id_get(sensor_id, start_date=None, end_date=None):  # noqa: E501
    """Calculer la valeur minimale d&#x27;un capteur entre deux dates

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param sensor_id: String Id of the sensor to get
    :type sensor_id: str
    :param start_date: Integer/timestamp of the start date
    :type start_date: int
    :param end_date: Integer/timestamp of the end date
    :type end_date: int

    :rtype: List[int]
    """
    return 'do some magic!'
