from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from . import views

app_name = 'ner'

urlpatterns = [
    # Map the 'django.contrib.auth.views.login' view to the /login/ URL.
    # The additional parameters to the view are passed via the 3rd argument which is
    # a dictionary of various parameters like the name of the template to be
    # used by the view.
    url(r'^login/$', 'django.contrib.auth.views.login',
          {
           "template_name" : "ner/login.html",
          },
          name="login_ner"),
    # Map the 'django.contrib.auth.views.logout' view to the /logout/ URL.
    # Pass additional parameters to the view like the page to show after logout
    # via a dictionary used as the 3rd argument.
    url(r'^logout/$', 'django.contrib.auth.views.logout',
          {
            "next_page" : reverse_lazy('login_ner')
          }, name="logout_ner"),
    url(r'^workspace/$', views.workspace, name='workspace_ner'),
    url(r'^annotate_text/(?P<file_id>[a-zA-Z0-9_.-]+)/$', views.annotate_text, name='annotate_text'),
    url(r'^map_umls_terms/(?P<file_id>[a-zA-Z0-9_.-]+)/$', views.map_umls_terms, name='map_umls_terms'),
    url(r'^save_annotation/$', views.save_annotation, name='save_annotation'),
    url(r'^submit_annotation/$', views.submit_annotation, name='submit_annotation'),
    url(r'^annotation_jurisdiction/(?P<file_id>[a-zA-Z0-9_.-]+)/$', views.annotation_jurisdiction, name='annotation_jurisdiction'),
    url(r'^umls_lookup/$', views.umls_lookup, name='umls_lookup'),
    url(r'^umls_lookup_with_translation/$', views.umls_lookup_with_translation, name='umls_lookup_with_translation'),
    url(r'^save_umls_mapping/$', views.save_umls_mapping, name='save_umls_mapping'),
    url(r'^submit_umls_mapping/$', views.submit_umls_mapping, name='submit_umls_mapping'),
    url(r'^umls_jurisdiction/$', views.umls_jurisdiction, name='umls_jurisdiction'),
    url(r'^decide_umls_jurisdiction/$', views.decide_umls_jurisdiction, name='decide_umls_jurisdiction'),
    url(r'^umls_jurisdiction_edit/$', views.umls_jurisdiction_edit, name='umls_jurisdiction_edit'),
    
]