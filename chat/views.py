
import os
import re
from django.shortcuts import render
from dotenv import load_dotenv
from google import genai
from rest_framework.decorators import api_view
from rest_framework.response import Response


#Utilizando o function calling para conectar ia ao orm
from metricas.views import listar_vendedores
from google.genai import types





# Carrega as variáveis do arquivo .env
load_dotenv()

# Recupera a chave da API
API_KEY = os.getenv("GEMINI_API_KEY")

# Cria o cliente Gemini
client = genai.Client(api_key=API_KEY) if API_KEY else None


def chat(request):
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
            model="gemini-3.1-flash-lite",
            contents=mensagem,
            config=types.GenerateContentConfig(
                tools=[listar_vendedores],
                system_instruction=(
                                "Você é o Chat Misael. "
                "Responda sempre em português. "

                "Quando o usuário perguntar quantos vendedores estão cadastrados "
                "ou pedir para listar os vendedores, utilize a ferramenta "
                "listar_vendedores e informe somente a quantidade e os nomes. "
                "Não mostre as metas nesses casos. "

                "Quando o usuário perguntar especificamente sobre metas, "
                "utilize a ferramenta listar_vendedores e informe as metas "
                "correspondentes. "

                "Não invente informações. Utilize somente os dados retornados "
                "pela ferramenta."
                )
            )
        )
        texto = resposta.text

        # Remove os ** do negrito
        texto = re.sub(r'\*\*(.*?)\*\*', r'\1', texto)

        return Response({
            "response": texto
        })
    except Exception as erro:
        print(f"Erro ao consultar Chat Misael : {erro}")

        return Response(
            {
                "erro": "O Chat Misael está temporariamente indisponível. Tente novamente."
            },
            status=503
        )
