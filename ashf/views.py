from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PapersContent

@csrf_exempt
def get_papers(request):
    papers = PapersContent.objects.all()
    return JsonResponse(list(papers), safe=False)