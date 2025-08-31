import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_about():
    # main content wrapper
    st.markdown("""
    <div class="main-content">
    """, unsafe_allow_html=True)

    # what is food disposal
    col1, col2 = st.columns([1,2]) 

    with col1:
        st.image("https://raw.githubusercontent.com/nabihahadnin/food-disposal-app/main/img/Compost%20cycle-bro.png", width=300)

    with col2:
        st.markdown("""<p style='font-size:30px; font-weight: 600; color: #16a34a'> What is Food Waste Disposal?</p>""", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size:16px; line-height:1.5;'>
            Food waste disposal refers to the process of <b>properly managing and getting rid of leftover or unwanted food</b>. 
            Instead of throwing food waste into the regular trash, which ends up in landfills and produces harmful greenhouse gases, 
            food waste disposal involves methods like <b>composting, recycling, or donating edible food</b>. Proper food waste disposal helps <b>reduce 
            environmental impact and supports sustainable living</b>.
            </p>
        """, unsafe_allow_html=True)

    # why is food waste disposal important
    st.markdown("""
            <p style='font-size:23px; font-weight: 400; margin-top: 60px; margin-bottom: 40px; text-align: center; color: #16a34a'>
            Why is Proper Food Waste Disposal Important?
            </p>
            
            <div class="custom-columns">
                <div class="column left">
                    <h5>Mitigate Climate Change 🌡️</h5>
                    <p>Wasted food in landfills rots and produces methane, a greenhouse gas 28 times as powerful as CO2. With proper food disposal, greenhouse gas emissions can be reduced, contributing to climate change mitigation.</p>
                </div>
                <div class="column middle">
                    <h5>Returns Nutrients to the Soil 🌱</h5>
                    <p>Inedible parts of food can be used to create compost which can return valuable nutrients to the soil, promoting healthy plant growth and reducing the need for chemical fertilizers.</p>
                </div>
                <div class="column right">
                    <h5>Supports Circular Economy 🔁</h5>
                    <p>Proper food disposal contributes to a circular economy by reintroducing organic waste back into the production cycle, reducing the need for natural resources and minimizing waste.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # how food waste can be disposed properly
    col3, col4 = st.columns([1,2]) 

    with col3:
        st.image("https://raw.githubusercontent.com/nabihahadnin/food-disposal-app/main/img/Volunteering-bro.png", width=300)

    with col4:
        st.markdown("""<p style='font-size:23px; font-weight: 400; color: #16a34a'> How Food Waste Can Be Disposed Properly?</p>""", unsafe_allow_html=True)
        st.markdown("""
            <ul style='font-size:16px;'>
                <li><b>Anaerobic Digestion:</b> This process involves breaking down organic material in the absence of oxygen, producing biogas that can be used for energy.</li>
                <li><b>Composting:</b> Composting is the natural decomposition of organic material, such as food scraps and yard waste, into a nutrient-rich soil amendment.</li>
                <li><b>Donation:</b> Edible food that is no longer wanted can be donated to food banks or shelters, helping those in need while reducing waste.</li>
                <li><b>Animal Feed:</b> Some food waste can be repurposed as animal feed, providing a sustainable food source for livestock.</li>
                <li><b>Industrial Uses:</b> Food waste can be processed into biofuels or other industrial products, contributing to a circular economy.</li>
            </ul>
        """, unsafe_allow_html=True)

    # how our locator works
    st.markdown("""
            <p style='font-size:23px; font-weight: 400; margin-top: 40px; text-align: center; color: #16a34a'>
            How Our Locator Works 📌
            </p>
            <p style='font-weight: 400; margin-bottom: 40px; text-align: center'>
            Food waste disposal centers are facilities that specialize in the proper disposal and management of food waste. 
                They play a crucial role in reducing food waste and promoting sustainable practices. 
                Our locator helps users find these centers in Kuala Lumpur and Selangor easily.
            </p>
                
            <div class="custom-columns">
                <div class="column left">
                    <h5>Location-Based Search ✅</h5>
                    <p>Our locator allows you to enter your location to find the nearest food waste disposal centers, making it easy to find a facility near you.</p>
                </div>
                <div class="column middle">
                    <h5>Verified Locations ✅</h5>
                    <p>All listed food waste disposal centers are obtained from verified sources, ensuring you have the most reliable information at your fingertips.</p>
                </div>
                <div class="column right">
                    <h5>Easy Access ✅</h5>
                    <p>Our locator provides easy access to information about food waste disposal centers, helping you make informed decisions about waste management.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # close the main content wrapper
    st.markdown('</div>', unsafe_allow_html=True)
