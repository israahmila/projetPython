from django.urls import path
from . import views

app_name = 'meuble'

urlpatterns = [
    path('', views.MeubleListView.as_view(), name='meuble_list'),
    path('meuble/<int:pk>/', views.MeubleDetailView.as_view(), name='meuble_detail'),
    path('meuble/ajouter/', views.MeubleCreateView.as_view(), name='meuble_add'),
    path('meuble/<int:pk>/modifier/', views.MeubleUpdateView.as_view(), name='meuble_edit'),
    path('meuble/<int:pk>/supprimer/', views.MeubleDeleteView.as_view(), name='meuble_delete'),

    path('categories/', views.CategorieListView.as_view(), name='categorie_list'),
    path('categorie/ajouter/', views.CategorieCreateView.as_view(), name='categorie_add'),
    path('categorie/<int:pk>/modifier/', views.CategorieUpdateView.as_view(), name='categorie_edit'),
    path('categorie/<int:pk>/supprimer/', views.CategorieDeleteView.as_view(), name='categorie_delete'),

    path('fournisseurs/', views.FournisseurListView.as_view(), name='fournisseur_list'),
    path('fournisseur/ajouter/', views.FournisseurCreateView.as_view(), name='fournisseur_add'),
    path('fournisseur/<int:pk>/modifier/', views.FournisseurUpdateView.as_view(), name='fournisseur_edit'),
    path('fournisseur/<int:pk>/supprimer/', views.FournisseurDeleteView.as_view(), name='fournisseur_delete'),
]
