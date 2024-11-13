
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return render(
        request,
        'whitelabel/pages/index.html'
    )
@csrf_exempt
def send_email_view(request):
    success = False
    error_message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        setor = request.POST.get('setor')
        message = request.POST.get('message')

        user_ip = request.META.get('REMOTE_ADDR')

        # Conteúdo do email
        subject = f"Novo contato de {name}"
        content = (
            f"Nome: {name}\n"
            f"Email: {email}\n"
            f"Telefone: {phone}\n"
            f"Setor: {setor}\n"    
            f"Mensagem:\n{message}\n"
            f"IP: {user_ip}"
        )
        try:
            send_mail(
                subject,
                content,
                settings.DEFAULT_FROM_EMAIL,
                ['gouberg@gmail.com'],
                fail_silently=False,
            )
            success = True
        
        except Exception as e:

            error_message =  f'Ocorreu um erro ao enviar o e-mail: {e}'

        
        #return redirect('index')  # Mude 'index' para a view/página que você deseja redirecionar
    return render(request, 'whitelabel/pages/index.html', {'success': success, 'error_message': error_message})