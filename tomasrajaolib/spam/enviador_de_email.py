class Enviador:

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in destinatario:
            raise EmailInvalido(f'Email de destinatário inválido: {destinatario}')
        return destinatario

class EmailInvalido(Exception):
    pass
