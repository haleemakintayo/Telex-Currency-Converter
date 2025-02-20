
from django.urls import path

from api.views import convert_currency_view



urlpatterns = [
    path('convert/', convert_currency_view, name='telex_convert'),

]
