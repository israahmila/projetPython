from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categorie, Fournisseur, Meuble

# --- Meuble Views ---
class MeubleListView(ListView):
    model = Meuble
    template_name = 'meuble_list.html'
    context_object_name = 'meubles'

class MeubleDetailView(DetailView):
    model = Meuble
    template_name = 'meuble_detail.html'

class MeubleCreateView(CreateView):
    model = Meuble
    template_name = 'meuble_form.html'
    fields = ['nom', 'categorie', 'fournisseur', 'description', 'prix', 'quantite_en_stock', 'image']
    success_url = reverse_lazy('meuble:meuble_list')

class MeubleUpdateView(UpdateView):
    model = Meuble
    template_name = 'meuble_form.html'
    fields = ['nom', 'categorie', 'fournisseur', 'description', 'prix', 'quantite_en_stock', 'image']
    success_url = reverse_lazy('meuble:meuble_list')

class MeubleDeleteView(DeleteView):
    model = Meuble
    template_name = 'meuble_confirm_delete.html'
    success_url = reverse_lazy('meuble:meuble_list')


# --- Categorie Views ---
class CategorieListView(ListView):
    model = Categorie
    template_name = 'categorie_list.html'
    context_object_name = 'categories'

class CategorieCreateView(CreateView):
    model = Categorie
    template_name = 'categorie_form.html'
    fields = ['nom', 'description']
    success_url = reverse_lazy('meuble:categorie_list')

class CategorieUpdateView(UpdateView):
    model = Categorie
    template_name = 'categorie_form.html'
    fields = ['nom', 'description']
    success_url = reverse_lazy('meuble:categorie_list')

class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = 'categorie_confirm_delete.html'
    success_url = reverse_lazy('meuble:categorie_list')


# --- Fournisseur Views ---
class FournisseurListView(ListView):
    model = Fournisseur
    template_name = 'fournisseur_list.html'
    context_object_name = 'fournisseurs'

class FournisseurCreateView(CreateView):
    model = Fournisseur
    template_name = 'fournisseur_form.html'
    fields = ['nom', 'contact', 'adresse']
    success_url = reverse_lazy('meuble:fournisseur_list')

class FournisseurUpdateView(UpdateView):
    model = Fournisseur
    template_name = 'fournisseur_form.html'
    fields = ['nom', 'contact', 'adresse']
    success_url = reverse_lazy('meuble:fournisseur_list')

class FournisseurDeleteView(DeleteView):
    model = Fournisseur
    template_name = 'fournisseur_confirm_delete.html'
    success_url = reverse_lazy('meuble:fournisseur_list')
