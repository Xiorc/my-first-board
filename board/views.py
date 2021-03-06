from django.shortcuts import render
from django.utils import timezone
from .models import Board

# Create your views here.
def bulletin_list(request):
	boards = Board.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'board/bulletin_list.html', {'boards': boards})

