from django.db import models

class Contact_data(models.Model):
    """ Model for contact data """

    address = models.CharField(max_length=300, verbose_name="Dirección")
    city = models.CharField(max_length=100, verbose_name="Ciudad")
    postal_code = models.IntegerField(verbose_name="Código Postal")
    state = models.CharField(max_length=100, verbose_name="Comunidad Autónoma")
    country = models.CharField(max_length=100, verbose_name="Pais")
    phone = models.IntegerField(verbose_name="Número de teléfono")
    prefix = models.CharField(max_length=10, verbose_name="Prefijo")
    email = models.EmailField(verbose_name="Dirección de Email")
    website = models.URLField(verbose_name="Website")
    linkedin = models.URLField(verbose_name="LinkedIN")

    class Meta:
        verbose_name = "Dato de contacto"
        verbose_name_plural = "Datos de contacto"

    def __str__(self):
        return "Dirección: {}, {}, {}. {}, {}. Tel: {} {}. Email: {}. Website: {}. LinkedIN: {}.".format(
            self.address,
            self.postal_code,
            self.city,
            self.state,
            self.country,
            self.prefix,
            self.phone,
            self.email,
            self.website,
            self.linkedin
        )
    

class Experience(models.Model):
    """ Profesional experience """

    job = models.CharField(max_length=300, verbose_name="Puesto")
    company = models.CharField(max_length=300, verbose_name="Compañía")
    start_date = models.DateField(verbose_name="Fecha inicio")
    end_date = models.DateField(verbose_name="Fecha fin", default=False)
    actually_job = models.BooleanField(verbose_name="Trabajo actual", default=False)
    resume = models.TextField(verbose_name="Resumen del puesto")

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ["-end_date",]

    def __str__(self):
        end_date = "Actualidad" if self.actually_job else str(self.end_date)
        return "{}/{} - {} en {}.".format(str(self.start_date), end_date, self.job, self.company)
    

class Program_language(models.Model):
    """ Set program language """

    LEVEL_CHOICES = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5")
    )

    name = models.CharField(max_length=100, verbose_name="Lenguaje")
    level = models.CharField(max_length=10, verbose_name="Nivel", choices=LEVEL_CHOICES)
    logo = models.ImageField(upload_to="skills/", verbose_name="Logotipo")
    primary_language = models.BooleanField(default=False)
    other_languages = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Lenguaje de programación"
        verbose_name = "Lenguajes de programación"

    def __str__(self):
        return self.name
    

class Framework(models.Model):
    """ Set Frameworks and habilities """

    LEVEL_CHOICES = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5")
    )

    name = models.CharField(max_length=100, verbose_name="Framework o tecnología")
    language = models.ForeignKey(Program_language, on_delete=models.CASCADE, verbose_name="Basado en", blank=True, null=True)
    level = models.CharField(max_length=10, verbose_name="Nivel", choices=LEVEL_CHOICES)
    logo = models.ImageField(upload_to="skills/", verbose_name="Logotipo")

    class Meta:
        verbose_name = "Framework"
        verbose_name = "Frameworks"

    def __str__(self):
        return self.name
    
class Language(models.Model):
    """ Set language """

    LEVEL_CHOICES = (
        ("elemental","Elemental"),
        ("intermedio","Intermedio"),
        ("avanzado","Avanzado"),
        ("nativo","Nativo")
    )

    name = models.CharField(max_length=100, verbose_name="Idioma")
    level = models.CharField(max_length=10, verbose_name="Nivel", choices=LEVEL_CHOICES)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name = "Habilidades"

    def __str__(self):
        return self.name


class Tool(models.Model):
    """ Set tools, software and OS """

    name = models.CharField(max_length=100, verbose_name="Nombre")

    class Meta:
        verbose_name = "Herramienta"
        verbose_name_plural = "Herramientas"

    def __str__(self):
        return self.name


class Education(models.Model):
    """ School education """

    name = models.CharField(max_length=300, verbose_name="Nombre")
    school = models.CharField(max_length=300, verbose_name="Escuela")
    start_date = models.DateField(verbose_name="Fecha inicio")
    end_date = models.DateField(verbose_name="Fecha fin")
    resume = models.TextField(verbose_name="Resumen de la formación")
    
    class Meta:
        verbose_name = "Formación"
        verbose_name_plural = "Formaciones"
        ordering = ["-start_date",]

    def __str__(self):
        return "{} en {}.".format(self.name, self.school)


class Certification(models.Model):
    """ School education """

    name = models.CharField(max_length=300, verbose_name="Nombre")
    school = models.CharField(max_length=300, verbose_name="Escuela")
    start_date = models.DateField(verbose_name="Fecha curso")

    class Meta:
        verbose_name = "Certificación"
        verbose_name_plural = "Certificaciones"
        ordering = ["-start_date",]

    def __str__(self):
        return "{} - {} en {}.".format(str(self.start_date), self.name, self.school)
    
class Other_url(models.Model):
    """ Sites of Interest """

    name = models.CharField(max_length=300, verbose_name="Sitio")
    url = models.URLField(verbose_name="URL")

    class Meta:
        verbose_name = "Otra url"
        verbose_name_plural = "Otras urls de interés"

    def __str__(self):
        return "{}: {}.".format(self.name, self.url)

class CV(models.Model):
    """ Global model to generate CV """

    cvname = models.CharField(max_length=100, verbose_name="Nombre CV")
    name = models.CharField(max_length=300, verbose_name="Nombre completo")
    contact_data = models.ForeignKey(Contact_data, on_delete=models.CASCADE, verbose_name="Datos de contacto")
    resume = models.TextField(verbose_name="Resumen Profesional")
    experiences = models.ManyToManyField(Experience, verbose_name="Experiencia")
    program_languages = models.ManyToManyField(Program_language, verbose_name="Lenguajes de programación")
    frameworks = models.ManyToManyField(Framework, verbose_name="Frameworks")
    languages = models.ManyToManyField(Language, verbose_name="Idiomas")
    tools = models.ManyToManyField(Tool, verbose_name="Herramientas")
    education = models.ManyToManyField(Education, verbose_name="Formación")
    certification = models.ManyToManyField(Certification, verbose_name="Certificación")
    urls_for_interest = models.ManyToManyField(Other_url, verbose_name="Sitios de interés")

    class Meta: 
        verbose_name = "Curriculum Vitae"
        verbose_name_plural = "Curriculums"

    def __str__(self):
        return self.cvname

