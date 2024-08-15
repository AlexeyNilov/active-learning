from data.words import get_known_verbs


def test_get_known_verbs():
    data = get_known_verbs()
    assert data[:2] == ['hacer', 'hablar']
