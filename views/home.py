"""Homepage: mission, workflow, and paths into the working demo."""
import streamlit as st
from pathlib import Path
import base64
from components.navigation import go_to


def start_demo(role):
    st.session_state.demo_role = role
    go_to("Demo Studio")


def render():
    logo = Path(__file__).resolve().parents[1] / "assets" / "foodrescue_logo.png"
    logo_data = base64.b64encode(logo.read_bytes()).decode("ascii")
    st.markdown(f'<div class="fr-home-logo"><img src="data:image/png;base64,{logo_data}" alt="FoodRescue official logo"></div>', unsafe_allow_html=True)
    st.markdown("""
    <section class="fr-hero">
      <div class="fr-hero-content">
        <div class="fr-kicker">LESS WASTE · MORE GOOD</div>
        <h1>Good Food<br>Shouldn't Go to Waste.</h1>
        <p>FoodRescue is designed to connect local businesses with food banks, making it easier to share surplus food and support our communities.</p>
        <div class="fr-hero-benefits"><span>🌱 Reduce waste</span><span>♡ Support communities</span><span>⌂ Connect locally</span></div>
      </div>
    </section>
    """, unsafe_allow_html=True)
    a,b,c = st.columns([1,1,3])
    with a:
        if st.button("Get Started →", key="start_home", type="primary", use_container_width=True):
            go_to("Account")
    with b:
        if st.button("Try Demo →", key="try_home", use_container_width=True):
            start_demo("Business")

    st.markdown('<div class="fr-section"><small>THE PROCESS</small><h2>How FoodRescue Works</h2><p>A simple way to connect surplus food with local food banks.</p></div>', unsafe_allow_html=True)
    steps = [
        ("01", "Businesses post donations", "Local businesses list surplus food they would otherwise waste."),
        ("02", "Food banks browse & request", "Food banks discover available food and request what they need."),
        ("03", "Coordinate pickup", "The business and food bank can arrange a pickup."),
    ]
    for col, (number,title,desc) in zip(st.columns(3),steps):
        with col:
            st.markdown(f'<div class="fr-step"><div class="fr-number">{number}</div><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="fr-section"><small>EXPLORE THE POSSIBILITIES</small><h2>Food that could be shared</h2><p>Illustrative categories, not actual donations.</p></div>', unsafe_allow_html=True)
    foods=[("🥖","Bakery","Bread & pastries"),("🥬","Produce","Fresh vegetables"),("🥛","Dairy","Dairy products"),("🥗","Prepared food","Prepared meals")]
    for col,(emoji,category,name) in zip(st.columns(4),foods):
        with col:
            st.markdown(f'<div class="fr-food"><div class="fr-emoji">{emoji}</div><small>{category}</small><h3>{name}</h3><p>Example food category</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="fr-section"><small>INTERACTIVE WALKTHROUGH</small><h2>One platform. Two perspectives.</h2><p>Try both sides of the app using fictional demonstration listings.</p></div>', unsafe_allow_html=True)
    business,bank=st.columns(2)
    with business:
        st.markdown('<div class="fr-role"><h3>🏪 Business perspective</h3><p>Create listings and manage incoming requests.</p></div>',unsafe_allow_html=True)
        if st.button("View as Business →",use_container_width=True,key="role_biz"):start_demo("Business")
    with bank:
        st.markdown('<div class="fr-role"><h3>♡ Food bank perspective</h3><p>Browse available listings and request food.</p></div>',unsafe_allow_html=True)
        if st.button("View as Food Bank →",use_container_width=True,key="role_bank"):start_demo("Food Bank")
    st.markdown('<div class="fr-mission"><small>OUR MISSION</small><h2>Less food waste. Stronger communities.</h2><p>We are building FoodRescue to help local organizations connect surplus food with people who need it.</p></div>',unsafe_allow_html=True)
    st.caption("Prototype notice: no food distribution is claimed. All demonstration listings and actions are fictional.")
