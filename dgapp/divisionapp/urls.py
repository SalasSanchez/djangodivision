from django.conf.urls import url
from divisionapp import views


urlpatterns = [
    url(r'^$', views.new_division),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^division/$', views.new_division),
]