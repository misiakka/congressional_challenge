# FoodRescue

A student-built Streamlit app that helps local food businesses share surplus food with community organizations.

## Run locally

1. Open this folder in VS Code.
2. In the terminal run `python3 -m pip install -r requirements.txt`.
3. Run `python3 -m streamlit run app.py`.
4. Create a **test donor** account to post food, then log out and create a **test community organization** account to claim it. Check **My Activity** to mark pickup complete.

## What works

- Registration, login, logout, and account types.
- SQLite storage for accounts and donations (`data/foodrescue.db`, created automatically).
- Donors can post and cancel their available donations.
- Organizations can browse, search, filter, and claim available food.
- Either side of a claimed donation can confirm completion.
- The claim update is atomic, so two organizations cannot both claim the same listing.

## Important prototype limits

- No email verification, password reset, account recovery, or pickup messaging.
- Pickup details are entered by donors and coordination happens outside the app.
- Accounts use PBKDF2 password hashing but this is not audited production authentication. Avoid real personal information.
- SQLite persistence works on your local machine. Many free/cloud Streamlit hosts have **ephemeral disks**; use a hosted database for real deployment.
- The app does not determine whether food is safe to distribute. Donors and receivers must follow food-safety guidance.
- AI is intentionally not enabled and **no API key is included**. An AI assistant can be added later without changing the core workflow.

## Project organization

`app.py` handles page routing; `views/` holds each page; `data/database.py` contains SQL and account logic; `components/` contains shared UI; `styles/main.css` contains the theme.

Never commit `.streamlit/secrets.toml`, `.env`, or database files. If a key has been exposed, revoke it and use a new one.


## Design update
The Ocean Blue theme uses a blue-gray header, navy buttons, white background, and a pale sidebar. On desktop the sidebar opens expanded by default. You can still collapse it with Streamlit's native control. No account, database, or donation logic was changed in this update.
