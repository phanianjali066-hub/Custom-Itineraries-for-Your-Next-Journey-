import streamlit as st
import google.generativeai as genai

# --- MILESTONE 2: INITIALIZING THE MODEL ---
# Recommendation: Move this to streamlit secrets or an environment variable later!
API_KEY = "AIzaSyBi378yRdGGHeXjAOskWCNbqo1ZM80uYVs" 
genai.configure(api_key=API_KEY)

# Using gemini-1.5-flash for speed and reliability
model = genai.GenerativeModel('gemini-2.5-flash')

# --- MILESTONE 3: INTERFACING WITH THE MODEL ---
def generate_itinerary(destination, days, nights):
    prompt = f"""
    You are an expert travel guide. Create a highly detailed itinerary for {destination}.
    Trip length: {days} days and {nights} nights.
    Please include:
    - Daily morning, afternoon, and evening activities.
    - Specific local restaurant names and what to order.
    - Important travel tips for this location.
    Format the response clearly with bold headers and bullet points.
    """
    response = model.generate_content(prompt)
    return response.text

# --- MILESTONE 4: MODEL DEPLOYMENT (Streamlit UI) ---
def main():
    # Fixed the SyntaxError here by removing hidden characters
    st.set_page_config(page_title="TravelGuideAI", page_icon="✈️")
    
    st.title("🌍 Travel Itinerary Generator")
    st.write("Let AI plan your next dream vacation!")

    # User Input Fields
    destination = st.text_input("Enter your desired destination:", placeholder="e.g. Kyoto, Japan")
    
    col1, col2 = st.columns(2)
    with col1:
        days = st.number_input("Number of days:", min_value=1, step=1, value=3)
    with col2:
        nights = st.number_input("Number of nights:", min_value=0, step=1, value=2)

    # Logic Trigger
    if st.button("Generate Itinerary"):
        if destination.strip():
            with st.spinner(f"Researching the best of {destination}..."):
                try:
                    itinerary = generate_itinerary(destination, days, nights)
                    st.success("Here is your custom plan!")
                    st.markdown("---")
                    st.markdown(itinerary) 
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.error("Please provide a destination first.")

if __name__ == "__main__":
    main()