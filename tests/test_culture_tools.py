from travel_assistant.tools.culture_tools import get_local_culture_info


def test_get_local_culture_info_paris():
    """Prueba que la herramienta devuelva los datos correctos de Paris"""
    resultado = get_local_culture_info("Paris")
    assert "Croissant" in resultado
    assert "Bonjour" in resultado
    assert "Merci" in resultado

def test_get_local_culture_info_default():
    """Prueba el comportamiento por defecto con cualquier otra ciudad"""
    resultado = get_local_culture_info("Madrid")
    assert "Cultura Local - Madrid" in resultado