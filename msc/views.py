from django.shortcuts import render
from  django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.views import generic

# Create your views here.


def index(request):
    context = {
        'tips': NutritionTips.objects.all(),
    }
    return render(request, 'msc/index.html', context)


def contact(request):
    if request.method == 'POST':
        print(request.POST)
        # return JsonResponse({'blank': f'{request.POST["name"]}'})
        if request.POST['name'] != '' and request.POST['mail'] != '' and request.POST['message'] != '' and request.POST['subject'] != '':
            name = request.POST['name']
            mail = request.POST['mail']
            msg = request.POST['message']
            subject = request.POST['subject']

            new_contact = Contact()
            new_contact.name = name
            new_contact.mail = mail
            new_contact.message = msg
            new_contact.subject = subject
            new_contact.save()

            dic = {'info': 'success'}
            return JsonResponse(dic)
        else:
            dic = {'info': f'{request.POST}'}
            return JsonResponse(dic)
    else:
        return HttpResponseRedirect('/msc/')


# def review(request):
#     context = {
#         'reviews': Review.objects.all()
#     }
#     return render(request, 'msc/review.html', context)

class ReviewView(generic.ListView):
    context_object_name = 'reviews'
    template_name = 'msc/review.html'
    paginate_by = 3

    def get_queryset(self):
        return Review.objects.all()


class HealthView(generic.ListView):
    context_object_name = 'tips'
    template_name = 'msc/health.html'
    paginate_by = 3

    def get_queryset(self):
        return NutritionTips.objects.all()