from django.contrib import admin
from .models import React, Usuario, Tamanho, pizzaTemTamanho, Sabores
# Register your models here.


    
admin.site.register(React)
admin.site.register(Usuario)
admin.site.register(Tamanho)
admin.site.register(pizzaTemTamanho)
admin.site.register(Sabores)

