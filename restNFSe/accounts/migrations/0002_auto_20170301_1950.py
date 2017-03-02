# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-01 22:50
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='certificado_pfx',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/marcelo/Dev/Personal_Projects/restNFSe/restNFSe/accounts/cert'), upload_to='', verbose_name='Certificado PFX'),
        ),
        migrations.AlterField(
            model_name='user',
            name='numero_lote_rps',
            field=models.IntegerField(default=0, verbose_name='Número Lote RPS'),
        ),
    ]