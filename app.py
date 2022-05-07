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
    \overrightarrow{V}* \overrightarrow{E} = \frac{\rho}{\epsilon_0}   
 ''')
st.title('Ley de Gauss para el magnetismo')

st.latex(r'''
    \overrightarrow{V}* \overrightarrow{B} = 0 
 ''')
st. write (""" Esta se fundamenta en que las fuentes y sumideros del campo magnético no existen.
No hay “cargas magnéticas”.""")


st. write (""" Eso no quiere decir que no haya objetos que puedan crear campos magnéticos; ¡eso es
lo que hacen los imanes!
La cosa es que al no haber ni fuentes ni sumideros, el campo magnético siempre debe “cerrarse”
sobre si mismo.
Por ejemplo, si intentas partir un imán en dos queriendo separarlo en dos monopolos,
el campo se cierra en la zona que has cortado, devolviendote dos imanes con dos polos cada
uno.
En resumen: En nuestro mundo los monopolos son imposibles (si existieran las ecuaciones de Maxweel podrian ser expresadas en una sola ecuación.""")
st.title('Ley de Faraday y Lenz')

st.latex(r'''
    \overrightarrow{V}* \overrightarrow{E} = -\frac{\partial B}{\partial t}   
 ''')

st. write ("""Detras de esta ley está el principio básico detrás
de casi todas las centrales eléctricas del planeta, pero me repetiré: nos dice que si
un campo magnético cambia en el tiempo esto activa el campo eléctrico de una manera precisa:
cerrándose.
Concretamente: si el campo magnético aumenta, el eléctrico se orienta en el sentido de
las agujas del reloj, si decrece se orienta al contrario.
En definitiva, nos está contado que no solo cargas e imanes pueden influir en los campos,
también pueden hacerlo entre ellos.""")

st. write ("""Eso es lo que encapsula la cuarta ecuación: *la Ley de Ampere*
:* que un campo eléctrico
cambiando en el tiempo o cargas moviéndose, es decir una corriente eléctrica, activan
el campo magnético (cerrándose, como tiene que ser).
""")
st. write ("""Basta con hacer pasar una corriente eléctrica por una bobina con la forma apropiada y tienes
un campo magnético, cuanto más intensa sea la corriente más intenso es el campo magnético.
Esto es un electroimán y la mayoría de los campos magnéticos del mundo se generan con
ellos, incluido el que nos protege del viento solar.""")






