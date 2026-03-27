import streamlit as st
import pandas as pd
from kpi_functions import *
st.set_page_config(page_title='Stellantis KPI Advanced', layout='wide')
st.title('🚗 Stellantis – KPI Dashboard (Advanced Cloud Edition)')
uploaded = st.file_uploader('Carica file KPI (.xlsx)', type=['xlsx'])
if uploaded:
    df = pd.read_excel(uploaded, engine='openpyxl')
    st.success('File caricato correttamente!')
    st.dataframe(df, use_container_width=True)
    st.header('📊 KPI Global Overview')
    total_projects = len(df)
    pv_matches = sum(df.apply(lambda r: pv_matches_x2(r['PV_CLOSURE'], r['X2_DATE']), axis=1))
    ppap_matches = sum(df.apply(lambda r: ppap_matches_x3(r['PPAP_DATE'], r['X3_DATE']), axis=1))
    col1, col2, col3 = st.columns(3)
    col1.metric('Progetti Totali', total_projects)
    col2.metric('PV = X2', pv_matches)
    col3.metric('PPAP = X3', ppap_matches)
    st.header('🔎 Dettaglio Progetto')
    for _, row in df.iterrows():
        st.subheader(f"🔧 {row['PDEF']} – {row['VEHICLE_PROGRAM']}")
        c1, c2, c3 = st.columns(3)
        c1.write(f"**PV matches X2:** {'🟢' if pv_matches_x2(row['PV_CLOSURE'], row['X2_DATE']) else '🔴'}")
        c2.write(f"**PPAP matches X3:** {'🟢' if ppap_matches_x3(row['PPAP_DATE'], row['X3_DATE']) else '🔴'}")
        c3.write(f"**X2 readiness:** {readiness_indicator(row['X2_PART_READINESS'])}")
        st.markdown('---')