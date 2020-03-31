import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from managers import score_manager, cors_manager, search_manager


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
        item_url = json.loads(request.body)['item_url']

        page_content = cors_manager.get_item_content(item_url)

        data = score_manager.scrape_item_tables(page_content)
        response = JsonResponse({
            'data': data
        })

        return response
