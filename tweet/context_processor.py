#add context (or {{ variables }}) to the each request
#so that every template can access it with passing each time seperately in render

#we need to give this context processors as a middleware in django(settings)
# in templates options

from .forms import SearchForm

def search_form(request):
    form = SearchForm()
    return { 'search_form' : form }
