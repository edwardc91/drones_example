# Generated by Django 3.2 on 2022-05-21 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_flight_load'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drone',
            options={},
        ),
        migrations.AlterModelOptions(
            name='medication',
            options={},
        ),
        migrations.AlterField(
            model_name='flight',
            name='drone_rel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights_rel', to='base.drone', verbose_name='Drone'),
        ),
        migrations.AlterField(
            model_name='load',
            name='flight_rel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loads_rel', to='base.flight', verbose_name='Flight'),
        ),
        migrations.AlterField(
            model_name='load',
            name='medication_rel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='loads_rel', to='base.medication', verbose_name='Medication'),
        ),
        migrations.AddConstraint(
            model_name='drone',
            constraint=models.CheckConstraint(check=models.Q(weight_limit__lte=500), name='weight_limit_lte_500'),
        ),
        migrations.AddConstraint(
            model_name='drone',
            constraint=models.CheckConstraint(check=models.Q(weight_limit__gte=0), name='weight_limit_gte_0'),
        ),
        migrations.AddConstraint(
            model_name='drone',
            constraint=models.CheckConstraint(check=models.Q(battery_capacity__lte=100), name='battery_capacity_lte_100'),
        ),
        migrations.AddConstraint(
            model_name='drone',
            constraint=models.CheckConstraint(check=models.Q(battery_capacity__gte=0), name='battery_capacity_gte_0'),
        ),
        migrations.AddConstraint(
            model_name='medication',
            constraint=models.CheckConstraint(check=models.Q(weight__lte=500), name='weight_lte_500'),
        ),
        migrations.AddConstraint(
            model_name='medication',
            constraint=models.CheckConstraint(check=models.Q(weight__gt=0), name='weight_gt_0'),
        ),
    ]
