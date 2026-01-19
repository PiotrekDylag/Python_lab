from kursy_walut import pobierz_cene_euro


def test_pobierz_cene_euro(mocker):
    # fałszywe dane jak z API NBP
    fake_response = {
        "rates": [
            {"mid": 4.50}
        ]
    }

    # mock obiektu response
    mock_response = mocker.Mock()
    mock_response.json.return_value = fake_response

    # podmiana requests.get
    mocker.patch(
        "kursy_walut.requests.get",
        return_value=mock_response
    )

    wynik = pobierz_cene_euro()

    assert wynik == 4.50
