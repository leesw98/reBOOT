# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('tax_receipt_no', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Tax Receipt Number')),
                ('donate_date', models.DateField(verbose_name='Date Donated')),
                ('verified', models.BooleanField(default=False, verbose_name='Verified Donation')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=75, verbose_name='Donor Name')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('want_receipt', models.BooleanField(verbose_name='Tax receipt?')),
                ('telephone_number', models.CharField(blank=True, max_length=30, verbose_name='Telephone #')),
                ('mobile_number', models.CharField(blank=True, max_length=30, verbose_name='Mobile #')),
                ('address_line', models.CharField(max_length=256, verbose_name='Street Address')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('province', models.CharField(choices=[('AB', 'Alberta'), ('BC', 'British Columbia'), ('ON', 'Ontario'), ('NS', 'Nova Scotia'), ('NL', 'Newfoundland and Labrador'), ('NU', 'Nunavut'), ('YT', 'Yukon'), ('MB', 'Manitoba'), ('SK', 'Saskatchewan'), ('PE', 'Prince Edward Island'), ('NT', 'Northwest Territories'), ('NB', 'New Brunswick'), ('QC', 'Quebec')], max_length=20, verbose_name='Province')),
                ('postal_code', models.CharField(max_length=7, verbose_name='Postal Code')),
                ('verified', models.BooleanField(default=False, verbose_name='Donations & Items Verified?')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Description')),
                ('particulars', models.CharField(blank=True, max_length=500, verbose_name='Particulars')),
                ('manufacturer', models.CharField(blank=True, max_length=500, verbose_name='Manufacturer')),
                ('model', models.CharField(blank=True, max_length=50, verbose_name='Model')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('working', models.BooleanField(verbose_name='Is the item working?')),
                ('condition', models.CharField(blank=True, max_length=20, verbose_name='Condition')),
                ('quality', models.CharField(choices=[('H', 'High'), ('L', 'Low'), ('M', 'Medium')], max_length=20, verbose_name='Quality')),
                ('batch', models.CharField(blank=True, max_length=10, verbose_name='Batch')),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Value')),
                ('verified', models.BooleanField(default=False, verbose_name='Verified Item')),
                ('tax_receipt_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Donation', verbose_name='Tax Receipt Number')),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='donor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Donor', verbose_name='Donor ID'),
        ),
    ]
