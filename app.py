import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony
st.set_page_config(page_title="ARKUSZ ZKP - LINIA MALEX", layout="centered")

# Funkcja do renderowania schematu Mermaid
def render_mermaid(code):
    components.html(
        f"""
        <div style="display: flex; justify-content: center;">
            <pre class="mermaid">
                {code}
            </pre>
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true, theme: 'neutral' }});
        </script>
        """,
        height=400,
    )

# --- NAGŁÓWEK ---
st.markdown("<h1 style='text-align: center;'>KARTA ZAKŁADOWEJ KONTROLI PRODUKCJI (ZKP)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>PRODUKCJA MATY TERMOIZOLACYJNEJ (ALU / 3W-LDPE / ALU)</p>", unsafe_allow_html=True)
st.write("---")

# --- SEKCJA 1: SCHEMAT ---
st.header("1. Schemat Procesu Technologicznego (Linia Malex)")
mermaid_flow = """
graph TD
    A[<b>WEJŚCIE:</b> Granulat + Alu] --> B(<b>KROK I:</b> Produkcja bazy 3W)
    B --> C(<b>KROK II:</b> Laminacja Alu + Warstwa 2)
    C --> D(<b>KROK III:</b> Laminacja Alu + Warstwa 3)
    D --> E(<b>KONFEKCJA:</b> Przekrawacz)
    E --> F[<b>WYJŚCIE:</b> Produkt Gotowy]
    
    style A fill:#f4f4f4,stroke:#333
    style F fill:#e1f5fe,stroke:#01579b
"""
render_mermaid(mermaid_flow)

# --- SEKCJA 2: KONTROLA I PARAMETRY ---
st.header("2. Parametry Krytyczne i Kontrola Surowców")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Wejście (Surowce)")
    st.markdown("""
    * **Granulat LDPE:** Weryfikacja TDS, brak zanieczyszczeń.
    * **Aluminium:** Sprawdzenie zbrojenia, brak utlenienia.
    * **Tuleje:** Kontrola średnicy pod nawijak.
    """)

with col2:
    st.subheader("⚙️ Maszyna Malex")
    st.markdown("""
    * **Głowica:** 200°C - 210°C
    * **Wały laminujące:** 85°C - 105°C
    * **Prędkość:** 12-20 m/min
    * **Docisk:** 5 Bar
    """)

st.write("---")

# --- SEKCJA 3: TABELA JAKOŚCI ---
st.header("3. Punkty Kontrolne i Tolerancje")

st.markdown("""
| Parametr | Metoda Badania | Częstotliwość | Tolerancja |
| :--- | :--- | :--- | :--- |
| **Szczelność Bąbla** | Test ściskania | Raz na 500m | Brak pękania |
| **Adhezja (Alu)** | Peel Test | Każda zmiana rolki | Rozdarcie folii |
| **Grubość Maty** | Mikrometr | Start partii | +/- 5% |
| **Szerokość** | Przymiar | Ciągła | +/- 2 mm |
""")

# --- SEKCJA 4: PROCEDURA NIEZGODNOŚCI ---
st.header("4. Postępowanie z Wyrobem Niezgodnym")
st.error("W przypadku wykrycia wady: Oznacz odcinek czerwoną etykietą, skoryguj parametry i odizoluj rolkę od reszty partii.")

st.write("---")

# --- SEKCJA 5: ZATWIERDZENIE (POPRAWIONA) ---
st.header("5. Zatwierdzenie Kontroli")

c1, c2, c3 = st.columns(3)

with c1:
    st.text_input("Data:", key="data_input")
with c2:
    st.text_input("Podpis Operatora:", key="op_input")
with c3:
    st.text_input("Podpis KJ:", key="kj_input")

st.markdown("<br><p style='text-align: center; color: gray;'>Dokument ZKP - Linia Produkcyjna Malex - 2026</p>", unsafe_allow_html=True)
