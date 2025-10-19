REVIEW_JSON_SCHEMA = {
    "name": "quantitative_review_entry",
    "schema": {
        "type": "object",
        "properties": {
            "Autor": {"type": "string"},
            "Tytuł": {"type": "string"},
            "Rok": {"type": "string"},
            "Cel_badan": {"type": "string"},
            "Kraj": {"type": "string"},
            "Baza_teoretyczna": {"type": "string"},
            "Tematyka": {"type": "string", "enum": ["Z","E","S","D","Z+D","E+D","S+D","E+S+D","brak danych"]},
            "Źródło_danych": {"type": "string", "enum": ["P","W","P+W","brak danych"]},
            "Źródło_danych_wtórnych": {"type": "string"},
            "Metoda": {"type": "string"},
            "Narzędzie_skala": {"type": "string"},
            "Dostępność_narzędzia": {"type": "string", "enum": ["Tak","Nie","brak danych"]},
            "Wielkość_próby": {"type": "string"},
            "Metoda_analizy": {"type": "string"},
            "Reprezentatywność": {"type": "string", "enum": ["Tak","Nie","Nie wiadomo","N/A","brak danych"]},
            "Wnioski_istotne": {"type": "string"},
            "Kierunki_dalszych_badań": {"type": "string"},
            "Czy_się_wpisujemy": {"type": "string", "enum": ["Tak","Nie","Nie wiadomo","N/A","brak danych"]},
            "Przydatność_przeglądu": {"type": "integer"},
            "Przydatność_hipotez": {"type": "integer"},
            "Przydatność_metodyki": {"type": "integer"},
            "Przydatność_dyskusji": {"type": "integer"},
            "Źródła_dalsze": {"type": "string", "enum": ["Tak","Nie","brak danych"]},
            "Źródło_link": {"type": "string"},
            "Luka_badawcza": {"type": "string"},
            "Ograniczenia_badań": {"type": "string"}
        },
        "required": [
            "Autor","Tytuł","Rok","Cel_badan","Kraj","Tematyka",
            "Źródło_danych","Metoda","Przydatność_przeglądu"
        ]
    }
}