# -*- coding: utf-8 -*-

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load NominatimFilterPlugin class from file nominatimfilter.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .osplaces_geocoder import OSPlacesGeocoderPlugin
    return OSPlacesGeocoderPlugin(iface)
