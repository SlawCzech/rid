from pathlib import Path
import pandas as pd
import datetime as dt

from ania_rid.prompts.pydantic_review import QuantitativeReviewEntry, MethodologyEntry


def _obj_to_row_dict(entry: "MethodologyEntry") -> dict:
    d = entry.model_dump(by_alias=True, exclude_none=False)
    def to_str(v):
        if v is None:
            return "brak danych"
        if isinstance(v, (list, tuple)):
            return ", ".join(map(str, v))
        return str(v)
    return {k: to_str(v) for k, v in d.items()}

def _extract_parsed_entry(response) -> "MethodologyEntry":
    parsed = getattr(response, "output_parsed", None)
    if parsed is not None:
        from pydantic import BaseModel
        if isinstance(parsed, BaseModel):
            return parsed
        return MethodologyEntry.model_validate(parsed)

    out = getattr(response, "output", []) or []
    for item in out:
        content = getattr(item, "content", []) or []
        for part in content:
            maybe = getattr(part, "parsed", None)
            if maybe is not None:
                try:
                    maybe.model_dump
                    return maybe
                except Exception:
                    pass
                return MethodologyEntry.model_validate(maybe)

    raise ValueError("Nie znaleziono zparsowanego obiektu w odpowiedzi.")

def save_response_to_excel(response, filename: str = f"{dt.datetime.now()}.xlsx") -> str:
    entry = _extract_parsed_entry(response)
    row = _obj_to_row_dict(entry)

    columns = [(fld.alias or name) for name, fld in MethodologyEntry.model_fields.items()]

    df = pd.DataFrame([row], columns=columns)
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(filename, index=False)
    return filename

