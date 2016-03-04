from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Email_Classify.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/','Email.views.login',name='login'),
    url(r'^logout/','Email.views.logout',name='logout'),
    url(r'^recieve/','Email.views.recieve',name='recieve'),
    url(r'^write/','Email.views.write',name='write'),
    url(r'^biz/','Email.views.biz',name='biz'),
    url(r'^world/','Email.views.world',name='world'),
    url(r'^send/','Email.views.send',name='send'),
    url(r'^sendOk/','Email.views.sendOk',name='sendOk'),
    url(r'^rubbish/','Email.views.rubbish',name='rubbish'),
    url(r'^pe/','Email.views.pe',name='pe'),
    url(r'^main/','Email.views.main',name='main'),
    url(r'^deleSendEail/(?P<parama>\d+)/$','Email.views.deleSendEail',name='deleSendEail'),
    url(r'^deleReceiverEail/(?P<parama>\d+)/$','Email.views.deleReceiverEail',name='deleReceiverEail'),
    url(r'^deleBizEail/(?P<parama>\d+)/$','Email.views.deleBizEail',name='deleBizEail'),
    url(r'^delePeEail/(?P<parama>\d+)/$','Email.views.delePeEail',name='delePeEail'),
    url(r'^deleRubbishEail/(?P<parama>\d+)/$','Email.views.deleRubbishEail',name='deleRubbishEail'),
    url(r'^deleWorldEail/(?P<parama>\d+)/$','Email.views.deleWorldEail',name='deleWorldEail'),
    url(r'^viewContext/(?P<parama>\d+)/$','Email.views.viewContext',name='viewContext'),
)
