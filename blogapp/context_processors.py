from .models import Category

#Context processors get extecuted before loading any html template/view.
def get_cats(request):
    cat_menu = Category.objects.all()
    cats=[]
    for cat in cat_menu:
        cats.append(cat)
    return {
        "cats": cats
    }
