from django.core.paginator import Paginator

def paginate(userlist,request):
     p = Paginator(userlist, 20)
     page = request.GET.get('page')
     users = p.get_page(page)
     return users