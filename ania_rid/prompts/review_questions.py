REVIEW_QUESTIONS = """
You must extract structured information from the provided academic article (PDF text)
according to the fields listed below.

Each field should be answered **in Polish** and follow the indicated type:
- "open" = short free-text answer based only on the article content
- "choice" = choose *one or more* values from the given list (if uncertain, write "brak danych")

Return answers **only as JSON** strictly following the schema.

Fields:

1. Autor — type: open  
2. Tytuł — type: open  
3. Rok — type: open  
4. Cel art./badań — type: open  
5. Kraj (badany) — type: open  
6. Baza teoretyczna — type: open  

7. Tematyka - powiązanie z nami — type: choice  
    Z zaangażowanie w S.C. ogólnie – poziom, przejawy, wymiary
    E proekologiczne zaangażowanie
    S prospołeczne zaangażowanie
    D determinanty zaangażowania (stymulanty, bariery)

   options: ["Z", "E", "S", "D", "Z+D", "E+D", "S+D", "E+S+D"]  

8. Źródło danych — type: choice  
    P pierwotne
    W wtórne
   options: ["P", "W", "P+W"]  

9. Źródło danych wtórnych (jeśli dotyczy) — type: open  

10. Metoda/technika — type: choice  
    options: [
      "Wywiad standaryzowany (PI/CAPI)",
      "Ankieta osobista (PAPI)",
      "Ankieta online (CAWI)",
      "Ankieta telefoniczna (CATI)",
      "Inna ankieta (mailowa, intercept)",
      "Ankieta audytoryjna",
      "Netografia",
      "Eksperyment rynkowy",
      "Eksperyment laboratoryjny",
      "inne"
    ]

11. Narzędzie/skala — type: open  
12. Dostępność narzędzia — type: choice ["Tak", "Nie"]  
13. Wielkość próby — type: open  
14. Główna metoda analizy danych — type: open  
15. Reprezentatywność badania — type: choice ["Tak", "Nie", "Nie wiadomo", "N/A"]  

16. Wnioski istotne dla nas — type: open  
17. Kierunki dalszych badań — type: open  
18. Czy się wpisujemy w te kierunki — type: choice ["Tak", "Nie", "Nie wiadomo", "N/A"]  

19. Przydatność do przeglądu — type: choice [0, 1, 2, 3]  
20. Przydatność do hipotez — type: choice [0, 1, 2, 3]  
21. Przydatność do metodyki (skala, konstrukt) — type: choice [0, 1, 2, 3]  
22. Przydatność do dyskusji — type: choice [0, 1, 2, 3]  

23. Czy są źródła do dalszego wyszukiwania — type: choice ["Tak", "Nie"]  
25. Luka badawcza (jeśli jest wskazana) — type: open  
26. Ograniczenia badań — type: open
"""