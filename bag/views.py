from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ View that renders page with shopping bag contents """
    return render(request, 'bag/bag.html')
