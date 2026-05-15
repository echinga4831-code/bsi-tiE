from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=100,verbose_name = 'Titulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(verbose_name='Imagen',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de actualizacion')

    def __str__(self):
        return self.title
class Meta:
    ordering = ['-created']
    db_table = 'portfolio'
    verbose_name = 'Portfolio'
    verbose_name_plural = 'Portfolios'
