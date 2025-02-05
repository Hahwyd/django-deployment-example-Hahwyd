from ninja import NinjaAPI

api = NinjaAPI(title="Example Project - DCI")


# Please note we are using this to get something quick
# In the course, our focus has been Django Restframework
# django-ninja is a cool API project as well.

@api.get('/')
def index(request):
    return {'message': 'This works!!!'}