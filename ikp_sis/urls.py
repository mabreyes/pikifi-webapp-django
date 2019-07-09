from django.conf.urls import url
from django.urls import include, path

from . import views
from .users import editors, viewers, organization

urlpatterns = [
    url(r'^$', views.student_list, name='student_list'),
    url(r'^student/(?P<pk>\d+)/$', views.student_detail, name='student_detail'),
    url(r'^student/new/$', views.student_new, name='student_new'),
    url(r'^student/(?P<pk>\d+)/edit/$', views.student_edit, name='student_edit'),
    url(r'^student/(?P<pk>\d+)/delete/$',
        views.student_delete, name='student_delete'),
    path('accounts/settings/update_password/',
         views.change_password, name='change_password'),
    path('accounts/change_password/success/',
         views.password_changed, name='password_changed'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', organization.SignUpView.as_view(), name='signup'),
    path('accounts/signup/viewer/',
         viewers.ViewerSignUpView.as_view(), name='viewer_signup'),
    path('accounts/signup/editor/',
         editors.EditorSignUpView.as_view(), name='editor_signup'),
    path('accounts/signout/',
         views.signout_prompt, name='signout'),
]

handler404 = 'views.handler404'
handler500 = 'views.handler500'
