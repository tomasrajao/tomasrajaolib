import pytest

from tomasrajaolib.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['luciano@python.pro.br', 'foo@bar.com.br'],
)
def test_destinatario(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        'renzo@python.pro.br',
        destinatario,
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert destinatario in resultado



@pytest.mark.parametrize(
    'destinatario',
    ['', 'foobar.com.br'],
)
def test_destinatario_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            'renzo@python.pro.br',
            destinatario,
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta.'
        )
