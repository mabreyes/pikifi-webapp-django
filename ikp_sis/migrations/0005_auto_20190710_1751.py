# Generated by Django 2.1.5 on 2019-07-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikp_sis', '0004_auto_20190710_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='middle_name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='child_status',
            field=models.CharField(choices=[('None', 'Select Status'), ('Orphaned', 'Orphaned'), ('Neglected', 'Neglected'), ('Abandoned', 'Abandoned'), ('Abused (Physically/Sexually)', 'Abused (Physically/Sexually)'), ('Trafficked', 'Trafficked'), ('Child in Conflict with the Law (CICL)', 'Child in Conflict with the Law (CICL)')], default='None', max_length=100),
        ),
    ]
