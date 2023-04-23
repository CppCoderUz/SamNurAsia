

from django.urls import path
from api import views


urlpatterns = [
    path('eslatma', views.eslatma_api),
    path('icon', views.icon_api),
    path('manzil', views.manzil_api),
    path('maqola_joylash', views.maqola_joylash_api),
    path('narxlar', views.narxlar_api),
    path('tarmoqlar', views.IjtimoiyTarmoqlarAPI.as_view()),

    # postlar
    path('post/all', views.PostAllAPI.as_view()),
    path('post/detail/<int:pk>', views.PostDetailAPI.as_view()),

    # Jurnal
    path('journal/all', views.JournalAllAPI.as_view()),
    path('journal/detail/<int:pk>', views.JournalDetailAPI.as_view()),

    # col
    path('col/all', views.ArticleColumnAllAPI.as_view()),
    path('col/detail/<int:pk>', views.ArticleColumnDetailAPI.as_view()),

    # maqola
    path('article/all', views.ArticleALLAPI.as_view()),
    path('article/detail/<int:pk>', views.ArticleDetailAPI.as_view()),
]