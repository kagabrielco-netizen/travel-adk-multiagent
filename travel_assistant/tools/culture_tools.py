def get_local_culture_info(destination: str) -> str:
    """Obtiene informacion cultural, platos tipicos, costumbres y frases utiles de un destino.

    Args:
        destination: El nombre de la ciudad o pais de destino.
    """
    destination_lower = destination.lower()

    if "paris" in destination_lower or "francia" in destination_lower:
        return """Cultura Local - Paris, Francia:
- Platos tipicos: Croissant, Coq au vin, Ratatouille, Escargots.
- Costumbres: Saludar siempre con un 'Bonjour' al entrar a una tienda.
- Frases utiles: 'S'il vous plait' (Por favor), 'Merci' (Gracias)."""

    elif "tokio" in destination_lower or "japon" in destination_lower:
        return """Cultura Local - Tokio, Japon:
- Platos tipicos: Sushi, Ramen, Tempura, Takoyaki.
- Costumbres: No se deja propina (es una falta de respeto). Reverencia al saludar.
- Frases utiles: 'Arigatou gozaimasu' (Muchas gracias), 'Sumimasen' (Disculpe)."""

    else:
        return f"""Cultura Local - {destination}:
- Platos tipicos: Gastronomia tradicional de la region y mercados locales.
- Costumbres: Respetar los horarios comerciales y codigos de vestimenta locales.
- Frases utiles: 'Por favor', 'Gracias' y 'Buenos dias' en el idioma local."""