from unittest.mock import Mock

import pytest

from tomasrajaolib import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/8079830?v=4'
    resp_mock.json.return_value = {
        'login': 'tomas', 'id': 10574,
        'avatar_url': url
    }
    get_mock = mocker.patch('tomasrajaolib.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('tomasrajao')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('tomasrajao')
    assert 'https://avatars.githubusercontent.com/u/80798306?v=4' == url
