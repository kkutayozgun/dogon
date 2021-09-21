
from django.urls import path
from page.views import (application_category_list, application_detail,
                        applications, blog, blog_category_list, blog_content, contact, home, aboutus, quality, kvkk_page)
from django.utils.translation import ugettext_lazy as _


urlpatterns = [
    path('', home, name='home'),
    path(_('hakkinda/'), aboutus, name='about'),
    path(_('iletisim/'), contact, name='contact'),
    path(_('uygulamalar/'), applications, name='applications'),
    path(_('uygulama-kategori/<slug>/'), application_category_list,
         name='application_category_list'),
    path(_('uygulamalar/<slug>/'), application_detail, name='application_detail'),
    path(_('kalite/'), quality, name='quality'),
    path(_('blog/'), blog, name='blog'),
    path(_('blog/<slug>/'), blog_content, name='blog_content'),
    path(_('blog-kategori/<slug>/'), blog_category_list, name='blog_category_list'),

    path(_('kvkk/'), kvkk_page, name='kvkk_page'),
]
