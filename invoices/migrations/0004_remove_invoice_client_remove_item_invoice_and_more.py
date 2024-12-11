# Generated by Django 5.1.4 on 2024-12-11 19:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_rename_company_name_client_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='client',
        ),
        migrations.RemoveField(
            model_name='item',
            name='invoice',
        ),
        migrations.CreateModel(
            name='UnifiedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('invoice_number', models.CharField(editable=False, max_length=20, unique=True)),
                ('date_issued', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Overdue', 'Overdue')], default='Pending', max_length=10)),
                ('item_title', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddConstraint(
            model_name='unifiedmodel',
            constraint=models.UniqueConstraint(fields=('invoice_number', 'item_title'), name='unique_invoice_item'),
        ),
    ]