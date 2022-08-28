from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def result(request):
    email = request.POST['email']
    if email:
        pos = email.index('@')
        user_name = email[:pos]
        domain_name = email[pos+1:]
        data = {'username': user_name, 'domainname': domain_name}
    else:
        error = "Please type your email in Email Field."
        data = {'error': error}
    
    
    return render(request, 'result.html', data)
