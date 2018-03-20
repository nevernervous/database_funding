from django.conf.urls import url

from .views import HomeView, ImportDataView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^import-data$', ImportDataView.as_view(), name='import_data')
]

