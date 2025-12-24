# ➡️ Nenhuma regra de negócio
# ➡️ Apenas efeito colateral técnico


class EmailService:
    def send_welcome(self, email: str):
        print(f"[EMAIL] Bem-Vindo! E-mail enviado para {email}")