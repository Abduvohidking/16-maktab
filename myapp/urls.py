from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path ,include
from .views import ListViews, CreateViews, DetailViews, DeleteViews, EmployeeUpdate, AudioCreateViews, AudioUpdate, \
    AudioDetailViews, Book, AudioBook, search_result, AudioDeleteViews, register, create

urlpatterns = [
    path('', ListViews.as_view(),name='home'),
    path('create/', CreateViews.as_view(),name='create'),
    path('create/audio/', AudioCreateViews.as_view(),name='audio'),
    path('detail/<slug:slug>',DetailViews.as_view(),name='detail'),
    path('search/', search_result, name='search_result'),
    path('detail/audio/<slug:slug>',AudioDetailViews.as_view(),name='detail_audio'),
    path('delete/<slug:slug>',DeleteViews.as_view(),name='delete'),
    path('delete/audio/<slug:slug>',AudioDeleteViews.as_view(),name='delete_audio'),
    path('update/<slug:slug>',EmployeeUpdate.as_view(),name='update'),
    path('update/audio/<slug:slug>',AudioUpdate.as_view(),name='audio_date'),
    path('book/',Book.as_view(),name='book'),
    path('audio/',AudioBook.as_view(),name='jasur'),
    path('register/',register,name='register'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)