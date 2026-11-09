import streamlit as st
jawaban = st.text_input ("blay abng ad pertanyaan. siap? ya atau tidak")
while jawaban != "tidak":
  jawaban = st.text_input ("blay abng ad pertanyaan. siap? ya atau tidak")
if jawaban == "ya":
  pertanyaan2 = st.text_input ("menurut blay abang bisa ndak nge program? mano bisa atau bisa")
while pertanyaan2 != "mano bisa":
  pertanyaan2 = st.text_input ("menurut blay abang bisa ndak nge program? mano bisa atau bisa")
if pertanyaan2 == "bisa":
  pertanyaan3 = st.text_input ("kalau bisa dik bng apo? mbo cain kakak-kakak untuk abng atau traktir mbo jajan")
while pertanyaan3 != "traktir mbo jajan":
  pertanyaan3 = st.text_input ("kalau bisa dik bng apo? mbo cain kakak-kakak untuk abng atau traktir mbo jajan")
print("wkwkwk wleee bisa bng kau")
