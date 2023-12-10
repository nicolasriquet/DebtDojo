# Generated by Django 4.1.11 on 2023-12-02 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0227_alter_debt_risk_acceptance_recommendation_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt_risk_acceptance',
            name='accepted_by',
            field=models.CharField(blank=True, default=None, help_text='The person that accepts the risk, can be outside of Debt Citadel.', max_length=200, null=True, verbose_name='Accepted By'),
        ),
        migrations.AlterField(
            model_name='debt_risk_acceptance',
            name='expiration_date',
            field=models.DateTimeField(blank=True, default=None, help_text='When the risk acceptance expires, the Debt Items will be reactivated (unless disabled below).', null=True),
        ),
        migrations.AlterField(
            model_name='debt_risk_acceptance',
            name='owner',
            field=models.ForeignKey(help_text='User in Debt Citadel owning this acceptance. Only the owner and staff users can edit the risk acceptance.', on_delete=django.db.models.deletion.RESTRICT, to='dojo.dojo_user'),
        ),
        migrations.AlterField(
            model_name='debt_risk_acceptance',
            name='reactivate_expired',
            field=models.BooleanField(default=True, help_text='Reactivate Debt Items when risk acceptance expires?', verbose_name='Reactivate debt_items on expiration'),
        ),
        migrations.AlterField(
            model_name='debt_risk_acceptance',
            name='recommendation',
            field=models.CharField(choices=[('A', 'Accept (The debt is acknowledged, yet remains)'), ('M', 'Mitigate (The debt still exists, yet compensating actions make it less of a problem)'), ('P', 'Pay (The debt is eliminated)'), ('T', 'Transfer (The debt is transferred to a 3rd party)')], default='P', help_text='Recommendation from the team.', max_length=2, verbose_name='Recommendation'),
        ),
        migrations.AlterField(
            model_name='debt_risk_acceptance',
            name='restart_sla_expired',
            field=models.BooleanField(default=False, help_text='When enabled, the SLA for Debt Items is restarted when the risk acceptance expires.', verbose_name='Restart SLA on expiration'),
        ),
    ]