from django.shortcuts import render

# Create your views here.

def help(request):
    help_dict = {"help_notification": "Need help finding something?"}
    return render(request, "help/help.html", context=help_dict)