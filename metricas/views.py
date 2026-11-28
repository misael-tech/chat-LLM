from django.shortcuts import render,redirect
from .models import Vendedor
# Create your views here.


def cad_vendedor(request):

    if request.method == "POST":
        nome = request.POST.get('nome')
        meta = request.POST.get('meta')

        Vendedor.objects.create(
            nome=nome,
            meta=meta
        )
        return redirect('cadastrar_vendedor')

    vendedores = Vendedor.objects.all()

    return render(request, 'vendedores.html', {
        'vendedores': vendedores
    })


def listar_vendedores() -> list:
    """
    Lista os vendedores cadastrados e suas metas.
    """

    vendedores = Vendedor.objects.all()

    return [
        {
            "id": vendedor.id,
            "nome": vendedor.nome,
            "meta": str(vendedor.meta)
        }
        for vendedor in vendedores
    ]
