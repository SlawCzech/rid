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

METHODOLOGY_QUESTIONS = """
You must extract structured information from the provided academic article (PDF text)
according to the methodology-related fields listed below.

Each field should be answered **in English** and follow the indicated type:
- "open" = short free-text answer based only on the article content (if missing, write "NP")
- "choice" = choose one value from the given list (if missing/uncertain, use "NP" if available)

Return answers **only as JSON** strictly following the schema.

General rule:
- If the article does not provide the required information, answer "NP".
- Do NOT invent or guess information.

Fields:

1. Quantitative — type: choice
   Is a quantitative research design used?
   options: ["Y", "N", "NP"]

2. Qualitative — type: choice
   Is a qualitative research design used?
   options: ["Y", "N", "NP"]

3. Primary — type: choice
   Are primary data collected by the authors?
   options: ["Y", "N", "NP"]

4. Secondary — type: choice
   Are secondary data used (existing datasets, reports, statistics, etc.)?
   options: ["Y", "N", "NP"]

5. SEC_source1 — type: open
   First source of secondary data (if any) – e.g. database, report, institution, prior study.
   If not provided, write "NP".

6. SEC_source2 — type: open
   Second source of secondary data (if any).
   If no second source or not provided, write "NP".

7. METHOD1 — type: open
   Main data collection method/technique (e.g. survey, interview, experiment, CAWI, CATI, PAPI).
   Use English names or common abbreviations. If not provided, write "NP".

8. METHOD2 — type: open
   Second data collection method/technique (if applicable).
   If there is only one or not specified, write "NP".

9. SCALE1 — type: open
   Name/label of the first measurement scale used specifically to measure consumer engagement in the supply chain (SC).
   If there is no such scale or it is not specified, write "NP".

10. SCALE2 — type: open
    Name/label of the second scale for consumer engagement in SC (if any).
    If there is no second scale, write "NP".

11. SCALE1_type — type: open
    Type and length of the first scale (e.g. "Likert 5-point", "Likert 7-point", etc.).
    If not provided, write "NP".

12. SCALE1_source — type: open
    Source of the first scale:
    - If it is an own/author-developed scale, write "Own".
    - If it is adopted/adapted from other authors, paste the citation or description.
    If not provided, write "NP".

13. RELIABILITY — type: choice
    Was the reliability of the scale(s) tested?
    options: ["Y", "N", "NP"]

14. RELIABILITY_how — type: open
    How was reliability tested? For example: "Cronbach's alpha", "test–retest", "composite reliability", "AVE", etc.
    If not provided, write "NP".

15. SAMPLE_N — type: open
    Sample size N (numeric value, or description if necessary).
    If not provided, write "NP".

16. SAMPLE_method — type: open
    Sampling method (e.g. random sampling, convenience sampling, quota sampling, snowball sampling).
    If not provided, write "NP".

17. SAMPLE_quotas — type: open
    If quota sampling is used, specify the quota criteria (e.g. age, gender, region).
    If not applicable or not provided, write "NP".

18. PILOT_study — type: choice
    Was a pilot study conducted?
    options: ["Y", "N", "NP"]

19. SAMPLE_represent — type: choice
    Do the authors claim that the sample is representative?
    options: ["Y", "N", "NP"]

20. ANALYSIS1 — type: open
    First/main method of data analysis (e.g. regression, SEM, PLS-SEM, ANOVA, CFA, t-test, cluster analysis).
    If not provided, write "NP".

21. ANALYSIS2 — type: open
    Second data analysis method (if any).
    If there is only one or not specified, write "NP".

22. MODEL_tested — type: choice
    Do the authors explicitly test a conceptual/statistical model?
    options: ["Y", "N", "NP"]

23. TESTED_how — type: open
    How is the model tested? Provide the method/approach (e.g. "PLS-SEM", "covariance-based SEM", "multiple regression").
    If not provided, write "NP".

24. NEW_METHODS — type: open
    What do the authors say in the limitations and future research sections regarding methodology?
    Paste the relevant fragments or concise paraphrases in English.
    If there are no explicit methodological recommendations or they are not provided, write "NP".
"""