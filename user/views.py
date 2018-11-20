from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render

from servidores.models import Servidor
from user.forms import UserForm
from user.models import User


# Create your views here.


def cadastro_usuario(request):
    form = UserForm(request.POST, None)
    if form.is_valid():
        form.siape = request.POST.get('siape')
        form.email = request.POST.get('email')

        servidor = Servidor.objects.filter(siape=form.siape).filter(email=form.email).first()

        if servidor:
            user_servidor = User.objects.filter(servidor=servidor).first()

            if user_servidor is None:
                novo_usuario = User.objects.create_user(
                    email=servidor.email,
                    first_name=servidor.nome,
                    last_name=servidor.sobrenome,
                    username=servidor.email.split('@')[0],
                    servidor=servidor,
                    password=servidor.siape)

                novo_usuario.save()

                set_password_form = PasswordResetForm({'email': novo_usuario.email})
                if set_password_form.is_valid():
                    print
                    'Reset Form Is Valid'
                    set_password_form.save(
                        request=request,
                        use_https=False,
                        from_email="simplegp2018@gmail.com",
                        subject_template_name='registration/criar_senha_subject.txt',
                        email_template_name='registration/criar_senha.html')
                return confirmacao_cadastro(request)
            else:
                # Já existe usuário, sugere avisa cliente e sugere redefinição de senha.
                return render(request, 'users/cadastro_duplicado.html')

        else:
            return render(request, 'users/erro_cadastro.html')

    return render(request, 'users/cadastro_user.html', {'form': form})


def confirmacao_cadastro(request):
    return render(request, 'users/confirmacao_cadastro.html')
