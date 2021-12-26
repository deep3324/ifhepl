from django.shortcuts import render


def ads(request):
    return render(request, "ads.txt")


def maintainance(request):
    return render(request, "maintainance.html")


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request, exception):
    return render(request, '500.html', status=500)
