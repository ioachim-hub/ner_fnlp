import json

import spacy.tokens
import streamlit as st

from app.common import get_model, display_text, NpEncoder, State, DataEntry

model = get_model()


def render(state: State) -> None:
    st.header("NER comparing :scales:")

    text_to_predict = st.sidebar.text_area(
        label="Insert your text: ", placeholder="Ana are mere", height=200
    )

    if text_to_predict:
        st.markdown("## :brain: Model prediction: ")
        doc = model(text_to_predict)
        tags_ = set([ent.label_ for ent in doc.ents])
        tags_checkbox_: dict[st.checkbox, str] = {}

        st.markdown("#### Tags found:")
        cols = st.columns(len(tags_))

        for col, tag in zip(cols, tags_):
            with col:
                if (
                    st.checkbox(
                        label=tag,
                        value=True,
                        label_visibility="visible",
                        key=f"prediction-{tag}",
                    )
                    is False
                ):
                    doc.ents = tuple([ent for ent in doc.ents if ent.label_ != tag])

        st.markdown("### Result:")
        # _, col1 = st.columns([1, 9])
        # with col1:
        st.markdown(display_text(doc=doc), unsafe_allow_html=True)

        data = doc.to_dict()
        del data["user_data_values"]
        del data["user_data_keys"]

        st.sidebar.download_button(
            label="Download prediction",
            file_name="data.json",
            mime="application/json",
            data=json.dumps(data, cls=NpEncoder),
        )

    st.markdown(
        """
    <br/>
    <br/>
    <br/>
    <br/>""",
        unsafe_allow_html=True,
    )

    file_correct = st.sidebar.file_uploader(label="Upload test entry")
    if file_correct:
        st.markdown("## :bulb: Correct labeled data: ")
        data_ = DataEntry.parse_obj(json.loads(file_correct.getvalue()))

        nlp = spacy.blank("ro")
        doc = spacy.tokens.Doc(
            nlp.vocab,
            words=data_.tokens,
            spaces=data_.space_after,
            ents=data_.ner_tags,
        )

        tags_ = set([ent.label_ for ent in doc.ents])
        tags_checkbox_: dict[st.checkbox, str] = {}

        st.markdown("#### Tags found:")
        cols = st.columns(len(tags_))

        for col, tag in zip(cols, tags_):
            with col:
                if (
                    st.checkbox(label=tag, value=True, label_visibility="visible")
                    is False
                ):
                    doc.ents = tuple([ent for ent in doc.ents if ent.label_ != tag])

        st.markdown("### Result:")
        # _, col1 = st.columns([1, 9])
        # with col1:
        st.markdown(display_text(doc=doc), unsafe_allow_html=True)
