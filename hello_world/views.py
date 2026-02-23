from django.shortcuts import render


def home_page_view(request):
    """Render the homepage using a template."""
    context = {
        'title': 'Home',
    }
    return render(request, 'hello_world/index.html', context)