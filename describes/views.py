from django.shortcuts import render
from describes.models import Describes


# Create your views here.

def describe_index(request) :
    describes = Describes.objects.all()
    context = {
        'describes' : describes
    }
    return render(request, 'describe_index.html', context)


def describe_detail(request, pk) :
    describe = Describes.objects.get(pk=pk)
    context = {
        'describe' : describe
    }
    return render(request, 'describe_detail.html', context)
