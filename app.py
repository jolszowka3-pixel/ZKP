import streamlit as st
import streamlit.components.v1 as components

# Ustawienia strony
st.set_page_config(page_title="ZKP - Mata Termoizolacyjna", layout="wide")

def render_mermaid(code):
    components.html(
        f"""
        <pre class="mermaid">
            {code}
        </pre>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """,
        height=600,
    )

# Tytuł i nagłówek
st.title("🛡️ System Zakładowej Kontroli Produkcji (ZKP)")
st.subheader("Produkcja Maty Termoizolacyjnej (Alu + 3xLDPE) - Linia Malex")
st.markdown("---")

# Sidebar - nawigacja
st.sidebar.header("Menu Nawigacji")
section = st.sidebar.radio("Przejdź do sekcji:", 
    ["Schemat Procesu", "Kontrola Surowców", "Parametry Maszyny Malex", "Kontrola Jakości Bąbla", "Pakowanie i Magazyn"])

if section == "Schemat Procesu":
    st.header("1. Graficzny Schemat Produkcji i Kontroli")
    mermaid_code = """
    graph TD
        A[Dostawa: Granulat + Alu] --> B{Kontrola Wejściowa}
        B --> C[Produkcja Folii Bazy 3W]
        C --> D{Test Bąbla i Grubości}
        D --> E[Laminacja I: Alu + Nowe 3W + Baza]
        E --> F{Test Adhezji I}
        F --> G[Laminacja II: Alu + Nowe 3W + Półprodukt]
        G --> H{Kontrola Końcowa 5-warstw}
        H --> I[Przekrawacz: Krawędziowanie]
        I --> J[Pakowanie i Etykieta CE]
        
        style B fill:#f96,stroke:#333
        style D fill:#f96,stroke:#333
        style F fill:#f96,stroke:#333
        style H fill:#f96,stroke:#333
    """
    render_mermaid(mermaid_code)
    st.info("💡 Pomarańczowe romby oznaczają Krytyczne Punkty Kontrolne (CCP).")

elif section == "Kontrola Surowców":
    st.header("2. Kontrola Wejściowa (A-Z)")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Granulat LDPE**")
        st.table({
            "Parametr": ["MFR (Wskaźnik płynięcia)", "Gęstość", "Czystość"],
            "Wymaganie": ["Zgodnie z TDS", "0.918 - 0.924 g/cm3", "Brak wtrąceń obcych"]
        })
        
    with col2:
        st.write("**Aluminium Zbrojone**")
        st.table({
            "Parametr": ["Grubość folii", "Gramatura siatki", "Powierzchnia"],
            "Wymaganie": ["min. 7-12 mikronów", "Zgodnie z zamówieniem", "Sucha, bez oleju"]
        })

elif section == "Parametry Maszyny Malex":
    st.header("3. Kluczowe Ustawienia Procesowe (Karta Operatora)")
    
    st.warning("⚠️ Przekroczenie tych parametrów skutkuje odrzutem produkcyjnym!")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Temp. Głowicy (LDPE)", "205°C", "± 5°C")
        st.write("- **Sekcja zasilania:** 165°C")
        st.write("- **Sekcja sprężania:** 190°C")
    
    with col_b:
        st.metric("Temp. Wałów Laminujących", "95°C", "Zależna od prędkości")
        st.write("- **Docisk:** 4-6 Bar")
        st.write("- **Chłodzenie wałów:** 18°C")

    with col_c:
        st.metric("Prędkość Linii", "15 m/min", "Max 25 m/min")
        st.write("- **Naciąg Alu:** Napięcie stałe (hamulec proszkowy)")
        st.write("- **Naciąg nawoju:** Malejący (Taper)")

elif section == "Kontrola Jakości Bąbla":
    st.header("4. Testy Fizyczne i Wytrzymałościowe")
    
    st.markdown("""
    | Nazwa Testu | Częstotliwość | Metoda | Norma / Cel |
    | :--- | :--- | :--- | :--- |
    | **Szczelność Bąbla** | Co 500m | Ściskanie ręczne / obciążnik | Brak pęknięć sekwencyjnych |
    | **Test Adhezji (Peel)** | Raz na zmianę | Odrywanie ręczne Alu | Zerwanie w LDPE (nie na spoinie) |
    | **Grubość Całkowita** | Co rolkę | Mikrometr talerzykowy | Zgodność z deklaracją (np. 8mm) |
    | **Waga mb** | Raz na dobę | Waga elektroniczna | Stabilność dozowania granulatu |
    """)
    
    if st.button("Zgłoś Niezgodność (Raport NC)"):
        st.error("Wdrożono procedurę wyrobu niezgodnego. Oznacz rolkę CZERWONĄ etykietą.")

elif section == "Pakowanie i Magazyn":
    st.header("5. Finalizacja i Identyfikowalność")
    st.success("Produkt gotowy do wprowadzenia do obrotu po sprawdzeniu etykiety.")
    
    st.checkbox("Sprawdzono szerokość po krawędziowaniu (Tolerancja +/- 2mm)")
    st.checkbox("Etykieta zawiera Numer Partii (Data + Nr Maszyny)")
    st.checkbox("Znakowanie CE widoczne na opakowaniu zbiorczym")
    
    st.text_area("Uwagi do partii:", placeholder="Np. wymiana noży na przekrawaczu w połowie zlecenia...")

# Stopka
st.markdown("---")
st.caption("System ZKP v1.0 | Wygenerowano dla: Producent Mat Termoizolacyjnych")
