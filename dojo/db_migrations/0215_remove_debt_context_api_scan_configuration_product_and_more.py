# Generated by Django 4.1.11 on 2023-11-20 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0214_remove_debt_test_dojo_debt_t_debt_en_1d276c_idx_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='debt_context_api_scan_configuration',
            name='product',
        ),
        migrations.AddField(
            model_name='debt_context_api_scan_configuration',
            name='debt_context',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dojo.debt_context'),
            preserve_default=False,
        ),
    ]