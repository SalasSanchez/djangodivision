from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import DivisionForm

# This loads the about page
class AboutPageView(TemplateView):
    template_name = 'about.html'


# This loads the home page and processes the data from the form, when it sends a request.
def new_division(request):
    if request.method == 'POST':
        form = DivisionForm(request.POST)
        if form.is_valid():
            division = form.cleaned_data
            # Checking for a 0 divisor, as the built-in checks in is_valid() do not cover this case.
            if division['divisor'] == 0:
                message = 'Dividing anything by 0 is undefined'
                return render(request, 'base.html', {'form': form, 'message': message})
            else:
                division['result'] = get_result(division['dividend'], division['divisor'])
                form = DivisionForm()
                return render(request, 'base.html', {'division': division, 'form': form})
        else:
            message = "Make sure you enter only numbers"
            return render(request, 'base.html', {'form': form, 'message': message})
    else:
        form = DivisionForm()
        return render(request, 'base.html', {'form': form})


# This is a utility method to perform the division. If it required any database
# calls or any more heavy-duty processing of the data, it would have to be under a model in models.py
def get_result(dividend, divisor):
    return dividend/divisor

