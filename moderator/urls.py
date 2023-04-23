

from django.urls import path

from moderator import views

urlpatterns = [
    # Avtorizatsiya
    path('', views.dashboard, name='dashboard'),
    path('profile/view', views.profile_view, name='profile_view'),
    path('profile/update', views.profile_update, name='profile_update'),
    path('auth/login', views.login_view, name='login'),
    path('auth/logout', views.logout_view, name='logout'),

    # maqolalar
    path('article/all', views.all_articles, name='all_article'),
    path('article/detail/<int:pk>', views.article_read, name='article_read'),
    path('article/archive/<int:pk>', views.article_archive, name='article_archive'),
    path('article/delete/<int:pk>', views.article_delete, name='article_delete'),
    path('article/change/<int:pk>', views.article_change, name='article_change'),
    
    # postlar
    path('post/all', views.all_posts, name='all_posts'),
    path('post/create', views.post_create, name='post_create'),
    path('post/update/<int:pk>', views.post_update, name='post_update'),
    path('post/delete/<int:pk>', views.post_delete, name='post_delete'),

    # Jurnallar
    path('journal/all', views.journal_all, name='journal_all'),
    path('journal/create', views.journal_create, name='journal_create'),
    path('journal/update/<int:pk>', views.journal_update, name='journal_update'),
    path('journal/delete/<int:pk>', views.journal_delete, name='journal_delete'),

    # Article columns
    path('col/all', views.article_col_all, name='article_col_all'),
    path('col/create', views.article_col_create, name='article_col_create'),
    path('col/update/<int:pk>', views.article_col_update, name='article_col_update'),
    path('col/delete/<int:pk>', views.article_col_delete, name='article_col_delete'),

    # Arizalar
    path('petition/all', views.petition_all, name='petition_all'),
    path('petition/detail/<int:pk>', views.petition_detail, name='petition_detail'),
    path('petition/access/<int:pk>', views.petition_access, name='petition_accesss'),
    path('petition/not_access/<int:pk>', views.petition_not_access, name='petition_not_access'),
    path('petition/warning/<int:pk>', views.petition_warning, name='petition_warning'),

    # moderatorlar
    path('moderator/all', views.moderator_all, name='moderator_all'),
    path('moderator/detail/<int:pk>', views.moderator_detail, name='moderator_detail'),
    path('moderator/add', views.moderator_add, name='moderator_add'),
]