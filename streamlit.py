import streamlit as st
import pandas as pd
import plotly.graph_objects as go

data = pd.read_excel("Cut-off Frequency.xlsx")

st.title("Karakteristik Cut-off Frequency Transistor Efek Medan Terobosan Multilayer Armchair Graphene Nanoribbon Menggunakan Pendekatan Fungsi Airy", anchor=False)
st.divider()

with st.sidebar:
    st.write("Material")
    m = st.checkbox("Monolayer")
    b = st.checkbox("Bilayer")
    t = st.checkbox("Trilayer")
    st.divider()
    st.write("Parameter")
    p = st.selectbox("", ("Tegangan Drain", "Panjang Channel", "Tebal Lapisan Oksida", "Lebar Material", "Temperatur"), label_visibility="collapsed")

if p == "Tegangan Drain":
    y = st.sidebar.selectbox("", ("0,05 V", "0,10 V", "0,15 V", "0,20 V", "0,25 V"), label_visibility="collapsed")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.write("Panjang Channel")
        st.write("20 nm")
    with c2:
        st.write("Tebal Lapisan Oksida")
        st.write("1,0 nm")
    with c3:
        st.write("Lebar Material")
        st.write("5,042 nm")
    with c4:
        st.write("Temperatur")
        st.write("300 K")
elif p == "Panjang Channel":
    y = st.sidebar.selectbox("", ("10 nm", "15 nm", "20 nm", "25 nm", "30 nm"), label_visibility="collapsed")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.write("Tegangan Drain")
        st.write("0,10 V")
    with c2:
        st.write("Tebal Lapisan Oksida")
        st.write("1,0 nm")
    with c3:
        st.write("Lebar Material")
        st.write("5,042 nm")
    with c4:
        st.write("Temperatur")
        st.write("300 K")
elif p == "Tebal Lapisan Oksida":
    y = st.sidebar.selectbox("", ("0,5 nm", "1,0 nm", "1,5 nm", "2,0 nm", "2,5 nm"), label_visibility="collapsed")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.write("Tegangan Drain")
        st.write("0,10 V")
    with c2:
        st.write("Panjang Channel")
        st.write("20 nm")
    with c3:
        st.write("Lebar Material")
        st.write("5,042 nm")
    with c4:
        st.write("Temperatur")
        st.write("300 K")
elif p == "Lebar Material":
    y = st.sidebar.selectbox("", ("1,353 nm", "3,197 nm", "5,042 nm", "7,256 nm", "9,100 nm"), label_visibility="collapsed")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.write("Tegangan Drain")
        st.write("0,10 V")
    with c2:
        st.write("Panjang Channel")
        st.write("20 nm")
    with c3:
        st.write("Tebal Lapisan Oksida")
        st.write("1,0 nm")
    with c4:
        st.write("Temperatur")
        st.write("300 K")
elif p == "Temperatur":
    y = st.sidebar.selectbox("", ("100 K", "200 K", "300 K", "400 K", "500 K"), label_visibility="collapsed")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.write("Tegangan Drain")
        st.write("0,10 V")
    with c2:
        st.write("Panjang Channel")
        st.write("20 nm")
    with c3:
        st.write("Lebar Material")
        st.write("5,042 nm")
    with c4:
        st.write("Tebal Lapisan Oksida")
        st.write("1,0 nm")

st.divider()

x = {"Tegangan Drain":"V", "Panjang Channel":"L", "Tebal Lapisan Oksida":"t", "Lebar Material":"w", "Temperatur":"T"}

fig = go.Figure()
fig.update_xaxes(title_text="Vg (V)")
fig.update_yaxes(title_text="f (Hz)")
fig.update_traces(mode='markers', marker_line_width=2, marker_size=10)

if m and b and t:
    fig.add_trace(go.Scatter(x=data["V"], y=data["M" + x[p] + y], name="MAGNR", mode="markers"))
    fig.add_trace(go.Scatter(x=data["V"], y=data["B" + x[p] + y], name="BAGNR", mode="markers"))
    fig.add_trace(go.Scatter(x=data["V"], y=data["T" + x[p] + y], name="TAGNR", mode="markers"))
    st.plotly_chart(fig, use_container_width=True)
elif m and b:
    fig.add_trace(go.Scatter(x=data["V"], y=data["M" + x[p] + y], name="MAGNR", mode="markers"))
    fig.add_trace(go.Scatter(x=data["V"], y=data["B" + x[p] + y], name="BAGNR", mode="markers"))
    st.plotly_chart(fig, use_container_width=True)
elif m and t:
    fig.add_trace(go.Scatter(x=data["V"], y=data["M" + x[p] + y], name="MAGNR", mode="markers"))
    fig.add_trace(go.Scatter(x=data["V"], y=data["T" + x[p] + y], name="TAGNR", mode="markers"))
    st.plotly_chart(fig, use_container_width=True)
elif b and t:
    fig.add_trace(go.Scatter(x=data["V"], y=data["B" + x[p] + y], name="BAGNR", mode="markers"))
    fig.add_trace(go.Scatter(x=data["V"], y=data["T" + x[p] + y], name="TAGNR", mode="markers"))
    st.plotly_chart(fig, use_container_width=True)
elif m:
    fig.add_trace(go.Scatter(x=data["V"], y=data["M" + x[p] + y], name="MAGNR", mode="markers"))
    st.plotly_chart(fig, use_container_width=True)
elif b:
    fig.add_trace(go.Scatter(x=data["V"], y=data["B" + x[p] + y], name="BAGNR", mode="markers"))
    st.plotly_chart(fig, use_container_width=True)
elif t:
    fig.add_trace(go.Scatter(x=data["V"], y=data["T" + x[p] + y], name="TAGNR", mode="markers"))
    st.plotly_chart(fig, use_container_width=True)
else:
    st.plotly_chart(fig, use_container_width=True)