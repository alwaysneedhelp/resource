# admin.py

from django.contrib import admin
from .models import Article, Category, Research, Member  # Import Member
from ckeditor.widgets import CKEditorWidget
from django import forms

class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }

class ResearchAdminForm(forms.ModelForm):  # Create a form for Research
    class Meta:
        model = Research
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }

class MemberAdminForm(forms.ModelForm):  # Create a form for Member
    class Meta:
        model = Member
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

class ResearchAdmin(admin.ModelAdmin):  # Admin for Research
    form = ResearchAdminForm

class MemberAdmin(admin.ModelAdmin):  # Admin for Member
    form = MemberAdminForm

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Research, ResearchAdmin)  # Register Research
admin.site.register(Member, MemberAdmin)  # Register Member