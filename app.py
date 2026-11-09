import streamlit as st
jawaban = st.text_input ("blay abng ad pertanyaan. siap? ya atau tidak")
if jawaban == "ya":
  pertanyaan2 = st.text_input ("menurut blay abang bisa ndak nge program? mano bisa atau bisa")
if pertanyaan2 == "bisa":
  pertanyaan3 = st.text_input ("kalau bisa dik bng apo? mbo cain kakak-kakak untuk abng atau traktir mbo jajan")
if pertanyaan3 == "mbo cain kakak-kakak untuk abng":
  st.write ("wkwkwk wleee bisa bng kau")
