from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class User(models.Model):
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=25, blank=False)  # Verschlusselung


class Data(models.Model):
    vorname = models.CharField(max_length=30, blank=False)
    nachname = models.CharField(max_length=30, blank=False)
    geburstag = models.DateField(blank=False)  # Wie aendern sie sich?
    d_ort = models.CharField(max_length=30, blank=False)
    familienstand = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    tel = models.CharField(blank=False, unique=True, max_length=30)
    adresse = models.CharField(max_length=30, blank=False)
    hobbys = models.CharField(max_length=80, blank=False)  # Wie werden Sie eingegeben # könnte leer sein

    user = models.OneToOneField(User, on_delete=models.CASCADE)
   

class Sprachen(models.Model):
    sprache = models.CharField(max_length=20, blank=False)
    sprachniveau = models.CharField(max_length=30, blank=False)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)


class Cv(models.Model):
    layout = models.IntegerField(blank=False)   # muss noch besprechen werden
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Ausbildung(models.Model):
    abschluss = models.CharField(max_length=100)
    a_anfang = models.DateField()
    e_ende = models.DateField()
    a_ort = models.CharField(max_length=100)
    a_beschreibung = models.TextField(blank=True)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)


class Beruf(models.Model):
    b_anfang = models.DateField()
    b_ende = models.DateField()
    b_ort = models.CharField(max_length=100)
    b_beschreibung = models.TextField(blank=True)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)


class Kenntnisse(models.Model):
    kenntniss = models.CharField(max_length=100)
    kn_niveau = models.CharField(max_length=50)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
