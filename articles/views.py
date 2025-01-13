from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article, Category, Research, Member  # Import Research
from bs4 import BeautifulSoup
from django.views import View
from django.shortcuts import get_object_or_404

def about(request):
    members = Member.objects.all()
    print(members)  # Debugging line
    return render(request, 'about.html', {'members': members})

def articles_list(request):
    articles = Article.objects.all()  # Fetch all articles initially
    
    # Sorting logic
    sort_option = request.GET.get('sort')
    if sort_option == 'az':
        articles = articles.order_by('title')  # A to Z
    elif sort_option == 'za':
        articles = articles.order_by('-title')  # Z to A
    elif sort_option == 'first':
        articles = articles.order_by('published_date')  # First ones
    elif sort_option == 'last':
        articles = articles.order_by('-published_date')  # Last ones

    paginator = Paginator(articles, 3)  # Show 3 articles per page
    page_number = request.GET.get('page')
    articles_page = paginator.get_page(page_number)
    return render(request, 'articles/articles_list.html', {'articles': articles_page, 'request': request})

def researches_list(request):
    researches = Research.objects.all()
    return render(request, 'researches/researches_list.html', {'researches': researches})

def get_popular_articles():
    return Article.objects.order_by('-views')[:5]  # Get top 5 articles by views

def get_popular_researches():
    return Research.objects.order_by('-views')[:5]  # Get top 5 researches by views

def search(request):
    query = request.GET.get('q', '')
    articles = Article.objects.filter(title__icontains=query)  # Search in articles
    researches = Research.objects.filter(title__icontains=query)  # Search in researches

    return render(request, 'search_results.html', {
        'query': query,
        'articles': articles,
        'researches': researches,
    })

def home(request):
    latest_articles = Article.objects.order_by('-published_date')[:3]  # Fetch latest 3 articles
    latest_researches = Research.objects.order_by('-published_date')[:4]  # Fetch latest researches
    popular_articles = get_popular_articles()
    popular_researches = get_popular_researches()
    categories = Category.objects.all()

    # Extract plain text for latest articles
    for article in latest_articles:
        soup = BeautifulSoup(article.content, 'html.parser')
        article.plain_text = soup.get_text(strip=True)

    # No need to extract plain text from research as it has a file
    for research in latest_researches:
        research.plain_text = "Content file available for download."  # Placeholder text

    return render(request, 'base.html', {
        'latest_articles': latest_articles,
        'latest_researches': latest_researches,
        'categories': categories,
        'popular_articles': popular_articles,
        'popular_researches': popular_researches,
    })

def categories_page(request):
    categories = Category.objects.all()
    categories_data = {}

    for category in categories:
        articles = Article.objects.filter(category=category).order_by('-published_date')[:10]
        researches = Research.objects.filter(category=category).order_by('-published_date')[:10]
        mixed_content = list(articles) + list(researches)
        categories_data[category] = mixed_content[:10]  # Combine and limit to 10 items

    return render(request, 'categories/categories_page.html', {'categories_data': categories_data})


class ArticleDetailView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        
        # Increment views by 1
        article.views += 1
        article.save()

        # Fetch related articles based on the same category, excluding the current article
        related_articles = Article.objects.filter(category=article.category).exclude(id=article.id)[:5]

        return render(request, 'articles/article_detail.html', {
            'article': article,
            'related_articles': related_articles,
        })

class ResearchDetailView(View):
    def get(self, request, slug):
        research = get_object_or_404(Research, slug=slug)
        
        # Increment views by 1
        research.views += 1
        research.save()

        # Fetch related research based on the same category, excluding the current research
        related_research = Research.objects.filter(category=research.category).exclude(id=research.id)[:5]

        return render(request, 'researches/research_detail.html', {
            'research': research,
            'related_research': related_research,
        })