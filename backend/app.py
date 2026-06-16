from flask import Flask, request, jsonify
from flask_cors import CORS

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Denuncia
from config import DATABASE_URL

from email_service import enviar_email_denuncia

from datetime import datetime
import random

app = Flask(__name__)

CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True
)

# ==========================================
# CONEXÃO COM O BANCO
# ==========================================

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# ==========================================
# GERADOR DE PROTOCOLO
# ==========================================

def gerar_protocolo(tipo):

    agora = datetime.now()

    data = agora.strftime("%Y%m%d")
    hora = agora.strftime("%H%M%S")

    randomico = random.randint(1000, 9999)

    return f"{tipo[:3]}-{data}-{hora}-{randomico}"

# ==========================================
# ROTA INICIAL
# ==========================================

@app.route("/")
def home():
    return "API Reclame funcionando!"

# ==========================================
# RECEBER DENÚNCIA
# ==========================================

@app.route("/api/denuncia", methods=["POST"])
def receber_denuncia():

    try:

        dados = request.get_json()

        print("\n==============================")
        print("DADOS RECEBIDOS:")
        print(dados)
        print("==============================\n")

        print("TIPO:", dados.get("tipo"))
        print("EMAIL:", dados.get("email"))
        print("RELATO:", dados.get("relato"))

        tipo = dados.get("tipo")
        email = dados.get("email")
        relato = dados.get("relato")

        protocolo = gerar_protocolo(tipo)

        session = Session()

        nova_denuncia = Denuncia(

            # CAMPOS PRINCIPAIS
            protocolo=protocolo,
            tipo=tipo,

            categoria_ia="Pendente",
            prioridade="Média",

            email=email,
            relato=relato,

            dados_criptografados="Pendente",

            # ==================================
            # ASSÉDIO
            # ==================================

            assediado=dados.get("assediado"),
            assediador=dados.get("assediador"),
            ocupacao=dados.get("ocupacao"),
            local_ocorrencia=dados.get("local_ocorrencia"),
            data_ocorrencia=dados.get("data_ocorrencia"),
            hora_ocorrencia=dados.get("hora_ocorrencia"),

            # ==================================
            # ALUNO
            # ==================================

            curso=dados.get("curso"),
            aluno_denunciado=dados.get("aluno_denunciado"),

            # ==================================
            # PROFESSOR
            # ==================================

            nome_professor=dados.get("nome_professor"),
            disciplina=dados.get("disciplina"),

            # ==================================
            # TÉCNICO
            # ==================================

            nome_tecnico=dados.get("nome_tecnico"),

            # ==================================
            # INFRAESTRUTURA
            # ==================================

            area_infraestrutura=dados.get("area_infraestrutura")
        )

        session.add(nova_denuncia)

        session.commit()
        
        enviar_email_denuncia(
        protocolo,
        tipo,
        relato
        )

        session.close()

        return jsonify({
            "status": "sucesso",
            "mensagem": "Denúncia salva com sucesso!",
            "protocolo": protocolo
        })

    except Exception as erro:

        return jsonify({
            "status": "erro",
            "mensagem": str(erro)
        }), 500

# ==========================================
# INICIAR SERVIDOR
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)