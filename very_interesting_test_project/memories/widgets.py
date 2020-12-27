from django.conf import settings
from django.forms import widgets


class GoogleMapsAddressWidget(widgets.TextInput):
    """a widget that will place a google map right after the #id_address field"""
    template_name = "widgets/map_widget.html"

    class Media:
        css = {
            'all': (settings.STATIC_URL +
                    'css/google-maps.css',)
        }
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
            'https://maps.google.com/maps/api/js?key={}&libraries=places'.format(
                settings.GOOGLE_MAPS_API_KEY),
            settings.STATIC_URL + 'js/google-maps.js',
        )
