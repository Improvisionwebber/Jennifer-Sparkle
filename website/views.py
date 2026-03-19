from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    if request.method == 'POST':
        # Handle form submission here
        # e.g. send email, save to database, etc.
        pass
    return render(request, 'contact.html')