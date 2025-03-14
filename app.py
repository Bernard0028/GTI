import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image
import base64
import streamlit as st
from statsmodels.tsa.holtwinters import Holt
import numpy as np
    






# Encode the image as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Replace 'your_image.png' with the actual image filename
image_base64 = get_base64_image("istockphoto-106492379-612x612.jpg")


# Load Data
data = pd.read_csv("Global Terrorism Index 2023.csv")

# Load Image for Introduction Page
image = Image.open("istockphoto-106492379-612x612.jpg")

# Set Page Title and Layout
st.set_page_config(page_title="Global Terrorism Dashboard", layout="wide")

#Custom CSS for Styled Title and Sidebar
st.markdown("""
    <style>
        .title { text-align: center; font-size: 36px !important; font-weight: bold; color: white; }
        .sidebar .sidebar-content { background-color: #f7f7f7; }
        .question-box { font-size: 20px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📍 Navigation")
page = st.sidebar.radio("Go to", ["About Us", "Introduction", "Overview", "EDA", "Prediction"])


if page == "About Us":
    st.markdown("<p class='title'>👥 About Us</p>", unsafe_allow_html=True)

    # Welcome Message
    st.write("""
    ## 🌟 Welcome to Our Interactive Global Terrorism Index 2023 Dashboard!
    
    This dashboard is designed to provide a *comprehensive analysis* of global terrorism trends. By leveraging the dataset below, we deliver valuable insights into how various factors such as *country, **year, **number of incidents, **fatalities, and **injuries* impact the global terrorism landscape.
    """)

    # Dataset Information
    st.subheader("📊 Preprocessed Global Terrorism Index Dataset")
    st.write(f"""
    - *Number of Rows*: {len(data):,}  
    - *Key Features*: Country, Year, Incidents, Fatalities, Injuries, Hostages  
    - *Purpose*: To analyze and visualize terrorism trends across different dimensions.
    """)

    # Display Full Dataset (Optional)
    if st.checkbox("Show Full Dataset"):
        st.dataframe(data)  # Show the entire dataset

    # Download Option for Full Dataset
    st.subheader("📥 Download Full Dataset")
    st.markdown("""
    If you'd like to explore the dataset further, you can download it as a CSV file:
    """)
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Dataset as CSV",
        data=csv,
        file_name="Global_Terrorism_Index_2023.csv",
        mime="text/csv"
    )


    # Additional Metrics
    total_incidents = data["Incidents"].sum()
    total_fatalities = data["Fatalities"].sum()
    total_injuries = data["Injuries"].sum()
    years_covered = data["Year"].nunique()

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="📌 Total Incidents Recorded", value=f"{total_incidents:,}")
    
    with col2:
        st.metric(label="💀 Total Fatalities", value=f"{total_fatalities:,}")
    
    with col3:
        st.metric(label="🚑 Total Injuries", value=f"{total_injuries:,}")

    st.write(f"🔹 *Years Covered*: {years_covered}")

    st.write("🔹 Our goal is to provide valuable insights to enhance awareness and support data-driven decision-making. Thank you for using our dashboard!")


# Submitted By Section
    st.subheader("📝 Submitted By:")
    st.markdown("""
    - *Bernard*  
    - *Barry*   
    - *Travis*  
    """)


# 🎯 Introduction Page
if page == "Introduction":
    st.markdown("<p class='title'>🌍 Global Terrorism Index 2023 Dashboard</p>", unsafe_allow_html=True)
    
    
   
    
    # Center Image 
    st.markdown(
    """
    <div style="text-align: center;">
        <img src="data:image/png;base64,{}" width="500">
    </div>
    """.format(base64.b64encode(open("istockphoto-106492379-612x612.jpg", "rb").read()).decode()),
    unsafe_allow_html=True
)








    # Introduction Text
    st.write("""
    ## 📊 Understanding Global Terrorism Trends
    Terrorism remains one of the most critical global security challenges, affecting *millions of lives* and disrupting societies. 
    The *Global Terrorism Index Dashboard* provides insights into terrorism incidents worldwide using *2023* data.

    ### 🛡 *What is Terrorism?*
    Terrorism refers to *the unlawful use of violence and intimidation*, especially against civilians, to achieve political, 
    religious, or ideological goals. It often targets governments, infrastructure, and innocent populations to spread fear 
    and influence decision-making.

    ### 🌎 *Global Trends in Terrorism*
    Over the years, terrorism has evolved in scale, tactics, and geographical distribution. Some key trends include:

    - 📈 *Rise and fall of terrorist organizations*: Groups like ISIS, Al-Qaeda, and Boko Haram have shaped global security, while some have weakened due to counterterrorism efforts.
    - 🌍 *Regional Hotspots: The highest number of terrorist attacks occur in regions like the **Middle East, South Asia, and Africa*.
    - 🔥 *Shifting Strategies*: Terrorist groups have adapted to technology, using social media for propaganda, recruitment, and financing.
    - 📉 *Declining Trends: Some regions have seen a decrease in attacks due to **strong counterterrorism policies* and *intelligence cooperation*.

    ### 🔹 *Key Features of This Dashboard*
    This dashboard allows users to explore global terrorism trends using real-time data and visualization tools.

    - 📌 *Overview of terrorism incidents* by *country* and *year*.
    - 🔍 *Interactive tools* for analyzing trends and patterns.
    - 📊 *Heatmaps & time-series charts* to understand attack frequency.
    - 🌎 *Insights on the top 10 most affected countries*.

    By studying these trends, policymakers, researchers, and the public can **better understand terrorism and develop 
    strategies to prevent future threats**.

    ---
    """)

    # 🔥 Poll Question
    st.subheader("📊 Quick Question")
    st.markdown("<p class='question-box'>Which country had the highest number of terrorism incidents in 2023?</p>", unsafe_allow_html=True)

    options = [
        "Afghanistan", 
        "Iraq", 
        "Nigeria", 
        "Pakistan", 
        "Syria", 
        "India", 
        "Somalia", 
        "Philippines"
    ]

    answer = st.radio("Select an answer:", options)
    
    if st.button("Submit Answer"):
        if answer == "Afghanistan":
            st.success("✅ Correct! Afghanistan had the highest number of terrorism incidents in 2023.")
        else:
            st.error("❌ Incorrect. The correct answer is Afghanistan.")

    # Moved navigation instructions below the poll
    st.markdown("📂 *For more infomation, navigate through the sections using the sidebar.*")








# 📊 Overview Page
if 'page' in locals() and page == "Overview":
    # Centered Title
    st.markdown("""
    <h1 style='text-align: center; font-size: 45px;'>🌍 Global Terrorism Overview</h1>
    <h3 style='text-align: center; font-size: 20px; color: gray;'>Analyzing global terrorism trends, hotspots, and impacts.</h3>
""", unsafe_allow_html=True)

    # Create a two-column layout (adjust column widths as needed)
    col1, col2 = st.columns([1.2, 2])  # 1: GIF, 2: Text

    with col1:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGxsZmw3bTJnNmIyb3V1OXllZHNtaWFwbHNjbHF5ZzVlN3k2b2xveSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cb89q6BvqAHfwH6AEU/giphy.gif", width=400)

    with col2:
        st.markdown("""
        <p style='font-size: 20px; font-weight: bold; text-align: justify; line-height: 1.6;'>
        Terrorism is a global threat that evolves with political conflicts, economic disparities, and technological advancements. 
        Regions like the Middle East, Africa, and South Asia remain major hotspots, while cyber and lone-wolf attacks are on the rise. 
        Terrorist groups leverage social media, encrypted communication, and drones, increasing their reach and impact.
        </p>

        <p style='font-size: 20px; font-weight: bold; text-align: justify; line-height: 1.6;'>
        The consequences of terrorism include humanitarian crises, economic disruptions, and political instability. Governments and 
        international bodies like the UN and NATO work to counteract threats through intelligence sharing, financial sanctions, 
        and counter-radicalization programs. Addressing the root causes remains key to long-term solutions.
        </p>
        """, unsafe_allow_html=True)


    # 📍 Region Selection (Now above the map)
    st.subheader("Select a Region")
    regions = {
    "NA": "North America",
    "EU": "Europe",
    "SA": "South America",
    "AF": "Africa",
    "AS": "Asia",
    "ME": "Middle East",
    "OC": "Oceania"
    }

    selected_region = st.radio("📍 Select a Region:", list(regions.keys()), horizontal=True, format_func=lambda x: regions[x])

    # 🌍 Define countries per region
    region_countries = {
        "NA": ["United States", "Canada", "Mexico"],
        "EU": ["United Kingdom", "Germany", "France", "Italy", "Spain", "Netherlands", "Sweden"],
        "SA": ["Brazil", "Argentina", "Colombia", "Chile", "Peru"],
        "AF": ["South Africa", "Nigeria", "Egypt", "Kenya", "Ethiopia"],
        "AS": ["China", "India", "Japan", "Indonesia", "Malaysia", "Pakistan"],
        "ME": ["Iran", "Iraq", "Syria", "Saudi Arabia", "Yemen"],
        "OC": ["Australia", "New Zealand", "Fiji", "Papua New Guinea"]
    }
    
    # 🌍 Filter data based on selected region
    filtered_data = data[data["Country"].isin(region_countries[selected_region])]

    # 🌍 Display Region-Specific Map
    st.subheader(f"Terrorism Incidents in {regions[selected_region]}")
    
    if not filtered_data.empty:
        fig = px.choropleth(
    data_frame=filtered_data,
    locations="Country",
    locationmode="country names",
    color="Incidents",
    hover_name="Country",  # Show country name on hover
    hover_data={"Incidents": True},  # Show incident numbers
    title=f"Terrorism Incidents in {regions[selected_region]}",
    color_continuous_scale="reds",
    template="plotly_dark",
    projection="natural earth"
)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(f"No data available for {regions[selected_region]}.")

    # 📌 Country Selection (Now based on selected region)
    selected_country = st.selectbox("Select a Country:", region_countries[selected_region])

    # 📊 Insights from dataset
    st.subheader(f"Insights for {selected_country}:")
    country_data = data[data["Country"] == selected_country]

    if not country_data.empty:
        incidents = country_data["Incidents"].sum()
        most_common_attack = country_data["Attack Type"].mode()[0] if "Attack Type" in country_data else "N/A"

        st.markdown(f"🛑 *Total Incidents*: {incidents:,}")
        st.markdown(f"🔥 *Most Common Attack Type*: {most_common_attack}")
    else:
        st.warning("No data available for the selected country.")

    st.markdown("---")  # Divider
    

elif page == "EDA":
    # Apply Seaborn theme for better aesthetics
    sns.set_style("whitegrid")
    sns.set_palette("Set2")

    st.markdown("<p class='title'>🔍 Exploratory Data Analysis (EDA)</p>", unsafe_allow_html=True)
    
    # Create tabs for different EDA sections
    tab1, tab2, tab3 = st.tabs(["📌 Top 10 Countries", "📊 Data Exploration", "📈 Visualization"])

    # 📌 Top 10 Most Affected Countries
    with tab1:
        st.markdown("## 📌 Top 10 Most Affected Countries")
        
        # Aggregating data to find top affected countries
        country_counts = data.groupby("Country")["Incidents"].sum().reset_index()
        top_countries = country_counts.sort_values(by="Incidents", ascending=False).head(10)

        # Display bar chart
        st.bar_chart(top_countries.set_index("Country"))

        # Data Table
        st.subheader("Top 10 Countries Data")
        st.write(top_countries)

        # Alternative visualization with Seaborn
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x="Incidents", y="Country", data=top_countries, palette="Reds_r", ax=ax)
        ax.set_xlabel("Number of Incidents")
        ax.set_ylabel("Country")
        ax.set_title("Top 10 Countries with Highest Terrorism Incidents")
        st.pyplot(fig)

    # 📊 General Data Exploration
    with tab2:
        st.markdown("## 🔍 Explore the Data")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📍 Incidents by Country")
            st.write(data["Country"].value_counts())

        with col2:
            st.subheader("📆 Incidents by Year")
            st.write(data["Year"].value_counts())

    # 📈 Visualization of Terrorism Trends
    with tab3:
        st.markdown("## 📈 Visualizing Terrorism Trends")

        # Group by Year and Sum Incidents
        incidents_by_year = data.groupby("Year")["Incidents"].sum().reset_index()

        # Line Chart
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.lineplot(x="Year", y="Incidents", data=incidents_by_year, marker="o", color="red", ax=ax)
        ax.set_xlabel("Year")
        ax.set_ylabel("Total Incidents")
        ax.set_title("Trend of Terrorism Incidents Over Time")
        ax.grid(True)
        st.pyplot(fig)

        # 🌍 World Heatmap (Choropleth)
        fig = px.choropleth(
            data, 
            locations="iso3c", 
            color="Incidents",
            hover_name="Country",
            title="Global Terrorism Intensity",
            color_continuous_scale="Reds",
            projection="natural earth"
        )
        st.plotly_chart(fig)






  




elif page == "Prediction":
    # Apply Seaborn theme for better aesthetics
    sns.set_style("whitegrid")
    sns.set_palette("Set2")

    st.markdown("<p class='title'>📈 Terrorism Incident Prediction</p>", unsafe_allow_html=True)
    st.write("This application predicts future terrorism incidents based on historical data using Holt's Exponential Smoothing.")

    # Country selection
    selected_country = st.selectbox("Select a country:", sorted(data["Country"].unique()))

    # Filter data by the selected country
    country_data = data[data["Country"] == selected_country]

    if country_data.empty:
        st.warning("No data available for the selected country.")
    else:
        # Group by Year and sum incidents
        incidents_by_year = country_data.groupby("Year")["Incidents"].sum().reset_index()

        if incidents_by_year.empty:
            st.warning("No incident data available for the selected country.")
        else:
            # Fit the Holt model
            model = Holt(incidents_by_year["Incidents"])
            fit = model.fit(smoothing_level=0.2, smoothing_trend=0.1, optimized=True)

            # Ensure non-negative fitted values
            fitted_values = np.maximum(fit.fittedvalues, 0)

            # User input for number of years to predict
            num_years_to_predict = st.slider("Select number of years to predict:", 1, 10, 5)
            last_year = incidents_by_year["Year"].max()
            forecast_years = list(range(last_year + 1, last_year + num_years_to_predict + 1))

            # Ensure non-negative forecast values
            forecast_values = np.maximum(fit.forecast(len(forecast_years)), 0)

            # Plot results
            fig, ax = plt.subplots(figsize=(12, 6))

            # Actual Data
            ax.plot(incidents_by_year["Year"], incidents_by_year["Incidents"], 
                    marker="o", markersize=7, linewidth=2, label="Actual Data", color="#4C72B0")

            # Fitted Trend
            ax.plot(incidents_by_year["Year"], fitted_values, linestyle="dashed", linewidth=2, 
                    color="red", label="Fitted Trend")

            # Forecast
            ax.plot(forecast_years, forecast_values, linestyle="dashed", marker="o", markersize=7, 
                    linewidth=2, color="green", label="Forecast")

            # Labels and Styling
            ax.set_xlabel("Year", fontsize=14, fontweight="bold")
            ax.set_ylabel("Total Incidents", fontsize=14, fontweight="bold")
            ax.set_title(f"Incident Prediction for {selected_country}", fontsize=16, fontweight="bold")
            ax.legend(fontsize=12)
            ax.grid(alpha=0.3)

            # Show plot in Streamlit
            st.pyplot(fig)

            # Display forecast values
            st.subheader(f"Predicted Incidents for {selected_country}:")
            predictions = pd.DataFrame({"Year": forecast_years, "Predicted Incidents": forecast_values})
            st.dataframe(predictions)
