import streamlit as st
import utils  

st.title("🪙 Crypto Market Monitor")

# Executes when the user clicks the button
if st.button("Refresh Market Data"):
    # Fetch data and store it in local variables
    market_data, report = utils.get_crypto_prices_and_save()
    
    # 1. Subheader and divider
    st.subheader("📊 Crypto Market Report")
    st.divider()
        
    # 2. Use st.metric for highlighted data visualization
    # Arrange metrics in three columns for a clean layout
    col1, col2, col3 = st.columns(3)
        
    # Display price and 24hr change for each coin    
    col1.metric("Bitcoin", f"${market_data['btc']['price']:,}", f"{market_data['btc']['change']:.2f}%")
    col2.metric("Ethereum", f"${market_data['eth']['price']:,}", f"{market_data['eth']['change']:.2f}%")
    col3.metric("Ripple", f"${market_data['xrp']['price']:.4f}", f"{market_data['xrp']['change']:.2f}%")

    st.success("Data updated!")