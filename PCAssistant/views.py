from django.shortcuts import render
from .audio_help import audioQuery
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def start_module(request):
    if request.method == 'POST':
        audio_query = audioQuery()
        audio_query.startModule()
        query = audio_query.query
        return render(request, 'result.html', {'query': query})
    return render(request, 'voice-help.html')
