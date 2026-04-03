import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony pod wydruk
st.set_page_config(page_title="ARKUSZ ZKP - LINIA MALEX", layout="centered")

# Funkcja do renderowania schematu blokowego
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
        height=450,
    )

# --- NAGŁÓWEK DOKUMENTU ---
st.markdown("<h1 style='text-align: center;'>KARTA ZAKŁADOWEJ KONTROLI PRODUKCJI (ZKP)</h1>", unsafe_allow_status=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>PRODUKCJA MATY TERMOIZOLACYJNEJ (ALU / 3W-LDPE / ALU)</p>", unsafe_allow_html=True)
st.write("---")

# --- SEKCJA 1: SCHEMAT PROCESU ---
st.header("1. Schemat Procesu Technologicznego (Linia Malex)")
mermaid_flow = """
graph TD
    A[<b>WEJŚCIE:</b> Granulat LDPE + Alu Zbrojone] --> B(<b>ETAP I:</b> Wytłaczanie bazy 3W)
    B --> C(<b>ETAP II:</b> Laminacja Alu + Warstwa 2)
    C --> D(<b>ETAP III:</b> Laminacja Alu + Warstwa 3)
    D --> E(<b>WYKOŃCZENIE:</b> Przekrawacz / Noże)
    E --> F[<b>WYJŚCIE:</b> Produkt Gotowy / Magazyn]
    
    style A fill:#f4f4f4,stroke:#333
    style F fill:#e1f5fe,stroke:#01579b
"""
render_mermaid(mermaid_flow)

# --- SEKCJA 2: KONTROLA SUROWCÓW I MASZYNY ---
st.header("2. Parametry Krytyczne (Kontrola A-Z)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Wejście (Surowce)")
    st.markdown("""
    **Granulat LDPE:**
    * Weryfikacja certyfikatu (TDS).
    * Brak zanieczyszczeń wizualnych.
    
    **Aluminium Zbrojone:**
    * Ciągłość siatki zbrojącej.
    * Brak utlenienia (biały nalot).
    * Szerokość rolki wejściowej.
    """)

with col2:
    st.subheader("⚙️ Maszyna Malex")
    st.markdown("""
    **Temperatury:**
    * Głowica (die): **200°C - 210°C**
    * Wały laminujące: **85°C - 105°C**
    
    **Mechanika:**
    * Prędkość: **12-20 m/min**
    * Naciąg (Tension): Stały (hamulce)
    * Docisk wałów: **5 Bar**
    """)

st.write("---")

# --- SEKCJA 3: TABELA KONTROLI JAKOŚCI ---
st.header("3. Punkty Kontrolne i Tolerancje")

st.markdown("""
| Parametr | Metoda Badania | Częstotliwość | Tolerancja / Wymaganie |
| :--- | :--- | :--- | :--- |
| **Jakość Bąbla** | Ściskanie (test szczelności) | Raz na 500m | Brak pękania, bąbel pełny |
| **Adhezja (Klejenie)** | Peel Test (ręczne odrywanie) | Każda zmiana rolki | Rozdarcie folii, nie spoiny |
| **Grubość Maty** | Mikrometr talerzykowy | Start partii / co 1000m | Zgodnie z deklaracją +/- 5% |
| **Szerokość (mm)** | Przymiar liniowy | Ciągła (noże) | +/- 2 mm |
| **Naciąg Nawoju** | Wizualna (brak teleskopu) | Każda rolka | Rolka zwarta, boki równe |
""")

# --- SEKCJA 4: PROCEDURA NIEZGODNOŚCI ---
st.header("4. Postępowanie z Wyrobem Niezgodnym")
st.error("W przypadku wykrycia wady przekraczającej tolerancję:")
st.markdown("""
1.  **Zatrzymaj proces** i skoryguj parametry na panelu Malex.
2.  **Oznacz wadliwy odcinek** czerwoną etykietą lub markerem.
3.  **Odizoluj rolkę** – nie może trafić do Magazynu Wyrobów Gotowych.
4.  **Wpisz zdarzenie** do dobowego raportu produkcji.
""")

st.write("---")

# --- STOPKA DO PODPISU ---
st.header("5. Zatwierdzenie")
c1, c2, c3 = st.columns(3)
with c1:
    st.text_input("Data kontroli:")
with hide_label_c2 := c2: # hack do wyrównania
    st.text_input("Podpis Operatora:")
with c3:
    st.text_input("Podpis Kontroli Jakości:")

st.markdown("<br><p style='text-align: center; color: gray;'>Dokument generowany automatycznie na potrzeby ZKP - 2026</p>", unsafe_allow_html=True)
