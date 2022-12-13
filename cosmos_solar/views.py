from django.shortcuts import render

from cosmos_solar.models import SobreNos


# Create your views here.
def home(request, pk=None):
    sobre_nos = SobreNos.objects.all()

    if len(sobre_nos) == 0:
        context2 = {
            "object.title1": "empty",
            "object.title2": "empty",
            "object.text": "empty",

        }
        return render(request, "cosmos_solar/index.html", context2)
    else:
        text = SobreNos.objects.first()
        context = {
            "object": text,

        }
        return render(request, "cosmos_solar/index.html", context)

