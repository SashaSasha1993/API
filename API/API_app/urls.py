from django.conf.urls import url
from .import views


urlpatterns = [
    # url(r'^$', BooksList.as_view(), name="Books"),
    url(r'^$', views.ListCreateAccessoriesID.as_view(), name='A_ID_API'),
    url(r'^$', views.ListCreateAccessoriesDetails.as_view(), name='A_DETAILS_API'),


]