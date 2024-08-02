from django.urls import path

from .views import (index,
                    menu_view,
                    shikoyatlar_create,
                    ComplaintListView,
                    about,)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),

    path('menu/', menu_view, name='menu'),
    path('complaints/', shikoyatlar_create, name='complaints'),
    path('complaints_list/', ComplaintListView.as_view(), name='complaints_list'),
    path('about/', about, name='about'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
