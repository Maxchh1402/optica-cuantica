import streamlit as st
st.markdown("<h1 style='text-align: center; color:lightblue;'>Ecuaciones de Maxwell</h1>", unsafe_allow_html=True)
st.button('click aqui')
st.balloons()
st.title('Ley de Gauss')
st. write (""" Esta describe como las cargas afectan al campo eléctrico En concreto te dice que las cargas eléctricas son fuentes de campo eléctrico si son positivas
o sumideros de campo eléctrico si son negativas, que no es otra cosa que decir en términos
“fancy” de campo que cargas del mismo signo repelen y de distinto atraen.
captura que el campo eléctrico decae con la distancia y lo hace
de una manera muy precisa: con el cuadrado de la distancia.""")


st.latex(r'''
    \overrightarrow{V}* \overrightarrow{E} \epsilon + \rho + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
st.title('Ley de Gauss para el magnetismo')
st.title('Ley de Faraday y Lenz')

