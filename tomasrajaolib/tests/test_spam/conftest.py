import pytest

from tomasrajaolib.spam.db import Conexao


@pytest.fixture(scope='module')  # Escopo de teste('function', 'module', 'session')
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj  # função geradora (vide: generators)
    # Teardown
    conexao_obj.fechar()


@pytest.fixture()
def sessao(conexao):
    # Setup
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    # Teardown
    sessao_obj.roll_back()
    sessao_obj.fechar()