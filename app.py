import streamlit as st
import numpy as np
import plotly.express as px
import bitstring

st.title("Numerical Hygine")

# markdown - a.md
with open("a.md") as f:
    st.markdown(f.read())

p = st.slider("p", -36, 36, 0, 1)
e = np.exp(-p)
y1 = np.log(1+e)
y2 = np.log1p(e)

st.write("p =", p)
st.write("exp(-p) =", e)
st.write("log(1+exp(-p)) =", y1)
st.write("log1p(exp(-p)) =", y2)

fig = px.bar(title="log(1+10^(-p))")
fig.add_bar(x=[0], y=[y1], name="log(1+10^(-p))", text=[y1], textposition="outside", textfont=dict(color="yellow", size=11))
# fig.add_bar(x=[1], y=[y2], name="log1p(10^(-p))", text=[y2], textposition="outside", textfont=dict(color="yellow", size=11))

st.plotly_chart(fig)

# markdown - b.md
with open("b.md") as f:
    st.markdown(f.read())

# markdown - c.md
with open("c.md") as f:
    st.markdown(f.read())

a = 1e-16

n = st.number_input("Decimal Value", value=0.5, step=a, format="%.16f")
l = st.selectbox("bit length", options=[16, 32, 64], index=0)

nb = bitstring.BitArray(float=n, length=l)
st.write("Selected Decimal Value:", n)
st.write("Floating Point Representation:", nb.bin)
st.write("Stored Floating Point Value:", nb.float)

st.markdown("The stored value is often different/inaccurate. This means that the computer can store only a limited number of digits after the decimal point. This is called the precision of the number. The precision of the number is determined by the number of bits used to store the number. The more bits used to store the number, the higher the precision of the number. The default bits used to store a number in Python is 64 bits.")

# markdown - d.md
with open("d.md") as f:
    st.markdown(f.read())

# markdown - e.md
with open("e.md") as f:
    st.markdown(f.read())

def basic_softplus(x):
    y = np.log(1 + np.exp(x))
    # if y = 0, then y = exp(-50)
    y = np.where(y > 0, y, np.exp(-50))
    return y

def relu(x):
    return np.maximum(x, 0)

x = np.linspace(-5, 5, 1000)
y1 = (basic_softplus(x))
y2 = (relu(x))

fig = px.line(title="Softplus function")
fig.add_scatter(x=x, y=y1, name="Softplus")
fig.add_scatter(x=x, y=y2, name="ReLU")

st.plotly_chart(fig)

st.markdown("For large negative values of $x$, the softplus function reaches almost $0$.")

st.markdown("For small positive values of $x$, the softminus function reaches almost $-\infty$.")

