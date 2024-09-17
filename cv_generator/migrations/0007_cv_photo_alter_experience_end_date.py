# Generated by Django 5.1.1 on 2024-09-17 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "cv_generator",
            "0006_alter_certification_options_alter_experience_options_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="cv",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile/", verbose_name="Foto"
            ),
        ),
        migrations.AlterField(
            model_name="experience",
            name="end_date",
            field=models.DateField(blank=True, null=True, verbose_name="Fecha fin"),
        ),
    ]
