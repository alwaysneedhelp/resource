from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import ArticleDetailView, ResearchDetailView, articles_list, researches_list, home, about, categories_page, search


urlpatterns = [
    path('', home, name='home'),
    path('articles/', articles_list, name='articles_list'),
    path('researches/', researches_list, name='researches_list'),
    path('about/', about, name='about'),
    path('search/', search, name='search'),  # Add this line for search
    path('categories/', categories_page, name='categories_page'),  # Add this line
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('research/<slug:slug>/', ResearchDetailView.as_view(), name='research_detail'),
    path('user/', include('userauths.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)