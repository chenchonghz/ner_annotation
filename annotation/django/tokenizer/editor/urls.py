from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from . import views

app_name = 'editor'

urlpatterns = [
    url(r'^tokenize_text/(?P<file_id>[a-zA-Z0-9_.-]+)/(?P<file_copy>[a-zA-Z0-9_.-]+)$', views.tokenize_text, name='tokenize_text'),
    url(r'^jurisdiction/(?P<file_id>[a-zA-Z0-9_.-]+)/$', views.jurisdiction, name='jurisdiction'),
    url(r'^workspace/$', views.workspace, name='workspace_editor'),
    url(r'^workspace_root/$', views.workspace_root, name='workspace_root'),
    url(r'^admin_overview/$', views.admin_overview, name='admin_overview'),
    url(r'^instruction/$', views.instruction, name='instruction'),
    url(r'^save_tokenized/$', views.save_tokenized, name='save_tokenized'),
    url(r'^submit_tokenized/$', views.submit_tokenized, name='submit_tokenized'),

    # Map the 'django.contrib.auth.views.login' view to the /login/ URL.
    # The additional parameters to the view are passed via the 3rd argument which is
    # a dictionary of various parameters like the name of the template to be
    # used by the view.
    url(r'^login/$', 'django.contrib.auth.views.login',
          {
           "template_name" : "editor/login.html",
          },
          name="login_editor"),
          
    # Map the 'django.contrib.auth.views.logout' view to the /logout/ URL.
    # Pass additional parameters to the view like the page to show after logout
    # via a dictionary used as the 3rd argument.
    url(r'^logout/$', 'django.contrib.auth.views.logout',
          {
            "next_page" : reverse_lazy('login_editor')
          }, name="logout_editor"),
]