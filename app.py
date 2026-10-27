import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="VELOOP Data Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Header Section
st.title("📊 VELOOP Data Analytics & Governance Dashboard")
st.markdown("**Author:** Nandala Srilatha | Data Science & Analytics Intern")
st.markdown("---")

# Sidebar Filters
st.sidebar.header("Filter & Settings")
time_range = st.sidebar.selectbox("Select Time Horizon", ["Last 7 Days", "Last 30 Days", "Quarter to Date"])
st.sidebar.info("Framework aligned with `User_Analytics_Spec`, `Reward_Analytics_Spec`, and `Wallet_Withdrawal_Spec`.")

# Key Performance Indicators (KPIs)
st.subheader("📌 Key Ecosystem Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Verified Users", value="1,000", delta="+12% vs last week")
with col2:
    st.metric(label="Reward Credits Issued", value="154,200 Pts", delta="+5.4%")
with col3:
    st.metric(label="Payout Conversion Rate", value="4.2%", delta="-0.3% (Healthy)")
with col4:
    st.metric(label="Flagged High-Risk Transactions", value="3", delta="-2 (Low Risk)")

st.markdown("---")

# Main Dashboard Content - Tabs
tab1, tab2, tab3 = st.tabs(["👤 User Analytics", "🎁 Reward Analytics", "💳 Wallet & Withdrawal Risk"])

with tab1:
    st.header("User Lifecycle & Engagement Analytics")
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Daily vs Monthly Active Users (DAU/MAU)")
        chart_data = pd.DataFrame(
            np.random.randint(100, 500, size=(10, 2)),
            columns=["DAU", "MAU"]
        )
        st.line_chart(chart_data)
    with col_b:
        st.subheader("User Acquisition Channels")
        acq_data = pd.DataFrame({
            "Channel": ["Referral Bonus", "Organic Direct", "Campaign Links", "Social Share"],
            "Users": [450, 300, 150, 100]
        })
        st.bar_chart(acq_data.set_index("Channel"))

with tab2:
    st.header("Reward Payout & Credit Conversion")
    col_c, col_d = st.columns(2)
    with col_c:
        st.subheader("Reward Distribution Breakdown")
        reward_df = pd.DataFrame({
            "Reward Category": ["Task Completion", "Referral Credits", "Streak Bonuses", "Special Event"],
            "Points Distributed": [70000, 45000, 25000, 14200]
        })
        st.dataframe(reward_df, use_container_width=True)
    with col_d:
        st.subheader("Points Liability vs Claimed Payouts")
        st.area_chart(chart_data)

with tab3:
    st.header("Wallet Withdrawal & Risk Velocity Detection")
    st.warning("⚡ Monitoring Rule Active: Flagging accounts exceeding > 5 transactions/hour.")
    
    risk_df = pd.DataFrame({
        "User ID": ["USR_089", "USR_341", "USR_892"],
        "Transaction Velocity": ["7 txns / hr", "6 txns / hr", "9 txns / hr"],
        "Withdrawal Amount": ["$250", "$180", "$500"],
        "Risk Status": ["Flagged for Review", "Flagged for Review", "Account Suspended"],
        "Action Required": ["Manual Verification", "Manual Verification", "Fraud Audit"]
    })
    st.table(risk_df)

st.markdown("---")
st.caption("VELOOP Data Governance & Verification Register Framework | Active Development Day")
