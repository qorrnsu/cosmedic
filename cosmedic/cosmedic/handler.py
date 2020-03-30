from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from managers import score_manager, cors_manager, search_manager
import json

@csrf_exempt
def search(request: object) -> JsonResponse:
    if request.method == 'POST':
        keyword = json.loads(request.body)['keyword']
        keyword.replace(' ', '+')

        page_content = cors_manager.get_search_content(keyword)

        results = search_manager.scrape_search_results(page_content)

        return JsonResponse({
            'length': len(results),
            'results': results
        })

@csrf_exempt
def get_score(request):
    if request.method == 'POST':
        # TODO:
        score = score_manager.get_the_score()
        response = JsonResponse(score)
        return response
