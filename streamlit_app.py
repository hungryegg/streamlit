import pandas as pd
import streamlit as st

st.title( "Financial Dashboard" )
st.write( "Let's start building!" )

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
