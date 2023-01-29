import logging

import streamlit as st

from datetime import datetime

from app import ner_tagging, ner_main, ner_comparing
from app.common import get_state


def init_logging() -> None:
    logging.basicConfig(level=logging.DEBUG)


def main() -> None:
    init_logging()
    state = get_state()

    PAGES = {
        "Main": ner_main.render,
        "Tagging": ner_tagging.render,
        "Comparing": ner_comparing.render,
    }

    st.sidebar.title("Navigation")
    st.sidebar.write("Time: {}".format(datetime.now()))
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    if selection is None:
        selection = "Main"

    page = PAGES[selection]
    page(state)


if __name__ == "__main__":
    st.set_page_config(page_title="NER", layout="wide")
    main()
