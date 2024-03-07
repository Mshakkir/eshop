from . models import category
def menu_links(request):
    try:
        links = category.objects.all()
    except category.DoesNotExist:
        links=[]
    return {'links': links}