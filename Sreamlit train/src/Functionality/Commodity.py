

        # Load data
        # copra_india_data = pd.read_excel("C:/Users/sahil.shrivastava/OneDrive - Marico Ltd/Desktop/Commodity Market/coconut-oil-IN.xlsx")
        # copra_usa_data = pd.read_excel("C:/Users/sahil.shrivastava/OneDrive - Marico Ltd/Desktop/Commodity Market/coconut-oil-USA.xlsx")
        # crude_oil_data = pd.read_excel("C:/Users/sahil.shrivastava/OneDrive - Marico Ltd/Desktop/Commodity Market/Crude oil.xlsx")

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def main():
    st.title("Commodity Market Trends")

    # Sidebar menu for navigation
    page = st.sidebar.selectbox("Select a page", ["Home", "Commodity Trends"])

    if page == "Home":
        st.write("Welcome to the Commodity Market Trends app!")
    elif page == "Commodity Trends":
        st.header("Commodity Trends")

        st.subheader("Indian Copra Price Trends")
        copra_india_data = pd.read_excel("C:/Users/sahil.shrivastava/OneDrive - Marico Ltd/Desktop/Commodity Market/coconut-oil-IN.xlsx")
        st.write(copra_india_data.head())

        st.subheader("USA Copra Price Trends")
        copra_usa_data = pd.read_excel("C:/Users/sahil.shrivastava/OneDrive - Marico Ltd/Desktop/Commodity Market/coconut-oil-USA.xlsx")
        st.write(copra_usa_data.head())

        st.subheader("Crude Oil Price Trends")
        crude_oil_data = pd.read_csv("C:/Users/sahil.shrivastava/OneDrive - Marico Ltd/Desktop/Commodity Market/Crude oil.xlsx")
        st.write(crude_oil_data.head())

        # Plotting Indian Copra Price Trend
        st.subheader("Indian Copra Price Trend")
        fig_copra_india = go.Figure()
        fig_copra_india.add_trace(go.Scatter(x=copra_india_data['Month'], y=copra_india_data['Price'], mode='lines', name='Price'))
        fig_copra_india.update_layout(title='Indian Copra Price Trend',
                                    xaxis_title='Month',
                                    yaxis_title='Price (Indian Rupee per Metric Ton)')
        st.plotly_chart(fig_copra_india)

        # Plotting USA Copra Price Trend
        st.subheader("USA Copra Price Trend")
        fig_copra_usa = go.Figure()
        fig_copra_usa.add_trace(go.Scatter(x=copra_usa_data['Month'], y=copra_usa_data['Price'], mode='lines', name='Price'))
        fig_copra_usa.update_layout(title='USA Copra Price Trend',
                                    xaxis_title='Month',
                                    yaxis_title='Price (USD)')
        st.plotly_chart(fig_copra_usa)

        # Plotting Crude Oil Price Trend
        st.subheader("Crude Oil Price Trend")
        fig_crude_oil = go.Figure()
        fig_crude_oil.add_trace(go.Scatter(x=crude_oil_data['Month'], y=crude_oil_data['CRUDE_PETRO'], mode='lines', name='Price'))
        fig_crude_oil.update_layout(title='Crude Oil Price Trend',
                                    xaxis_title='Month',
                                    yaxis_title='Price (USD/bbl)')
        st.plotly_chart(fig_crude_oil)

if __name__ == "__main__":
    main()
