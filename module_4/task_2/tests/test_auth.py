def test_get_token(auth_session):
    """Тест для проверки получения токена"""
    assert auth_session is not None, "Не удалось создать сессию с токеном"
    print("Токен успешно получен и добавлен в сессию.")


