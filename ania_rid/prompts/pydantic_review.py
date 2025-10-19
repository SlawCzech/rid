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