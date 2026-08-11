import streamlit as st
import streamlit.components.v1 as components

# Streamlit Page Config
st.set_page_config(page_title="Discipline Hub", layout="wide")

# HTML Content wrapped safely inside Python triple-quotes
html_code = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Discipline Hub | Student Productivity Mobile App</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- CDN Dependencies -->
  <script src="https://cdn.jsdelivr.net/npm/lucide@latest/dist/umd/lucide.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>
  <style>
    body { background-color: #090d16; color: #ffffff; font-family: 'Inter', sans-serif; padding: 20px; }
    .card { background: #131b2e; padding: 20px; border-radius: 12px; border: 1px solid #23304d; margin-top: 15px; }
    h1 { color: #6366f1; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Discipline Hub</h1>
    <p>Student Productivity & Self-Discipline App</p>
    <p>Status Clock: <span id="status-clock">09:41</span></p>
  </div>
</body>
</html>
"""

# Render HTML inside Streamlit component
components.html(html_code, height=800, scrolling=True)
     



























