import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony
st.set_page_config(page_title="ARKUSZ ZKP - LINIA MALEX (Laminacja Bezpośrednia)", layout="centered")

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
        height=450,
    )

# --- NAGŁÓWEK ---
st.markdown("<h1 style='text-align: center;'>KARTA ZAKŁADOWEJ KONTROLI PRODUKCJI (ZKP)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>PRODUKCJA MATY: LAMINACJA DO WARSTWY WYPŁYWAJĄCEJ (METODA HOT-MELT)</p>", unsafe_allow_html=True)
st.write("---")

# --- SEKCJA 1: SCHEMAT ---
st.header("1. Schemat Procesu: Łączenie w fazie płynnej")
mermaid_flow = """
graph TD
    A[<b>EKSTRUDER:</b> Wypływ gorącej warstwy LDPE] --> B{<b>PUNKT STYKU</b>}
    C[<b>PODAJNIK:</b> Folia Alu zbrojone] --> B
    D[<b>ODWIJAK:</b> Gotowa rolka bąbelkowa] --> B
    B --> E(Zespolenie termiczne na bębnie formującym)
    E --> F(Chłodzenie i stabilizacja)
    F --> G[Przekrawacz i Nawijak]
    
    style B fill:#ffeb3b,stroke:#fbc02d,stroke-width:2px
    style A fill:#f4f4f4,stroke:#333
"""
render_mermaid(mermaid_flow)

# --- SEKCJA 2: KONTROLA PARAMETRÓW ---
st.header("2. Kluczowe Parametry Procesu (CCP)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 Termika (Ekstruzja)")
    st.markdown("""
    **Temperatura stopu (Melt Temp):**
    * Musi być wystarczająca do aktywacji termicznej Alu.
    * Zakres: **205°C - 215°C** (zależnie od gęstości LDPE).
    
    **Chłodzenie bębna:**
    * Kluczowe dla "zamrożenia" spoiny.
    * Temp. wody: **15°C - 18°C**.
    """)

with col2:
    st.subheader("⚙️ Synchronizacja")
    st.markdown("""
    **Prędkość liniowa:**
    * Synchronizacja odwijaka z prędkością wypływu.
    * Brak naciągu "ciągnącego" – ryzyko zwężenia maty.
    
    **Prowadzenie Alu:**
    * Musi wchodzić idealnie w lustro płynnego LDPE.
    """)

st.write("---")

# --- SEKCJA 3: TABELA JAKOŚCI ---
st.header("3. Kontrola Jakości (Standard Budowlany)")

st.info("💡 Ponieważ doklejasz do gorącej warstwy, największym ryzykiem jest deformacja termiczna bąbli.")

st.markdown("""
| Parametr | Metoda Badania | Częstotliwość | Cel |
| :--- | :--- | :--- | :--- |
| **Siła Zgrzewu** | Próba rozdarcia | Co każdą rolkę | Rozdarcie materiału, nie odklejenie Alu |
| **Integracja Bąbla** | Pomiar grubości | Co 500m | Brak "klapniętych" bąbli (przegrzanie) |
| **Ciągłość Alu** | Wizualna | Ciągła | Brak marszczeń i pęcherzy powietrza pod Alu |
| **Szerokość** | Przymiar | Co rolkę | Zgodność z zamówieniem +/- 2mm |
""")

# --- SEKCJA 4: PROCEDURA ---
st.header("4. Postępowanie z Wyrobem Niezgodnym")
st.warning("⚠️ Jeżeli Alu odchodzi od LDPE 'na sucho' – podnieś temperaturę na głowicy lub zwolnij prędkość linii!")

# --- SEKCJA 5: ZATWIERDZENIE ---
st.header("5. Zatwierdzenie Partii")
c1, c2, c3 = st.columns(3)
with c1:
    st.text_input("Data:", key="d1")
with c2:
    st.text_input("Operator Malex:", key="o1")
with c3:
    st.text_input("Podpis KJ:", key="p1")

st.markdown("<br><p style='text-align: center; color: gray;'>System ZKP - Dokumentacja Cyfrowa v1.2</p>", unsafe_allow_html=True)
