from django.contrib import admin

from .models import Post


#Criando campo de visualização
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "update")
    prepopulated_fields = {"slug": ("title",)} #preencher automaticamente slug
# Register your models here.
