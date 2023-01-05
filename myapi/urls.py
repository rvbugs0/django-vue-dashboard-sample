from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register('get_all_records',views.get_all_records)

# router.register('weather_info', views.WeatherInfoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get_all_records',views.get_all_records),
    path('get_by_range',views.get_by_range),
    path('insert_record',views.insert_record),
    path('get_average_temperatures',views.get_average_temperatures)



]