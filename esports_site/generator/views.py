from django.shortcuts import render

from django.core.management import call_command

def generate(request):
    if request.method == "POST":
        call_command("generate_pages")
        return render(request, "success.html")

    return render(request, "generate.html")


def today(request):
    return render(request, "today.html")

def yesterday(request):
    return render(request, "yesterday.html")

def tomorrow(request):
    return render(request, "tomorrow.html")