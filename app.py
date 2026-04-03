import streamlit as st
import streamlit.components.v1 as components

# Ustawienie szerokiego układu strony (Wide)
st.set_page_config(page_title="ZKP - MATA TERMO", layout="wide")

def render_big_mermaid(code):
    # Kontener HTML z automatycznym skalowaniem i dużą wysokością
    components.html(
        f"""
        <div style="background-color: white; padding: 20px; border-radius: 10px;">
            <pre class="mermaid" style="display: flex; justify-content: center;">
                {code}
            </pre>
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ 
                startOnLoad: true, 
                theme: 'forest',
                flowchart: {{ useMaxWidth: false, htmlLabels: true, curve: 'basis' }} 
            }});
        </script>
        """,
        height=1000, # Zwiększona wysokość dla czytelności
    )

# --- TREŚĆ STRONY ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>SCHEMAT ZKP: PRODUKCJA MATY IZOLACYJNEJ</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Linia Malex - Proces laminacji bezpośredniej (Hot-Melt)</p>", unsafe_allow_html=True)
st.write("---")

# --- WIELKA GRAFIKA ---
# Uproszczona składnia Mermaid (bez zbędnych tagów HTML wewnątrz, by uniknąć błędów)
big_mermaid_code = """
graph TD
    Start([<b>START: Przyjazd surowców</b>]) --> In1[1. Granulat LDPE + Aluminium Zbrojone]
    In1 --> QC_In{<b>KONTROLA WEJŚCIOWA</b><br/>Certyfikaty i czystość}
    
    QC_In -->|OK| Step1[2. EKSTRUDER: Topienie LDPE]
    
    Step1 --> Point1{{<b>PUNKT STYKU I</b>}}
    Point1 --- Roll_Baza[Rolka bazy 3W]
    Point1 --- Roll_Alu1[Aluminium z szpuli]
    
    Point1 --> Step2[3. LAMINACJA: Łączenie w fazie płynnej]
    Step2 --> QC1{<b>TEST ADHEZJI</b><br/>Czy Alu trzyma?}
    
    QC1 -->|OK| Point2{{<b>PUNKT STYKU II</b>}}
    Point2 --- Roll_Alu2[Druga warstwa Alu / Folii]
    Point2 --- Product1[Wstęga z etapu 3]
    
    Point2 --> Step3[4. FORMOWANIE: Produkt 5-warstwowy]
    Step3 --> QC2{<b>TEST JAKOŚCI</b><br/>Grubość i Bąbel}
    
    QC2 -->|OK| Step4[5. PRZEKRAWACZ: Docinanie brzegów]
    Step4 --> Step5[6. NAWIJAK: Formowanie rolek]
    
    Step5 --> QC3{<b>KONTROLA KOŃCOWA</b><br/>Szerokość i Nawój}
    QC3 -->|OK| End([<b>MAGAZYN WYROBU GOTOWEGO</b>])

    %% Stylizacja
    style Start fill:#f4f4f4,stroke:#333
    style End fill:#c8e6c9,stroke:#2e7d32,stroke-width:4px
    style QC_In fill:#fff9c4,stroke:#fbc02d
    style QC1 fill:#fff9c4,stroke:#fbc02d
    style QC2 fill:#fff9c4,stroke:#fbc02d
    style QC3 fill:#fff9c4,stroke:#fbc02d
    style Point1 fill:#ffecb3,stroke:#ffa000,stroke-width:2px
    style Point2 fill:#ffecb3,stroke:#ffa000,stroke-width:2px
"""

render_big_mermaid(big_mermaid_code)

# --- TABELA PARAMETRÓW POD GRAFIKĄ ---
st.write("---")
st.header("📋 Kluczowe parametry do monitorowania")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("🔥 Termika")
    st.write("- **Głowica:** 205°C - 215°C")
    st.write("- **Stop LDPE:** Jednolity, bez grudek")
with col2:
    st.subheader("⚙️ Mechanika")
    st.write("- **Prędkość:** Stała (synchroniczna)")
    st.write("- **Hamulce:** Stały naciąg Alu")
with col3:
    st.subheader("📏 Jakość")
    st.write("- **Adhezja:** Zgrzew nie do rozerwania")
    st.write("- **Bąbel:** Nieprzegrzany (wysokość)")

st.success("Grafika jest zoptymalizowana pod wydruk A4 w orientacji pionowej.")
