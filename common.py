from typing import Optional, Any

import json
import logging
import pydantic

import spacy
import spacy.tokens
import numpy as np
import streamlit as st

from spacy import displacy
from spacy.displacy import render


class DataEntry(pydantic.BaseModel):
    ner_tags: list[str]
    tokens: list[str]
    space_after: Optional[list[bool]] = None


class State:
    def __init__(self) -> None:
        logging.info("State.__init__")


def get_state() -> State:
    if "state" not in st.session_state:
        print("WARNING: new state created")
        st.session_state["state"] = State()

    return st.session_state["state"]


# ner/lib/python3.11/site-packages/spacy/displacy/templates.py
TPL_ENT = """
<mark class="entity" style="background: {bg}; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">
    {text}
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem">{label}{kb_link}</span>
</mark>
"""

# ner/lib/python3.11/site-packages/spacy/displacy/render.py
DEFAULT_LABEL_COLORS = {
    "ORG": "#7aecec",
    "PRODUCT": "#bfeeb7",
    "GPE": "#feca74",
    "LOC": "#ff9561",
    "PERSON": "#aa9cfc",
    "NORP": "#c887fb",
    "FAC": "#9cc9cc",
    "EVENT": "#ffeb80",
    "LAW": "#ff8197",
    "LANGUAGE": "#ff8197",
    "WORK_OF_ART": "#f0d0ff",
    "DATE": "#bfe1d9",
    "TIME": "#bfe1d9",
    "DATETIME": "#bfe1d9",
    "MONEY": "#e4e7d2",
    "QUANTITY": "#e4e7d2",
    "ORDINAL": "#e4e7d2",
    "CARDINAL": "#e4e7d2",
    "PERCENT": "#e4e7d2",
    "NUMERIC": "#cccccc",
}


def display_text(doc: spacy.tokens.Doc):
    return displacy.render(doc, style="ent", jupyter=False)


def get_model() -> spacy.Language:
    model = spacy.load("./output3/model-best/")
    return model


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, bytes):
            return str(obj)
        return json.JSONEncoder.default(self, obj)
