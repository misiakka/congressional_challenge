# FoodRescue

Organized Streamlit prototype, preserving the original forest-green theme and donation workflows.

## Run

From this directory, with your Python environment activated:

```bash
pip install -r requirements.txt
streamlit run app.py
```

- `app.py`: entry point and routing
- `styles/main.css`: visual styling
- `views/`: Home, Donate Food, and Find Food screens
- `components/`: sidebar, listing cards, footer
- `data/`: session state and donation helpers

Donations are still demo-only and stored in the current Streamlit session, not in a database.
