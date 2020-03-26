from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from managers import score_manager, cors_manager
import json

@csrf_exempt
def search(request):
    if request.method == 'POST':
        keyword = json.loads(request.body)["keyword"]
        page_content = cors_manager.get_search_content(keyword)
        # TODO: pass page_content to search_manager to webscrape out the results and return as list in json
        response = HttpResponse(page_content)
        return response

@csrf_exempt
def get_score(request):
    if request.method == 'POST':
        # TODO:
        score = score_manager.get_the_score()
        response = JsonResponse(score)
        return response
