# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.views.decorators.csrf import csrf_exempt
from collector.views import StatusView, RecordApiView
from notifier.views import AlertListView, NewAlertView, EditAlertView, DeleteAlertView

urlpatterns = [
    # TODO: refactor api to utilize DRF..csrf_exempt - FOR TESTING ONLY
    url(r'^api/record/$', csrf_exempt(RecordApiView.as_view()), name='record-data'),
    url(r'^home/$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^alerts/new/$', NewAlertView.as_view(), name='alerts-new'),
    url(r'^alerts/(?P<pk>\d+)/edit/$', EditAlertView.as_view(), name='alerts-edit'),
    url(r'^alerts/(?P<pk>\d+)/delete/$', DeleteAlertView.as_view(), name='alerts-delete'),
    url(r'^alerts/$', AlertListView.as_view(), name='alerts-list'),
    url(r'^$', StatusView.as_view(), name='status'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include('djangios.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
