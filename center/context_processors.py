from .models import Category, Course

def categories(request):
    return {"categories": Category.actives.all()}

def courses(request):
    return {"courses": Course.actives.all()}