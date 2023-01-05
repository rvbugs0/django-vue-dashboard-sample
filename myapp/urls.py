from django.urls import include, path
from . import views
from .views import *


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('table_view', table_view ),
    path('chart_view', chart_view ),
    path('index',index_view),
    path('', table_view )
]