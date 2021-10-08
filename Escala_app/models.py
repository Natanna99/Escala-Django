from django.db import models

class Medico(models.Model):
    nome= models.CharField(max_length= 30)
    sobrenome= models.CharField(max_length= 150)
    data_admissao= models.DateField()

    def __str__(self):
        return "{} - {}".format("Medicos", self.nome)

class Posto(models.Model):
    nome_posto= models.CharField(max_length= 50)
    endereco= models.CharField(max_length= 150)

    def __str__(self):
        return "{} - {}".format("Postos", self.nome_posto)

class Folga(models.Model):
    dia= models.DateField()
    Medicos= models.ForeignKey(Medico, on_delete= models.CASCADE, null= True, blank= True)

    def __str__(self):
        return "{} - {}".format("Folga", self.dia)

class Escala(models.Model):
    Medicos= models.ForeignKey(Medico, on_delete= models.CASCADE, null= True, blank= True)
    Folgas= models.ForeignKey(Folga, on_delete= models.CASCADE, null= True, blank= True)
    Posto= models.ForeignKey(Posto, on_delete= models.CASCADE, null= True, blank= True)
    data= models.DateField()

    def __str__(self):
        return "{} - {}".format("Escala", self.data)
