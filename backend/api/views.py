from django.http import JsonResponse
import json
def api_home(request, *args, **kwargs):

    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    # print(dict(request.headers))
    # data['headers'] = request.headers
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    data['headers'] = dict(request.headers)
    return JsonResponse(data)