from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'main/$',views.main,name="main_controller"),
    url(r'^provided/$',views.provided,name="List_provided"),
    url(r'^returned/$',views.returned,name="returned_components"),
    url(r'^CreateProvide/$',views.CreateProvide,name="Create_provided"),
    url(r'^DeleteProvide/(?P<pk>[0-9]+)/$',views.DeleteProvide,name="Delete_provided"),
    url(r'^CreateComponent/$', views.CreateComponent.as_view(), name="Create_component"),
    url('^UpdateComponent/(?P<pk>[0-9]+)/$',views.UpdateComponent.as_view(),name="Update_component"),
    url(r'^DeleteComponent/(?P<pk>[0-9]+)/$', views.DeleteComponent, name="Delete_component"),
    url(r'^email/(?P<pk>[0-9]+)/$',views.reminder,name="reminder"),
    url(r'^pdf_provided/$',views.PDF_provided.as_view(),name="download_provided"),
    url(r'^pdf_returned/$',views.PDF_returned.as_view(),name="download_returned"),
    url(r'components/$', views.List_component, name="List_component"),
]