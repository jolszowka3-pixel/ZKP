import streamlit as st
import streamlit.components.v1 as components

# Ustawienia strony - tryb szeroki dla lepszej prezentacji
st.set_page_config(page_title="WDROŻENIE ZKP - LINIA MALEX", layout="wide")

# Funkcja renderująca powiększony schemat Mermaid
def render_big_mermaid(code):
    components.html(
        f"""
        <div style="display: flex; justify-content: center; background-color: white; padding: 20px; border-radius: 10px; zoom: 1.1;">
            <pre class="mermaid" style="width: 100%;">
                {code}
            </pre>
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ 
                startOnLoad: true, 
                theme: 'neutral',
                flowchart: {{ useMaxWidth: false, htmlLabels: true, curve: 'linear' }} 
            }});
        </script>
        """,
        height=900,
    )

# --- PANEL BOCZNY (Status Wdrożenia) ---
st.sidebar.header("📊 Status Wdrożenia ZKP")
st.sidebar.info("Ten panel pokazuje szefowi, ile pracy pozostało do uzyskania certyfikacji.")
st.sidebar.checkbox("Instrukcje dla operatorów", value=False)
st.sidebar.checkbox("Karty kontroli (papierowe/cyfrowe)", value=False)
st.sidebar.checkbox("Kalibracja czujników temperatury", value=False)
st.sidebar.checkbox("Archiwum próbek", value=False)

# --- NAGŁÓWEK ---
st.title("🛡️ Strategia Wdrożenia Zakładowej Kontroli Produkcji")
st.subheader("Cel: Zgodność z normami budowlanymi dla mat termoizolacyjnych")
st.markdown("""
Ta aplikacja przedstawia kompletny obieg kontroli od surowca po wysyłkę. 
Wdrożenie tych punktów jest niezbędne do legalnego znakowania produktu znakiem **CE** lub **B**.
""")

st.write("---")

# --- SEKCJA 1: SCHEMAT A-Z ---
st.header("1. Pełny Cykl Życia Produktu (Schemat A-Z)")

zkp_flow = """
graph TD
    %% Surowce
    A[<b>MAGAZYN WEJŚCIOWY</b><br/>Granulat + Aluminium] -->|Kontrola certyfikatów| B(<b>PRZYGOTOWANIE PRODUKCJI</b>)
    
    %% Proces Malex
    B --> C{{<b>EKSTRUZJA LDPE</b><br/>Topienie granulatu 210°C}}
    C --> D[<b>LAMINACJA I</b><br/>Łączenie bazy 3W z Alu]
    D --> E[<b>LAMINACJA II</b><br/>Doklejanie Alu/Foli do wstęgi]
    
    %% Punkty Kontrolne
    E --> QC1{<b>CCP 1: TEST ADHEZJI</b><br/>Czy zgrzew jest trwały?}
    QC1 -->|OK| QC2{<b>CCP 2: TEST BĄBLA</b><br/>Szczelność i wysokość}
    
    %% Wykończenie
    QC2 -->|OK| F[<b>PRZEKRAWACZ</b><br/>Krawędziowanie i wymiarowanie]
    F --> G[<b>KONFEKCJA</b><br/>Nawijanie i etykietowanie CE]
    
    %% Magazyn
    G --> H[<b>MAGAZYN WYROBU GOTOWEGO</b>]
    H -->|Traceability| I[<b>WYSYŁKA</b>]

    %% Style
    style QC1 fill:#ffcdd2,stroke:#c62828,stroke-width:2px
    style QC2 fill:#ffcdd2,stroke:#c62828,stroke-width:2px
    style C fill:#fff9c4,stroke:#fbc02d
    style H fill:#c8e6c9,stroke:#2e7d32
"""
render_big_mermaid(zkp_flow)

st.write("---")

# --- SEKCJA 2: CO MUSIMY WDROŻYĆ (DLA SZEFA) ---
st.header("2. Kluczowe obszary do przystosowania")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🛠️ Maszyny (Malex)")
    st.markdown("""
    **Co musimy dodać/sprawdzić:**
    1. **Precyzyjne czujniki temp.:** Musimy mieć pewność, że 210°C na głowicy to faktycznie 210°C.
    2. **Licznik metrów:** Kalibracja, by klient nie dostał mniej towaru.
    3. **Noże przekrawacza:** Harmonogram ostrzenia (czysta krawędź aluminium).
    """)

with col2:
    st.markdown("### 👥 Pracownicy")
    st.markdown("""
    **Nowe obowiązki:**
    1. **Raport dobowy:** Co 2h operator wpisuje parametry maszyny do tabeli.
    2. **Testy niszczące:** Przy każdej rolce operator musi spróbować rozerwać laminat (Peel Test).
    3. **Oznakowanie:** Odpowiedzialność za naklejenie etykiety z nr partii.
    """)

with col3:
    st.markdown("### 📦 Logistyka")
    st.markdown("""
    **Zmiany w magazynie:**
    1. **Kwarantanna:** Wydzielone miejsce na towar z wadą (nie może wyjechać!).
    2. **Paletyzacja:** Maty nie mogą leżeć na ziemi (korozja alu).
    3. **Archiwum:** Pudełko na próbki 30x30cm z każdej partii (wymóg normy).
    """)

st.write("---")

# --- SEKCJA 3: TABELA KONTROLI (CHECKLISTA) ---
st.header("3. Standard Kontroli Jakości (Do wdrożenia od zaraz)")

data = {
    "Krok": ["Przyjęcie LDPE", "Ekstruzja", "Laminacja", "Krawędziowanie", "Etykietowanie"],
    "Co sprawdzamy?": ["Certyfikat dostawcy (MFR)", "Temperatura stopu (210°C)", "Siła zgrzewu (Adhezja)", "Szerokość (np. 1200mm)", "Znak CE + Nr Partii"],
    "Tolerancja": ["Zgodna z zamówieniem", "+/- 5°C", "Brak rozwarstwienia", "+/- 2mm", "100% poprawności"]
}
st.table(data)

st.warning("💡 **Ważne dla Szefa:** Bez dokumentacji tych kroków, żadne badania w laboratorium zewnętrznym nie dadzą nam prawa do wystawienia Deklaracji Właściwości Użytkowych (DoP).")

# --- STOPKA ---
st.markdown("<p style='text-align: center; color: #7f8c8d;'>Opracowano na potrzeby wdrożenia normy budowlanej w zakładzie produkcji mat termoizolacyjnych. v1.5</p>", unsafe_allow_html=True)
