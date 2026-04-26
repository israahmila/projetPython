from django.contrib import admin
from .models import Categorie, Fournisseur, Meuble

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)

@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'contact', 'adresse')
    search_fields = ('nom', 'contact')

@admin.register(Meuble)
class MeubleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'fournisseur', 'prix', 'quantite_en_stock')
    list_filter = ('categorie', 'fournisseur')
    search_fields = ('nom', 'description')
