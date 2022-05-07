import streamlit as st
st.markdown("<h1 style='text-align: center; color:lightblue;'>Ecuaciones de Maxwell</h1>", unsafe_allow_html=True)
st.button('click aqui')
st.balloons()
import pandas as pd
st.title('Ley de Gauss')
st.latex(r'''
    \overrightarrow{\nabla}* \overrightarrow{E} = \frac{\rho}{\epsilon_0}   
 ''')
st. write (""" Esta describe como las cargas afectan al campo eléctrico. En concreto te dice que las cargas eléctricas son fuentes de campo eléctrico, si son positivas
o sumideros de campo eléctrico si son negativas, no es otra cosa que decir en términos
que cargas del mismo signo repelen y de distinto atraen.
Captura que el campo eléctrico decae con la distancia y lo hace
de una manera muy precisa: con el cuadrado de la distancia.""")

st.title('¿Para que sirve?')
st. write ("""La ley de gauss tiene su máxima utilidad para calcular el campo eléctrico en situaciones donde
la distribución de carga tiene simetría esférica, cilíndrica o está distribuida uniformemente en un plano o en una placa infinita.""")
st.image(["images.png",      "SUPERFICIE CILIDRICA.png"]) 

st. write ("""Se determina la dirección del campo eléctrico a partir de la
simetría de la distribución de carga (de la forma de la superfie) uniforme en estos cuerpos
simétricos y también su magnitud.

De manera alternativa conociendo el campo eléctrico los alrededores de estas distribuciones simétricas se pudiera
calcular la carga.
 .""")

st. write ("""Para calcular el campo eléctrico y su magnitud se utiliza la ley de Gauss:""") 
st.latex(r'''\oint_s\overrightarrow{E} * d\overrightarrow{s} = \frac{Q_{neta}}{\epsilon_0} ''')

st. write ("""Va de la mano a este tema para comprender qué es el flujo eléctrico;""") 

col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
         st.markdown("![Alt Text](http://3.bp.blogspot.com/-5ryI19Mmm78/USH2VKEzgLI/AAAAAAAACrQ/9OnqCH85ZNE/s400/gauss1.gif)")

    with col3:
        st.write("")

st. write ("""
Imaginemos una superficie plana como la de la imagen, esta
superficie tiene un área superficial S imaginemos que esta superficie es
atravesada por líneas de campo eléctrico en este ejemplo en particular imaginemos que ese campo eléctrico es uniforme, para lo cual el flujo eléctrico sería el producto de la magnitud de ese campo eléctrico
que está atravesando esta superficie por el área superficial por el coseno del ángulo que formaría ese vector campo eléctrico y
el vector normal n 
(vector n es un vector que es normal a la
superficie y forma un ángulo de 90
grados con la superficie). Esto cuando 
es uniforme y la superficie es plana.""") 




st.title('Ley de Gauss para el magnetismo')

st.latex(r'''
    \overrightarrow{\nabla}* \overrightarrow{B} = 0 
 ''')
st. write (""" Esta se fundamenta en que las fuentes y sumideros del campo magnético no existen.
No hay “cargas magnéticas”.""")


st. write (""" Eso no quiere decir que no haya objetos que puedan crear campos magnéticos (eso
lo hacen los imanes).
La cosa es que al no haber ni fuentes ni sumideros, el campo magnético siempre debe “cerrarse”
sobre si mismo.
Por ejemplo, si intentas partir un imán en dos queriendo separarlo en dos monopolos,
el campo se cierra en la zona que has cortado, devolviendote dos imanes con dos polos cada
uno. 
En nuestro mundo los monopolos son imposibles (si existieran las ecuaciones de Maxwell podrian ser expresadas en una sola ecuación.""")
st.title('Ley de Faraday y Lenz')

st.latex(r'''
    \overrightarrow{\nabla}* \overrightarrow{E} = -\frac{\partial \overrightarrow{B}}{\partial t}   
 ''')

st. write ("""De esta ley está el principio básico detrás
de casi todas las centrales eléctricas del planeta, nos dice que si
un campo magnético cambia en el tiempo esto activa el campo eléctrico de una manera precisa:
cerrándose.
Concretamente si el campo magnético aumenta, el eléctrico se orienta en el sentido de
las agujas del reloj, si decrece se orienta al contrario.
En definitiva, no solo cargas e imanes pueden influir en los campos,
también pueden hacerlo entre ellos.""")



st. write ("""Eso es lo que encapsula la cuarta ecuación:
La ley de Ampere""")
st. write ("""
Un campo eléctrico
cambiando en el tiempo o cargas moviéndose, es decir una corriente eléctrica, activan
el campo magnético (cerrándose, como tiene que ser).
""")

st.latex(r'''
    \overrightarrow{\nabla}* \overrightarrow{E} = \mu_0 \overrightarrow{J} +\mu_0 \epsilon_0 \frac{\partial \overrightarrow{E}}{\partial t}   
 ''')

st. write ("""Basta con hacer pasar una corriente eléctrica por una bobina con la forma apropiada para
 tener un campo magnético, cuanto más intensa sea la corriente más intenso es el campo magnético.
Esto es un electroimán y la mayoría de los campos magnéticos del mundo se generan con
ellos, incluido el que nos protege del viento solar.""")






