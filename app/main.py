import streamlit as st
import pandas as pd
import plotly.express as px 

st.set_page_config(page_title="Kifiya AI Mastery",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )

st.title("MoonLight Energy Solutions")
val = st.slider("Select a value", 0, 100, 0, step=1)
st.write(val)
btn1 = st.button("Click Me")
if btn1:
    st.write("I am clicked")
@st.cache_data
def load_data(path:str):
    data = pd.read_csv(path)
    return data

with st.sidebar:
    upload_file = st.file_uploader("Choose a file", type=["csv", "xlsx","pdf"])

    if upload_file is None:
        st.info("upload file through config",icon="ℹ️")
        st.stop()
  
upload_data = load_data(upload_file)
col1, col2, col3 = st.columns([1,1,1])

solar_data = upload_data.loc[(upload_data["Tamb"] == 26.2) & 
            (upload_data["RH"]== 93.8)&
            (upload_data["WSgust"] == 1.3),
        
            ]

with col1.expander("Solar Data"):
    st.dataframe(
        upload_data,
        column_config={
            "WD": st.column_config.NumberColumn(format="%d")
        }
        )

info = solar_data.describe()

with col2.expander("Description"):
    st.write(info)
col3.metric(label="Temprature", value= '${:,.2}'.format(solar_data["TModA"].sum()/1000000000)+"B", delta="-3" )
#scatter plot
@st.cache_data
def scatter_plot():
    fig = px.scatter(solar_data, x="RH", y="WS", color="WD", title="Humidity vs Wind Speed")
    st.plotly_chart(fig, use_container_width=True)

with col1:
    scatter_plot()

@st.cache_data
def line_plot():
    fig = px.line(solar_data, x="RH", y="WS", color="WD",text= "WDstdev", markers=True,
                  title="Humidity vs Wind Speed")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    line_plot()

# Bar chart
@st.cache_data
def bar_plot():
    fig = px.bar(solar_data, x="RH", y="WS", color="WD", title="Humidity vs Wind Speed")
    st.plotly_chart(fig, use_container_width=True)  


with col1:
    bar_plot()


