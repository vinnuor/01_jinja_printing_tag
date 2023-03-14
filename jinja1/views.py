from django.shortcuts import render

# Create your views here.
def sample(request):
    d={'tag':'jinja tags'}
    return render(request,'jinja_tag.html',context=d)