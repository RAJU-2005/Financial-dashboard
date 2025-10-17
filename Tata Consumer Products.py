import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page configuration to a wide layout for a better dashboard experience
st.set_page_config(layout="wide")

# --- Data Preparation ---
# Data for Tata Consumer Products, carefully transcribed from your images.
data = [
    # Liquidity Ratios
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '21", 'Value': 1.6583764},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '22", 'Value': 1.2718468},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '23", 'Value': 1.1443558},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '24", 'Value': 0.7323746},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '25", 'Value': 0.7513059},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '21", 'Value': 0.9461467},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '22", 'Value': 0.7105911},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '23", 'Value': 0.6083128},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '24", 'Value': 0.2253343},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '25", 'Value': 0.2212118},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '21", 'Value': 0.3260528},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '22", 'Value': 0.1444684},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '23", 'Value': 0.067945},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '24", 'Value': 0.0263072},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '25", 'Value': 0.0558468},

    # Solvency Ratios
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '21", 'Value': 0},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '22", 'Value': 0},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '23", 'Value': 0.0031026},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '24", 'Value': 0.1061459},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '25", 'Value': 0.0097461},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '21", 'Value': 0},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '22", 'Value': 0},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '23", 'Value': 0.003093},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '24", 'Value': 0.0959601},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '25", 'Value': 0.009652},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '21", 'Value': 18.45567},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '22", 'Value': 21.442154},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '23", 'Value': 21.577788},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '24", 'Value': 13.622602},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '25", 'Value': 7.2478291},

    # Profitability Ratios
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '21", 'Value': 5693.37},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '22", 'Value': 7313.88},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '23", 'Value': 8150.93},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '24", 'Value': 8612.18},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '25", 'Value': 9838.16},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '21", 'Value': 0.51},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '22", 'Value': 0.41},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '23", 'Value': 1},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '24", 'Value': 0.44},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '25", 'Value': 0.44},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '21", 'Value': 0.1330595},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '22", 'Value': 0.1383283},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '23", 'Value': 0.1346912},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '24", 'Value': 0.1502119},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '25", 'Value': 0.1407258},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '21", 'Value': 0.0792982},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '22", 'Value': 0.0804459},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '23", 'Value': 0.0976931},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '24", 'Value': 0.0812792},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '25", 'Value': 0.0778554},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '21", 'Value': 0.0821282},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '22", 'Value': 0.0851419},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '23", 'Value': 0.1054366},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '24", 'Value': 0.0821153},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '25", 'Value': 0.0798615},

    # Efficiency Ratios
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '21", 'Value': 8.0859007},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '22", 'Value': 5.4574881},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '23", 'Value': 6.0997628},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '24", 'Value': 5.8461382},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '25", 'Value': 5.3396147},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '21", 'Value': 90.207441},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '22", 'Value': 46.106124},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '23", 'Value': 44.218604},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '24", 'Value': 36.704725},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '25", 'Value': 34.06082},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable', 'Year': "Mar '21", 'Value': 19.481366},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable', 'Year': "Mar '22", 'Value': 10.585098},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable', 'Year': "Mar '23", 'Value': 11.181368},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable', 'Year': "Mar '24", 'Value': 10.77703},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable', 'Year': "Mar '25", 'Value': 11.348368},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '21", 'Value': 2.0713768},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '22", 'Value': 1.0831648},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '23", 'Value': 1.1246533},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '24", 'Value': 1.0930834},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '25", 'Value': 1.093395},
]

# Convert the list into a pandas DataFrame
df = pd.DataFrame(data)

# --- Function to Generate Insights ---
def get_category_insights(category_name, data_df):
    """Generates an explanation and a simple trend insight for a given ratio category."""
    insights = "No description available."
    trend_insight = "Could not generate a trend insight."
    
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
st.title("📈 Tata Consumer Products: Financial Ratio Analysis")

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