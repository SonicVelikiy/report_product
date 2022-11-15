import datetime

from django.db import models


# Create your models here.

class product(models.Model):
    sinf1 = 'I-sinf'
    sinf2 = 'II-sinf'
    sinf3 = 'III-sinf'
    sinf4 = 'IV-sinf'
    sinf5 = 'V-sinf'
    ROLES = (
        (sinf1, "I-sinf"),
        (sinf2, "II-sinf"),
        (sinf3, "III-sinf"),
        (sinf4, "IV-sinf"),
        (sinf5, "V-sinf"),
    )
    Mahsulot_nomi = models.CharField(max_length=256)
    Shifr = models.CharField(max_length=128)
    Sinf = models.CharField(max_length=30, choices=ROLES)

    Texnik_shart = models.CharField(max_length=32, default='TS-28078417')
    Texnik_shart_raqami = models.CharField(max_length=32)

    Sana = models.DateTimeField(default=datetime.datetime.now())
    Sinov_namunasi = models.BooleanField(default=False)
    Partiya_soni_belgilash = models.IntegerField(default=1)

    Buyurtmachi_nomi = models.CharField(max_length=128)
    Buyurtmachi_raqami = models.IntegerField()
    Buyurtma_soni = models.IntegerField()
    Partiya_raqami = models.IntegerField()
    Buyurtma_muddati = models.DateTimeField()
    Sinov_bayonnomasi_raqami = models.CharField(max_length=8)
    Sinov_bayonnomasi_sanasi = models.DateTimeField()
    Sinov_qilingan_mahsulot_nomi = models.CharField(max_length=128)
    Sinov_bayonnomasi_registratsiya_raqami = models.CharField(max_length=8)

    class Meta:
        db_table = "product"
