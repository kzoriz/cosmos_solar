from django.shortcuts import render

from cosmos_solar.models import SobreNos


# Create your views here.
def home(request, pk=None):
    text = SobreNos.objects.get(pk=1)
    context = {
        "object": text,

    }
    return render(request, "cosmos_solar/index.html", context)
