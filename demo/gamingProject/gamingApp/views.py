from django.shortcuts import render,HttpResponse
from .models import GameForm,PlayerForm
from .models import GameModel,PlayerModel
from django.views.generic import ListView,DetailView

def addgames(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = GameForm()
        return render(request, 'addgame.html', {'form': form})

class GameListView(ListView):
    model = GameModel
    template_name = 'games_list.html'
    context_object_name = 'games'
    


class GameDetailView(DetailView):
    model = GameModel
    template_name = 'games_detail.html'
    context_object_name = 'game'

import csv
def gen_csv(request):
    students = GameModel.objects.all().values()
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename = "students.csv"'
    writer = csv.writer(response)
    writer.writerow(['Sl No','game_name','score','players'])
    for s in students:
        writer.writerow(s.values())

    return response