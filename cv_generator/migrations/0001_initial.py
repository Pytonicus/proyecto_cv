# Generated by Django 5.1.1 on 2024-09-17 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Certification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300, verbose_name="Nombre")),
                ("school", models.CharField(max_length=300, verbose_name="Escuela")),
                ("start_date", models.DateField(verbose_name="Fecha curso")),
            ],
            options={
                "verbose_name": "Formación",
                "verbose_name_plural": "Formaciones",
            },
        ),
        migrations.CreateModel(
            name="Contact_data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=300, verbose_name="Dirección")),
                ("city", models.CharField(max_length=100, verbose_name="Ciudad")),
                (
                    "postal_code",
                    models.IntegerField(max_length=5, verbose_name="Código Postal"),
                ),
                (
                    "state",
                    models.CharField(max_length=100, verbose_name="Comunidad Autónoma"),
                ),
                ("country", models.CharField(max_length=100, verbose_name="Pais")),
                (
                    "phone",
                    models.IntegerField(
                        max_length=100, verbose_name="Número de teléfono"
                    ),
                ),
                ("prefix", models.CharField(max_length=10, verbose_name="Prefijo")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, verbose_name="Dirección de Email"
                    ),
                ),
                ("website", models.URLField(verbose_name="Website")),
                ("linkedin", models.URLField(verbose_name="LinkedIN")),
            ],
            options={
                "verbose_name": "Dato de contacto",
                "verbose_name_plural": "Datos de contacto",
            },
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300, verbose_name="Nombre")),
                ("school", models.CharField(max_length=300, verbose_name="Escuela")),
                ("start_date", models.DateField(verbose_name="Fecha inicio")),
                ("end_date", models.DateField(verbose_name="Fecha fin")),
                ("resume", models.TextField(verbose_name="Resumen de la formación")),
            ],
            options={
                "verbose_name": "Formación",
                "verbose_name_plural": "Formaciones",
            },
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("job", models.CharField(max_length=300, verbose_name="Puesto")),
                ("company", models.CharField(max_length=300, verbose_name="Compañía")),
                ("start_date", models.DateField(verbose_name="Fecha inicio")),
                ("end_date", models.DateField(verbose_name="Fecha fin")),
                ("actually_job", models.BooleanField(default=False)),
                ("resume", models.TextField(verbose_name="Resumen del puesto")),
            ],
            options={
                "verbose_name": "Experiencia",
                "verbose_name_plural": "Experiencias",
            },
        ),
        migrations.CreateModel(
            name="Other_url",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300, verbose_name="Sitio")),
                ("url", models.URLField(verbose_name="URL")),
            ],
            options={
                "verbose_name": "Formación",
                "verbose_name_plural": "Formaciones",
            },
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Tecnología")),
                (
                    "level",
                    models.CharField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
                        max_length=10,
                        verbose_name="Nivel",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(upload_to="skills/", verbose_name="Logotipo"),
                ),
            ],
            options={
                "verbose_name": "Habilidades",
            },
        ),
        migrations.CreateModel(
            name="Tool",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Nombre")),
            ],
            options={
                "verbose_name": "Herramienta",
                "verbose_name_plural": "Herramientas",
            },
        ),
        migrations.CreateModel(
            name="CV",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cvname", models.CharField(max_length=100, verbose_name="Nombre CV")),
                (
                    "name",
                    models.CharField(max_length=300, verbose_name="Nombre completo"),
                ),
                ("resume", models.TextField(verbose_name="Resumen Profesional")),
                (
                    "certification",
                    models.ManyToManyField(
                        to="cv_generator.certification", verbose_name="Certificación"
                    ),
                ),
                (
                    "contact_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cv_generator.contact_data",
                        verbose_name="Datos de contacto",
                    ),
                ),
                (
                    "education",
                    models.ManyToManyField(
                        to="cv_generator.education", verbose_name="Formación"
                    ),
                ),
                (
                    "experiences",
                    models.ManyToManyField(
                        to="cv_generator.experience", verbose_name="Experiencia"
                    ),
                ),
                (
                    "urls_for_interest",
                    models.ManyToManyField(
                        to="cv_generator.other_url", verbose_name="Sitios de interés"
                    ),
                ),
                (
                    "skills",
                    models.ManyToManyField(
                        to="cv_generator.skill", verbose_name="Habilidades"
                    ),
                ),
                (
                    "tools",
                    models.ManyToManyField(
                        to="cv_generator.tool", verbose_name="Herramientas"
                    ),
                ),
            ],
            options={
                "verbose_name": "Curriculum Vitae",
                "verbose_name_plural": "Curriculums",
            },
        ),
    ]
