from __future__ import annotations
from enum import StrEnum
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict, conint


# === Enumy zgodne ze schematem ===
class TematykaEnum(StrEnum):
    Z = "Z"
    E = "E"
    S = "S"
    D = "D"
    Z_D = "Z+D"
    E_D = "E+D"
    S_D = "S+D"
    E_S_D = "E+S+D"
    BRAK_DANYCH = "brak danych"


class ZrodloDanychEnum(StrEnum):
    P = "Pierwotne"
    W = "Wtórne"
    P_W = "Pierwotne + Wtórne"
    BRAK_DANYCH = "brak danych"


class TakNieEnum(StrEnum):
    TAK = "Tak"
    NIE = "Nie"
    BRAK_DANYCH = "brak danych"


class ReprezentatywnoscEnum(StrEnum):
    TAK = "Tak"
    NIE = "Nie"
    NIE_WIADOMO = "Nie wiadomo"
    NA = "N/A"
    BRAK_DANYCH = "brak danych"


class WpisujemyEnum(StrEnum):
    TAK = "Tak"
    NIE = "Nie"
    NIE_WIADOMO = "Nie wiadomo"
    NA = "N/A"
    BRAK_DANYCH = "brak danych"


# 0..3 dla pól „Przydatność…”
Score04 = conint(ge=0, le=3)


# === Model Pydantic ===
class QuantitativeReviewEntry(BaseModel):
    model_config = ConfigDict(populate_by_name=False)  # używamy aliasów z JSON-u przy I/O

    autor: str = Field(alias="Autor")
    tytul: str = Field(alias="Tytuł")
    rok: str = Field(alias="Rok")
    cel_badan: str = Field(alias="Cel_badan")
    kraj: str = Field(alias="Kraj")
    baza_teoretyczna: str = Field(alias="Baza_teoretyczna")

    tematyka: TematykaEnum = Field(alias="Tematyka")
    zrodlo_danych: ZrodloDanychEnum = Field(alias="Źródło_danych")

    zrodlo_danych_wtornych: Optional[str] = Field(default=None, alias="Źródło_danych_wtórnych")

    metoda: str = Field(alias="Metoda")
    narzedzie_skala: Optional[str] = Field(default=None, alias="Narzędzie_skala")
    dostepnosc_narzedzia: TakNieEnum | None = Field(default=None, alias="Dostępność_narzędzia")

    wielkosc_proby: Optional[str] = Field(default=None, alias="Wielkość_próby")
    metoda_analizy: Optional[str] = Field(default=None, alias="Metoda_analizy")

    reprezentatywnosc: ReprezentatywnoscEnum | None = Field(default=None, alias="Reprezentatywność")

    wnioski_istotne: Optional[str] = Field(default=None, alias="Wnioski_istotne")
    kierunki_dalszych_badan: Optional[str] = Field(default=None, alias="Kierunki_dalszych_badań")

    czy_sie_wpisujemy: WpisujemyEnum | None = Field(default=None, alias="Czy_się_wpisujemy")

    przydatnosc_przegladu: Score04 = Field(alias="Przydatność_przeglądu")
    przydatnosc_hipotez: Optional[Score04] = Field(default=None, alias="Przydatność_hipotez")
    przydatnosc_metodyki: Optional[Score04] = Field(default=None, alias="Przydatność_metodyki")
    przydatnosc_dyskusji: Optional[Score04] = Field(default=None, alias="Przydatność_dyskusji")

    zrodla_dalsze: TakNieEnum | None = Field(default=None, alias="Źródła_dalsze")
    zrodlo_link: Optional[str] = Field(default=None, alias="Źródło_link")

    luka_badawcza: Optional[str] = Field(default=None, alias="Luka_badawcza")
    ograniczenia_badan: Optional[str] = Field(default=None, alias="Ograniczenia_badań")





class YesNoNPEnum(StrEnum):
    Y = "Y"
    N = "N"
    NP = "NP"


class MethodologyEntry(BaseModel):
    """
    Model dopasowany do wyjścia z METHODOLOGY_QUESTIONS.
    Klucze JSON-owe (alias) są dokładnie takie jak w promptcie.
    """
    model_config = ConfigDict(populate_by_name=False)

    quantitative: YesNoNPEnum = Field(alias="Quantitative")
    qualitative: YesNoNPEnum = Field(alias="Qualitative")

    primary: YesNoNPEnum = Field(alias="Primary")
    secondary: YesNoNPEnum = Field(alias="Secondary")

    sec_source1: str = Field(alias="SEC_source1")
    sec_source2: str = Field(alias="SEC_source2")

    method1: str = Field(alias="METHOD1")
    method2: str = Field(alias="METHOD2")

    scale1: str = Field(alias="SCALE1")
    scale2: str = Field(alias="SCALE2")

    scale1_type: str = Field(alias="SCALE1_type")
    scale1_source: str = Field(alias="SCALE1_source")

    reliability: YesNoNPEnum = Field(alias="RELIABILITY")
    reliability_how: str = Field(alias="RELIABILITY_how")

    # Uwaga: tu przyjmujemy string, bo w JSON-ie może być liczba albo "NP"
    sample_n: str = Field(alias="SAMPLE_N")

    sample_method: str = Field(alias="SAMPLE_method")
    sample_quotas: str = Field(alias="SAMPLE_quotas")

    pilot_study: YesNoNPEnum = Field(alias="PILOT_study")
    sample_represent: YesNoNPEnum = Field(alias="SAMPLE_represent")

    analysis1: str = Field(alias="ANALYSIS1")
    analysis2: str = Field(alias="ANALYSIS2")

    model_tested: YesNoNPEnum = Field(alias="MODEL_tested")
    tested_how: str = Field(alias="TESTED_how")

    new_methods: str = Field(alias="NEW_METHODS")