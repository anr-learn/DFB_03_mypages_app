# my_pages_app/urls.py

from django.urls import path

from .views import MyHomePageView
from .views import MyAboutPageView

urlpatterns = [
	path("", MyHomePageView.as_view(),  name="home"),  # NOTE 'as_view()
	path("home/", MyHomePageView.as_view(),  name="home"),  # NOTE 'as_view()
	path("about/", MyAboutPageView.as_view(), name="about"),  # NOTE 'as_view()
	]

### end ###
