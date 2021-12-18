from django.shortcuts import render


def home_page(request):
    context = {}
    return render(request, 'home.html', context)


def header(request):
    context = {}
    return render(request, 'header.html', context)


"""
temporarily the footer dose not have any content
"""


def footer(request):
    context = {}
    return render(request, 'footer.html', context)
