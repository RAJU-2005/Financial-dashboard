import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page configuration to a wide layout for a better dashboard experience
st.set_page_config(layout="wide")

# --- Data Preparation ---
# This is the complete and corrected dataset from all four of your images.
data = [
    # Liquidity Ratios
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 1.6583764},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 1.2718468},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 1.1443558},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 0.7323746},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 0.7513059},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 0.612540614},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 0.130306},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 0.6136503},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 0.1821464},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Current Ratio', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 0.69466103},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 0.9461467},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 0.7105911},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 0.6083128},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 0.2253343},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 0.2212118},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 0.153686231},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 0.1553135},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 0.1436805},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 0.2858328},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Quick Ratio', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 0.20663665},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 0.3260528},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 0.1444684},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 0.067945},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 0.0263072},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 0.0558468},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 0.039454303},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 0.0006535},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 0.0039752},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 0.1068076},
    {'Category': 'Liquidity Ratios', 'Ratio Name': 'Cash Ratio', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 0.01643514},

    # Solvency Ratios
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 0},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 0},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 0.0031026},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 0.1061459},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 0.0097461},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 0.541417008},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 0.9065988},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 0.8367351},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 0.5774392},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt-to-Equity Ratio', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 0.3130154},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 0},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 0},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 0.003093},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 0.0959601},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 0.009652},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 0.351245232},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 0.4755058},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 0.4555557},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 0.3660853},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Debt Ratio', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 0.23839431},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 18.45567},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 21.442154},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 21.577788},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 13.622602},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 7.2478291},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 23.65825068},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 15.405226},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 18.864577},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 18.773841},
    {'Category': 'Solvency Ratios', 'Ratio Name': 'Times Interest Earned', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 22.1519452},
    
    # Profitability Ratios
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 5693.37},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 7313.88},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 8150.93},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 8612.18},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 9838.16},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 6710.02},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 8575.20},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 9891.18},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 9543.64},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'COGS', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 10684.94},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 0.51},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 0.41},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 1.0},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 0.44},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 0.44},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 0.49},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 0.39},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 0.33},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 0.43},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Gross Profit Margin', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 0.40},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 0.1330595},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 0.1383283},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 0.1346912},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 0.1502119},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 0.1407258},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 0.191021868},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 0.155735},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 0.1736696},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 0.1890267},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Operating Profit Margin', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 0.17762964},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 0.0792982},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 0.0804459},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 0.0976931},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 0.0812792},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 0.0778554},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 0.141823335},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 0.1072547},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 0.1421032},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 0.1277933},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Net Profit Margin', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 0.12202587},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 0.0821282},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 0.0851419},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 0.1054366},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 0.0821153},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 0.0798615},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 0.364113753},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 0.3309945},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 0.3964381},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 0.3851089},
    {'Category': 'Profitability Ratios', 'Ratio Name': 'Return on Assets (ROA)', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 0.42904705},

    # Efficiency Ratios
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 8.0859007},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 5.4574881},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 6.0997628},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 5.8461382},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 5.3396147},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 13.53809216},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 7.6464609},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 8.5033334},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 8.8775569},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Inventory Turnover', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 9.6944573},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 90.207441},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 46.106124},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 44.218604},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 36.704725},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 34.06082},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 132.4474652},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 62.520776},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 61.249178},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 53.621341},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Receivable Turnover', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 49.3825893},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 19.481366},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 10.585098},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 11.181368},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 10.77703},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 11.348368},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 22.05734243},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 12.042535},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 13.22356},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 11.885032},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Accounts Payable Turnover', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 11.5552658},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '21", 'Company': 'Tata Consumer Products', 'Value': 2.0713768},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '22", 'Company': 'Tata Consumer Products', 'Value': 1.0831648},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '23", 'Company': 'Tata Consumer Products', 'Value': 1.1246533},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '24", 'Company': 'Tata Consumer Products', 'Value': 1.0930834},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '25", 'Company': 'Tata Consumer Products', 'Value': 1.093395},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '21", 'Company': 'Britannia Industries', 'Value': 5.134533828},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '22", 'Company': 'Britannia Industries', 'Value': 2.9154562},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '23", 'Company': 'Britannia Industries', 'Value': 3.1276209},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '24", 'Company': 'Britannia Industries', 'Value': 2.9400198},
    {'Category': 'Efficiency Ratios', 'Ratio Name': 'Asset Turnover', 'Year': "Mar '25", 'Company': 'Britannia Industries', 'Value': 3.36390582},
]

# Convert the list into a pandas DataFrame
df = pd.DataFrame(data)

# --- Function to Generate Comparative Insights ---
def get_comparison_insights(category_name, data_df):
    """Generates a comparative insight for the latest year."""
    insights = "No description available."
    trend_insight = "Could not generate a comparison."
    
    key_ratios = {
        'Liquidity Ratios': 'Current Ratio', 'Solvency Ratios': 'Debt-to-Equity Ratio',
        'Profitability Ratios': 'Net Profit Margin', 'Efficiency Ratios': 'Asset Turnover'
    }
    descriptions = {
        'Liquidity Ratios': "💧 **Liquidity Ratios** measure a company's ability to pay its short-term debts. Higher values are generally better.",
        'Solvency Ratios': "🏦 **Solvency Ratios** assess long-term financial health. A lower Debt-to-Equity ratio is often preferred.",
        'Profitability Ratios': "💰 **Profitability Ratios** show how well a company generates profit. Higher margins and returns are signs of success.",
        'Efficiency Ratios': "⚙️ **Efficiency Ratios** measure how effectively a company uses its assets to generate sales. Higher turnover is a good sign."
    }

    insights = descriptions.get(category_name, insights)
    key_ratio_name = key_ratios.get(category_name)

    if key_ratio_name:
        latest_data = data_df[(data_df['Ratio Name'] == key_ratio_name) & (data_df['Year'] == "Mar '25'")]
        
        tata_val_series = latest_data[latest_data['Company'] == 'Tata Consumer Products']['Value']
        brit_val_series = latest_data[latest_data['Company'] == 'Britannia Industries']['Value']

        if not tata_val_series.empty and not brit_val_series.empty:
            tata_val = tata_val_series.iloc[0]
            brit_val = brit_val_series.iloc[0]
            
            winner = "Britannia Industries" if brit_val > tata_val else "Tata Consumer Products"
            # For solvency, lower is better, so we flip the winner
            if key_ratio_name == 'Debt-to-Equity Ratio':
                 winner = "Tata Consumer Products" if brit_val > tata_val else "Britannia Industries"

            trend_insight = f"In Mar '25, **{winner}** showed a more favorable **{key_ratio_name}** ({brit_val:.2f} vs {tata_val:.2f} for Tata)."

    return insights, trend_insight

# --- Streamlit App Layout ---
st.title("📊 Comparative Financial Analysis: Tata vs. Britannia")

# --- Sidebar Controls ---
st.sidebar.title("Dashboard Controls")
st.sidebar.markdown("---")
category_options = df['Category'].unique()
selected_category = st.sidebar.radio("Select a Ratio Category to Compare:", options=category_options)

# --- Main Panel Display ---
filtered_df = df[df['Category'] == selected_category].copy()
st.header(f"📈 Comparing: {selected_category}")

# --- Display Insights Section ---
st.markdown("---")
category_explanation, trend_explanation = get_comparison_insights(selected_category, filtered_df)
info_col, trend_col = st.columns(2)
with info_col:
    st.info(category_explanation)
with trend_col:
    st.success(trend_explanation)
st.markdown("---")

# --- Create Pivot Table for Charts and Final Table ---
pivot_df_category = filtered_df.pivot_table(index=['Ratio Name', 'Year'], columns='Company', values='Value').reset_index()
if 'Britannia Industries' in pivot_df_category.columns and 'Tata Consumer Products' in pivot_df_category.columns:
    pivot_df_category['Value Difference'] = pivot_df_category['Britannia Industries'] - pivot_df_category['Tata Consumer Products']

# --- Display Comparative Charts and Difference Bars ---
ratios_to_plot = filtered_df['Ratio Name'].unique()
for ratio_name in ratios_to_plot:
    
    chart_col, diff_col = st.columns(2)

    with chart_col:
        # Data for the line chart
        line_chart_df = filtered_df[filtered_df['Ratio Name'] == ratio_name]
        fig_line = px.line(
            line_chart_df, x='Year', y='Value', color='Company',
            title=f"5-Year Trend for: {ratio_name}",
            markers=True,
            color_discrete_map={
                'Tata Consumer Products': '#1f77b4', # blue
                'Britannia Industries': '#ff7f0e'  # orange
            }
        )
        fig_line.update_layout(xaxis_title=None, yaxis_title="Value", legend_title="Company")
        st.plotly_chart(fig_line, use_container_width=True)

    with diff_col:
        # Data for the bar chart
        diff_chart_df = pivot_df_category[pivot_df_category['Ratio Name'] == ratio_name]
        
        # Color bars based on positive or negative difference
        diff_chart_df['Color'] = ['green' if x > 0 else 'red' for x in diff_chart_df['Value Difference']]
        
        fig_bar = px.bar(
            diff_chart_df, x='Year', y='Value Difference',
            title=f"Difference (Britannia - Tata)",
            labels={'Value Difference': 'Difference Value'}
        )
        fig_bar.update_traces(marker_color=diff_chart_df['Color'])
        st.plotly_chart(fig_bar, use_container_width=True)


# --- Display Data Table with Differences ---
st.markdown("---")
st.subheader(f"Data for {selected_category}")
st.dataframe(pivot_df_category)