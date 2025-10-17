import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page configuration to a wide layout for a better dashboard experience
st.set_page_config(layout="wide")

# --- Data Preparation ---
# This data has been meticulously corrected to fix all previous typos.
data = [
    # Liquidity Ratios
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '21", 'Value': 0.612540614},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '22", 'Value': 0.130306},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '23", 'Value': 0.6136503},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '24", 'Value': 0.1821464},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '25", 'Value': 0.69466103},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '21", 'Value': 0.153686231},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '22", 'Value': 0.1553135},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '23", 'Value': 0.1436805},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '24", 'Value': 0.2858328},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '25", 'Value': 0.20663665},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '21", 'Value': 0.039454303},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '22", 'Value': 0.0006535},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '23", 'Value': 0.0039752},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '24", 'Value': 0.1068076},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '25", 'Value': 0.01643514},

    # Solvency Ratios
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '21", 'Value': 0.541417008},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '22", 'Value': 0.9065988},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '23", 'Value': 0.8367351},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '24", 'Value': 0.5774392},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '25", 'Value': 0.3130154},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '21", 'Value': 0.351245232},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '22", 'Value': 0.4755058},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '23", 'Value': 0.4555557},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '24", 'Value': 0.3660853},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '25", 'Value': 0.23839431},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '21", 'Value': 23.65825068},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '22", 'Value': 15.405226},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '23", 'Value': 18.864577},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '24", 'Value': 18.773841},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '25", 'Value': 22.1519452},

    # Profitability Ratios
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '21", 'Value': 6710.02},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '22", 'Value': 8575.20},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '23", 'Value': 9891.18},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '24", 'Value': 9543.64},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '25", 'Value': 10684.94},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '21", 'Value': 0.49},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '22", 'Value': 0.39},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '23", 'Value': 0.33},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '24", 'Value': 0.43},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '25", 'Value': 0.4},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '21", 'Value': 0.191021868},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '22", 'Value': 0.155735},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '23", 'Value': 0.1736696},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '24", 'Value': 0.1890267},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '25", 'Value': 0.17762964},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '21", 'Value': 0.141823335},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '22", 'Value': 0.1072547},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '23", 'Value': 0.1421032},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '24", 'Value': 0.1277933},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '25", 'Value': 0.12202587},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '21", 'Value': 0.364113753},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '22", 'Value': 0.3309945},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '23", 'Value': 0.3964381},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '24", 'Value': 0.3851089},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '25", 'Value': 0.42904705},

    # Efficiency Ratios
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '21", 'Value': 13.53809216},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '22", 'Value': 7.6464609},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '23", 'Value': 8.5033334},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '24", 'Value': 8.8775569},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '25", 'Value': 9.6944573},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable', 'Year': "Mar '21", 'Value': 132.4474652},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable', 'Year': "Mar '22", 'Value': 62.520776},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable', 'Year': "Mar '23", 'Value': 61.249178},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable', 'Year': "Mar '24", 'Value': 53.621341},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable', 'Year': "Mar '25", 'Value': 49.3825893},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '21", 'Value': 22.05734243},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '22", 'Value': 12.042535},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '23", 'Value': 13.22356},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '24", 'Value': 11.885032},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '25", 'Value': 11.5552658},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '21", 'Value': 5.134533828},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '22", 'Value': 2.9154562},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '23", 'Value': 3.1276209},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '24", 'Value': 2.9400198},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '25", 'Value': 3.36390582},
]

# Convert the list into a pandas DataFrame
df = pd.DataFrame(data)

# --- Function to Generate Insights ---
def get_category_insights(category_name, data_df):
    """Generates an explanation and a simple trend insight for a given ratio category."""
    insights = "No description available."
    trend_insight = "Could not generate a trend insight due to missing data."
    
    key_ratios = {
        'Liquidity Ratios': 'Current Ratio',
        'Solvency Ratios': 'Debt-to-Equity Ratio',
        'Profitability Ratios': 'Net Profit Margin',
        'Efficiency Ratios': 'Asset Turnover'
    }
    
    descriptions = {
        'Liquidity Ratios': "💧 **Liquidity Ratios** measure a company's ability to pay its short-term debts. Higher values are generally better.",
        'Solvency Ratios': "🏦 **Solvency Ratios** assess long-term financial health. A lower Debt-to-Equity ratio is often preferred.",
        'Profitability Ratios': "💰 **Profitability Ratios** show how well a company generates profit. Higher margins and returns are signs of success.",
        'Efficiency Ratios': "⚙️ **Efficiency Ratios** measure how effectively a company uses its assets to generate sales. A high Asset Turnover is a good sign."
    }

    insights = descriptions.get(category_name, insights)
    key_ratio_name = key_ratios.get(category_name)

    if key_ratio_name:
        key_ratio_data = data_df[data_df['Ratio Name'] == key_ratio_name]
        
        last_year_series = key_ratio_data[key_ratio_data['Year'] == "Mar '25'"]['Value']
        prev_year_series = key_ratio_data[key_ratio_data['Year'] == "Mar '24'"]['Value']

        if not last_year_series.empty and not prev_year_series.empty:
            last_year_val = last_year_series.iloc[0]
            prev_year_val = prev_year_series.iloc[0]

            if last_year_val > prev_year_val:
                trend = "an **improving**"
                if key_ratio_name == 'Debt-to-Equity Ratio': trend = "an **increasing** (less favorable)"
            elif last_year_val < prev_year_val:
                trend = "a **declining**"
                if key_ratio_name == 'Debt-to-Equity Ratio': trend = "a **decreasing** (more favorable)"
            else:
                trend = "a **stable**"
            
            trend_insight = f"The key ratio, **{key_ratio_name}**, shows {trend} trend in the last year, moving from {prev_year_val:.2f} to {last_year_val:.2f}."

    return insights, trend_insight

# --- Streamlit App Layout ---
st.title("📈 Britannia Industries: Financial Ratio Analysis")

# --- Sidebar Controls ---
st.sidebar.title("Dashboard Controls")
st.sidebar.markdown("---")
category_options = df['Category'].unique()
selected_category = st.sidebar.radio(
    "Select a Ratio Category to Analyze:",
    options=category_options
)

# --- Main Panel Display ---
filtered_df = df[df['Category'] == selected_category].copy()
st.header(f"📊 Visualizing: {selected_category}")

# --- Display Insights Section ---
st.markdown("---")
category_explanation, trend_explanation = get_category_insights(selected_category, filtered_df)
info_col, trend_col = st.columns(2)
with info_col:
    st.info(category_explanation)
with trend_col:
    st.success(trend_explanation)
st.markdown("---")

# --- Display Charts in a Grid ---
ratios_to_plot = filtered_df['Ratio Name'].unique()
col1, col2 = st.columns(2)

for i, ratio_name in enumerate(ratios_to_plot):
    ratio_df = filtered_df[filtered_df['Ratio Name'] == ratio_name]
    fig = px.line(
        ratio_df, x='Year', y='Value', title=f"Trend for: {ratio_name}",
        markers=True, text="Value"
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='top center')
    fig.update_layout(xaxis_title=None, yaxis_title="Value", title_font_size=16)

    if i % 2 == 0:
        with col1:
            st.plotly_chart(fig, use_container_width=True)
    else:
        with col2:
            st.plotly_chart(fig, use_container_width=True)

# --- Display Filtered Data Table ---
st.markdown("---")
st.subheader(f"Data for {selected_category}")
st.dataframe(filtered_df[['Ratio Name', 'Year', 'Value']])