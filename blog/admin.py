from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Seleccionar los campos que se muestren en la lista del panel admin(para campos relacionados, crear un campo propio)
    list_display = ('title', 'author', 'published', 'post_categories') 
    # Ordenar la lista del panel administrativo mediante los campos especificados
    ordering = ('author', 'published') 
    # Buscar elementos, mediante los campos especificados 
    search_fields = ('title', 'author__username', 'categories__name') 
    # Gerarquisar la fecha, para hacer búsqueda, ya sea por día, mes y año
    date_hierarchy = 'published'
    # Filtrar la búsqueda por los campos especificados (en general, tiene sentido con campos relacionados)
    list_filter = ('author__username', 'categories__name')

    # Crear nuestros propios campos especiales
    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorias'



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)