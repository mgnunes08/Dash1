


import pandas as pd
import streamlit as st






df2=pd.read_excel(r"C:\Users\Usuario\Downloads\Moneyball FM261.xlsm",sheet_name='🎯Armadores')

df2['MFG']=(df2['non Pen xG /90']+df2['Finalizações no gol/90']+df2['Ações que geraram finalizações ao gol /90'])/3

df2['MCR']=(df2['xA /90']+df2['Passes Decisivos /90']+df2['Chances de perigo criadas /90'])/3
indices=df2[['Jogador','MCR','MFG']].round(2)



st.title('Tabela')
st.dataframe(indices)
st.title('Indices')
opc = st.selectbox('Selecione',['MFG', 'MCR'])
st.bar_chart(df2,x='Jogador',y=opc)











  
   


    








