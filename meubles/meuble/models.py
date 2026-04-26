from django.db import models
from django.urls import reverse

class Categorie(models.Model):
    nom = models.CharField('Nom', max_length=100)
    description = models.TextField('Description', blank=True)

    class Meta:
        ordering = ['nom']
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('meuble:categorie_detail', kwargs={'pk': self.pk})

class Fournisseur(models.Model):
    nom = models.CharField('Nom', max_length=100)
    contact = models.CharField('Contact', max_length=100, blank=True)
    adresse = models.TextField('Adresse', blank=True)

    class Meta:
        ordering = ['nom']
        verbose_name = 'Fournisseur'
        verbose_name_plural = 'Fournisseurs'

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('meuble:fournisseur_detail', kwargs={'pk': self.pk})

class Meuble(models.Model):
    nom = models.CharField('Nom', max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name='Catégorie')
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Fournisseur')
    description = models.TextField('Description', blank=True)
    prix = models.DecimalField('Prix', max_digits=10, decimal_places=2)
    quantite_en_stock = models.IntegerField('Quantité en stock', default=0)
    image = models.ImageField('Image', upload_to='meubles/', blank=True, null=True)

    class Meta:
        ordering = ['nom']
        verbose_name = 'Meuble'
        verbose_name_plural = 'Meubles'

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('meuble:meuble_detail', kwargs={'pk': self.pk})
