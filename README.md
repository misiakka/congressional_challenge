# FoodRescue (organized Streamlit demo)

## Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Structure
- `app.py` — application entry point and page routing
- `components/navigation.py` — sidebar and logout
- `components/cards.py` / `footer.py` — shared UI
- `views/home.py` — public landing dashboard
- `views/signup.py` — **demo profile** form (not authentication)
- `views/donate.py` / `find_food.py` — donation and claiming flows
- `data/state.py` / `donations.py` — temporary session data and helpers
- `styles/main.css` — forest-green styling

**Important:** No real accounts are created. The demo profile does not verify identity or store passwords. Donations are stored in Streamlit session state, not a shared database. Do not use real personal information. A production deployment needs proper authentication, access controls, and persistent storage.

## Replacing your existing project
Copy the files into your existing `congressional_challenge` folder (not the folder itself), retaining its `.git` and `.venv`. Remove any obsolete `pages/` folder if it contains duplicate Streamlit navigation, and remove unused empty `navbar.py` or `dashboard.py` files. Back up first. Test before committing.


## Visual update
- White background and squared-off cards/buttons.
- Sidebar starts collapsed; its toggle is styled as a three-line hamburger icon using CSS (Streamlit DOM selectors may change between versions).
- Sign Up button appears at the top of the Home dashboard.
- Non-fruit emojis removed. Fruit icon retained in the browser tab and sidebar.

## Mission landing page redesign
- Home is now mission-first, with a locally bundled food image and no food listings or metrics.
- All pages have a top-right Sign Up action, changing to Log Out for active demo profiles.
- The Home page also includes a prominent Sign Up call to action.
- Dark-green buttons use white text; backgrounds remain white and cards boxy.
- No external image service is required at runtime.
