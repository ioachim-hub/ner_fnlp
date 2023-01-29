import json

import streamlit as st

from common import get_model, display_text, NpEncoder, State

model = get_model()


def render(state: State) -> None:
    st.header("NER tagging :label:")

    text = st.sidebar.text_area(
        label="Insert your text: ", placeholder="Ana are mere", height=200
    )

    if text:
        st.markdown("### :brain: Model prediction: ")
        doc = model(text)
        tags_ = set([ent.label_ for ent in doc.ents])

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

        data = doc.to_dict()
        del data["user_data_values"]
        del data["user_data_keys"]

        st.sidebar.download_button(
            label="Download prediction",
            file_name="data.json",
            mime="application/json",
            data=json.dumps(data, cls=NpEncoder),
        )
