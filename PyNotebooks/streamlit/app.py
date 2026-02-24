import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

st.title("Statistical Analysis using Streamlit: Python")

# st.markdown("$x^2 alpha$")
# st.header("Header: M.Sc. (Statistics) Batch 2025-27")
# st.subheader("Subheader: M.Sc. (Statistics) Batch 2025-27")
# st.text("Text: M.Sc. (Statistics) Batch 2025-27")
# st.markdown("# Markdown: M.Sc. (Statistics) Batch 2025-27")
# st.markdown("## Markdown: M.Sc. (Statistics) Batch 2025-27")
# st.success("Success")
# st.error("Error")
# st.warning("Warning")

st.sidebar.title("Distribution:")
dist=st.sidebar.selectbox("Select Distribution",
                          ["Normal","Exponential","Binomial","Poisson"])
n=st.sidebar.slider("Sample Size",10,1000,10)
if dist=="Normal":
    mu=st.sidebar.number_input("Mu",0)
    sigma=st.sidebar.number_input("Sigma",1)
    data=np.random.normal(mu,sigma,n)
elif dist=="Exponential":
    theta=st.sidebar.number_input("Theta",1)
    data=np.random.exponential(theta,n)
elif dist=="Binomial":
    trials=st.sidebar.number_input("Number of trials",100)
    prob=st.sidebar.number_input("Probability of Success",0.5)
    data=np.random.binomial(trials,prob,n)
else:
    lamb=st.sidebar.number_input("Lambda",1)
    data=np.random.poisson(lamb,n)

h=st.sidebar.checkbox("Histogram")
b=st.sidebar.checkbox("Boxplot")

if h==True:
    fig, ax = plt.subplots()
    ax.hist(data,bins=30)

    st.pyplot(fig)

if b==True:
    fig, ax = plt.subplots()
    ax.boxplot(data)

    st.pyplot(fig)

df=pd.DataFrame(data,columns=["X"])
st.table(df.describe())

file=st.sidebar.file_uploader("Upload Dataset in CSV",type=["csv"])
df=pd.read_csv(file)

# st.table(df.head(6))
st.table(pd.pivot_table(df,values="population",index="country",columns="year",aggfunc="mean"))
