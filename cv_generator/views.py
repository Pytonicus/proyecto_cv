from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from weasyprint.fonts import FontConfiguration

from .models import CV


def export_pdf(request):
    """ Export view data to pdf """

    cv = CV.objects.all()[0]
    base_url = request.build_absolute_uri('/')
    context = {"cv": cv, "base_url": base_url}
    html = render_to_string("cv/cv-pdf.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; cv.pdf"

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)

    return response