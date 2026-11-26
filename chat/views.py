
import os
from django.shortcuts import render
from dotenv import load_dotenv
from google import genai

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Carrega as variáveis do arquivo .env
load_dotenv()

# Recupera a chave da API
API_KEY = os.getenv("GEMINI_API_KEY")

# Cria o cliente Gemini
client = genai.Client(api_key=API_KEY) if API_KEY else None


def home(request):
    return render(request, "index.html")


@api_view(["POST"])
def chat_api(request):
    mensagem = request.data.get("message", "").strip()

    if not mensagem:
        return Response(
            {"erro": "Digite uma mensagem."},
            status=400
        )

    if client is None:
        return Response(
            {"erro": "Chave da API Chat Misael não configurada."},
            status=500
        )

    try:
        resposta = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=mensagem
        )

        return Response({
            "response": resposta.text
        })

    except Exception as erro:
        print(f"Erro ao consultar Chat Misael : {erro}")

        return Response(
            {
                "erro": "O Chat Misael está temporariamente indisponível. Tente novamente."
            },
            status=503
        )