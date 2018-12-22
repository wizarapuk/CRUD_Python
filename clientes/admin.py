from django.contrib import admin
from .models import Person, documento, Venda, Produto

admin.site.register(Person)
admin.site.register(documento)
admin.site.register(Venda)
admin.site.register(Produto)
# Register your models here.
