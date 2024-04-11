from django.db import models

class React(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
    #image = models.ImageField(upload_to='pizzas/images/')
    imagem = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome
class Tamanho(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class pizzaTemTamanho(models.Model):
    id = models.AutoField(primary_key=True)
    react = models.ForeignKey(React, on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.react.nome + ' - ' + self.tamanho.nome


class Sabores(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
    
    
    
class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    senha = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=200)
    pizzas = models.ManyToManyField(React) 
    quantidade = models.IntegerField()
    
    def __str__(self):
        return self.usuario.nome
