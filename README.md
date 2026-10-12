# FoodRescue — polished Streamlit prototype

## Start
From the project folder:

```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```

## What changed
- Replaced sidebar radio (which shared the `current_page` widget key) with buttons. Navigation now uses a separate session key and no longer triggers the StreamlitAPIException.
- Removed conflicting hamburger CSS. The native Streamlit sidebar toggle stays accessible; its exact icon is Streamlit-version-dependent.
- Unified white-and-forest-green styling, cards, typography, header, and mobile spacing.
- Wired signup, login, logout, and role-specific pages.
- Updated theme to white to avoid yellow flash/background.
- Excluded private/local database and environment files from Git.

## Important limitations
- Accounts are stored locally in `data/foodrescue.db`; this is **not** production-ready authentication. Use test credentials only. A production release needs secure hosting, persistent shared database, rate limiting, recovery, and robust session management.
- Donation listings and claims are **session-only demo data**, not shared between visitors, even though accounts use SQLite.
- The sidebar uses Streamlit's native toggle rather than a custom three-line icon to avoid fragile CSS and broken opening/closing.
- The uploaded ZIP contained a local database; it has intentionally **not** been included in this package. Keep your existing database locally if you want to retain test accounts.

## Integrate into your existing Git project
Back up your project. Copy the contents of this folder into the existing project directory, **not** the containing folder itself. Preserve your existing `.git` and any local database. Restart Streamlit, test navigation and authentication, then commit your code (never the database or secrets).
