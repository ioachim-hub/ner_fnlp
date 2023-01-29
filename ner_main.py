import streamlit as st

from common import State


def render(state: State) -> None:
    st.header("NER playground application")

    st.markdown("""
        **Named-entity recognition (NER)** (also known as **(named) entity identification**, **entity chunking**, and **entity extraction**) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.

Most research on NER/NEE systems has been structured as taking an unannotated block of text, such as this one:

Jim bought 300 shares of Acme Corp. in 2006.

And producing an annotated block of text that highlights the names of entities:

<div class="entities" style="line-height: 2.5; direction: ltr;">
<mark class="entity" style="background: rgb(170, 156, 252); padding: 0.45em 0.6em; margin: 0px 0.25em; line-height: 1; border-radius: 0.35em;">
    Jim
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem;">PERSON</span>
</mark>
 bought 
<mark class="entity" style="background: rgb(235, 64, 52); padding: 0.45em 0.6em; margin: 0px 0.25em; line-height: 1; border-radius: 0.35em;">
    300
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem;">NUMERIC</span>
</mark>
 shares of 
<mark class="entity" style="background: rgb(122, 236, 236); padding: 0.45em 0.6em; margin: 0px 0.25em; line-height: 1; border-radius: 0.35em;">
    Acme Corp
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem;">ORG</span>
</mark>
 in 
<mark class="entity" style="background: rgb(191, 225, 217); padding: 0.45em 0.6em; margin: 0px 0.25em; line-height: 1; border-radius: 0.35em;">
    2006
    <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem;">DATETIME</span>
</mark>
.</div>

In this example, a person name consisting of one token, a two-token company name and a temporal expression have been detected and classified.

State-of-the-art NER systems for English produce near-human performance. For example, the best system entering MUC-7 scored ***93.39%*** of F-measure while human annotators scored ***97.60%*** and ***96.95%***.

    """, unsafe_allow_html=True)

    st.markdown("""
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>""", unsafe_allow_html=True)
    st.markdown("""
    Authors:
    * :woman: Raluca Tudor (raluca.tudor@s.unibuc.com)
    * :man: Liviu Sopos (liviu.sopos@s.unibuc.com)
    * :man: Ioachim Lihor (ioachim.lihor@s.unibuc.com)
    """)
