from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import HomeView, ImportDataView, DeleteProjectView, ProjectView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^import-data$', ImportDataView.as_view(), name='import_data'),
    url(r'^project/delete$', login_required(DeleteProjectView.as_view()), name='delete_project'),
    url(r'^project/(?P<project_id>\d+)/$', login_required(ProjectView.as_view()), name='project_view')
]

