from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.MsgeView.as_view(), name='index'),
    url(r'^greetings/$', views.MsgeSuccView.as_view(), name='greetings'),
    url(r'^show/$', views.MsgeShowView.as_view(), name='show'),
    url(r'^comments/$', views.MsgeModeView.as_view(), name='comments'),
]
