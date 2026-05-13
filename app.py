import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📈",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #f0f2f6;
}

div[data-testid="metric-container"] {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}

h1 {
    color: #1f77b4;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.title("📈 Sales Prediction")

st.write(
    "Interactive business sales forecasting system"
)

st.markdown("---")

# =========================================
# SIDEBAR INPUTS
# =========================================

st.sidebar.header("📥 Business Inputs")

marketing = st.sidebar.slider(
    "Marketing Spend ($)",
    1000,
    100000,
    10000
)

customers = st.sidebar.slider(
    "Customers",
    10,
    2000,
    300
)

discount = st.sidebar.slider(
    "Discount (%)",
    0,
    50,
    10
)

store_size = st.sidebar.slider(
    "Store Size",
    500,
    10000,
    2000
)

holiday = st.sidebar.selectbox(
    "Holiday Season",
    ["No", "Yes"]
)

# =========================================
# SALES PREDICTION
# =========================================

holiday_value = 7000 if holiday == "Yes" else 0

predicted_sales = (
    marketing * 0.4
    + customers * 35
    + store_size * 2
    - discount * 120
    + holiday_value
)

# =========================================
# KPI SECTION
# =========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Predicted Sales",
        f"${predicted_sales:,.0f}"
    )

with col2:
    st.metric(
        "Customers",
        customers
    )

with col3:
    st.metric(
        "Marketing",
        f"${marketing:,.0f}"
    )

with col4:
    st.metric(
        "Discount",
        f"{discount}%"
    )

st.markdown("---")

# =========================================
# SALES INSIGHTS
# =========================================

st.subheader("📊 Sales Insights")

if predicted_sales > 60000:

    st.success("🚀 Strong Sales Growth Expected")

elif predicted_sales > 30000:

    st.info("👍 Moderate Sales Growth")

else:

    st.warning("📉 Sales May Be Low")

# =========================================
# PERFORMANCE BAR
# =========================================

st.subheader("🎯 Sales Performance")

performance = min(int(predicted_sales / 700), 100)

st.progress(performance)

# =========================================
# CHARTS LAYOUT
# =========================================

left_col, right_col = st.columns(2)

# =========================================
# LINE CHART
# =========================================

with left_col:

    st.subheader("📈 Monthly Sales Trend")

    months = [
        "Jan", "Feb", "Mar",
        "Apr", "May", "Jun"
    ]

    sales = [
        predicted_sales * 0.5,
        predicted_sales * 0.6,
        predicted_sales * 0.7,
        predicted_sales * 0.8,
        predicted_sales * 0.9,
        predicted_sales
    ]

    sales_df = pd.DataFrame({
        "Month": months,
        "Sales": sales
    })

    fig, ax = plt.subplots(figsize=(6,4))

    ax.plot(
        sales_df["Month"],
        sales_df["Sales"],
        marker='o',
        linewidth=3
    )

    ax.fill_between(
        sales_df["Month"],
        sales_df["Sales"],
        alpha=0.3
    )

    ax.set_title("Monthly Sales Trend")

    st.pyplot(fig)

# =========================================
# PIE CHART
# =========================================

with right_col:

    st.subheader("🧾 Business Contribution")

    labels = [
        "Marketing",
        "Customers",
        "Store Size"
    ]

    values = [
        marketing,
        customers,
        store_size
    ]

    fig2, ax2 = plt.subplots(figsize=(6,4))

    ax2.pie(
        values,
        labels=labels,
        autopct='%1.1f%%'
    )

    st.pyplot(fig2)

# =========================================
# DATA TABLE
# =========================================

st.subheader("📋 Sales Data Table")

st.dataframe(sales_df)

# =========================================
# FOOTER
# =========================================

st.markdown("---")

st.caption(
    "Built using Streamlit, Pandas & Machine Learning"
)