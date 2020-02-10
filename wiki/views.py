from django.shortcuts import render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


class PageList(ListView):
    """
    CHALLENGES:
      1. On GET, display a homepage that shows all Pages in your wiki.
      2. Replace this CHALLENGE text with a descriptive docstring for PageList.
      *A page is rendered that shows all of the existng pages in the Django admin database.*
      3. Replace pass below with the code to render a template named `list.html`.
    """
    model = Page
    page_object_name = "wiki"
    template_name = "list.html"

    def get(self, request):
        """ Returns a list of wiki pages. """
        page = {
          'wiki': Page.objects.all()
        }
        return render(request, 'list.html', page)


class PageDetailView(DetailView):
    """
    CHALLENGES:
      1. On GET, render a template named `page.html`.
      2. Replace this docstring with a description of what this accomplishes.
      *A page is rendered with a specific topic tht was input in the Django admin database.*

    STRETCH CHALLENGES:
      1. Import the PageForm class from forms.py.
          - This ModelForm enables editing of an existing Page object in the database.
      2. On GET, render an edit form below the page details.
      3. On POST, check if the data in the form is valid.
        - If True, save the data, and redirect back to the DetailsView.
        - If False, display all the errors in the template, above the form fields.
      4. Instead of hard-coding the path to redirect to, use the `reverse` function to return the path.
      5. After successfully editing a Page, use Django Messages to "flash" the user a success message
           - Message Content: REPLACE_WITH_PAGE_TITLE has been successfully updated.
    """
    model = Page
    page_object_name = "article"
    template_name = "page.html"


    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """
        page = {
          'article': Page.objects.get(slug=slug)
        }
        return render(request, 'page.html', page)

    def post(self, request, slug):
        pass
