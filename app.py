import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony
st.set_page_config(page_title="ZKP TOTAL: Od Surowca do Magazynu", layout="wide")

# Funkcja renderująca schemat
def render_full_mermaid(code):
    components.html(
        f"""
        <div style="display: flex; justify-content: center; background-color: #ffffff; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0;">
            <pre class="mermaid" style="width: 100%;">
                {code}
            </pre>
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ 
                startOnLoad: true, 
                theme: 'neutral',
                flowchart: {{ useMaxWidth: false, htmlLabels: true, curve: 'stepBefore' }} 
            }});
        </script>
        """,
        height=1100,
    )

# --- PANEL BOCZNY ---
st.sidebar.title("🚀 Plan Wdrożenia ZKP")
st.sidebar.markdown("### Etapy Certyfikacji:")
st.sidebar.progress(25) # Na razie 25% - bo mamy plan, ale brak wdrożenia
st.sidebar.write("1. 📝 Dokumentacja (W TOKU)")
st.sidebar.write("2. 🏗️ Przystosowanie Maszyn")
st.sidebar.write("3. 🎓 Szkolenie Załogi")
st.sidebar.write("4. 🔬 Badania Typu (ITT)")

# --- NAGŁÓWEK ---
st.title("🛡️ Kompletny Obieg Kontroli Produkcji (A-Z)")
st.info("Poniższy schemat i wytyczne są fundamentem do uzyskania Certyfikatu Zgodności dla maty termoizolacyjnej.")

# --- SEKCJA 1: GRAFICZNY ARCHI-SCHEMAT ---
st.header("1. Mapa Procesu i Punkty Kontrolne")

full_zkp_flow = """
graph TD
    %% ETAP 1
    subgraph S1 [<b>ETAP 1: SUROWCE</b>]
        A[Dostawa Granulatu i Alu] --> A1{Weryfikacja Dokumentów}
        A1 -->|Zgodne| A2[Pobranie próbki / Archiwum]
        A2 --> A3[Magazyn Surowców - Suchy]
    end

    %% ETAP 2
    subgraph S2 [<b>ETAP 2: PROCES MALEX (SERCE)</b>]
        A3 --> B1[Wytłaczanie warstwy płynnej]
        B1 --> B2{{<b>LAMINACJA BEZPOŚREDNIA</b><br/>Punkt styku gorącego LDPE}}
        B2 --> B3[Formowanie 5 warstw]
        B3 --> QC1{<b>CCP 1: TERMOPLIP</b><br/>Test zgrzewu i bąbla}
    end

    %% ETAP 3
    subgraph S3 [<b>ETAP 3: KRAWĘDZIOWANIE</b>]
        QC1 --> C1[Przekrawacz: Noże boczne]
        C1 --> C2{<b>CCP 2: GEOMETRIA</b><br/>Szerokość i czystość cięcia}
        C2 --> C3[System odsysania odpadu/ścinek]
    end

    %% ETAP 4
    subgraph S4 [<b>ETAP 4: KONFEKCJA I FINISZ</b>]
        C3 --> D1[Nawijak: Licznik metrów]
        D1 --> D2[Pakowanie w folię ochronną]
        D2 --> D3[<b>ETYKIETA CE:</b> Nr Partii / Data]
    end

    %% ETAP 5
    subgraph S5 [<b>ETAP 5: MAGAZYN I LOGISTYKA</b>]
        D3 --> E1[Paletyzacja: Brak kontaktu z podłożem]
        E1 --> E2{<b>CCP 3: SKŁADOWANIE</b><br/>Ochrona przed UV i naciskiem}
        E2 --> E3[Wydanie towaru / Dokumentacja WZ]
    end

    style QC1 fill:#ffcdd2,stroke:#c62828
    style QC2 fill:#ffcdd2,stroke:#c62828
    style E2 fill:#ffcdd2,stroke:#c62828
    style B2 fill:#fff9c4,stroke:#fbc02d
"""
render_full_mermaid(full_zkp_flow)

st.write("---")

# --- SEKCJA 2: SZCZEGÓŁOWY ROZBITY OPIS ---
st.header("2. Szczegółowe wymagania dla każdego kroku")

tab1, tab2, tab3, tab4 = st.tabs(["🏗️ Produkcja (Malex)", "✂️ Krawędziowanie", "📦 Pakowanie & CE", "🏬 Magazynowanie"])

with tab1:
    st.markdown("#### Krytyczne parametry na maszynie:")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.write("**Ekstruzja:**")
        st.write("- Temperatura głowicy: **210°C ± 5°C** (Klucz do adhezji)")
        st.write("- Chłodzenie bębna: **16°C - 20°C** (Klucz do formy bąbla)")
    with col_p2:
        st.write("**Laminacja:**")
        st.write("- Test 'na gorąco': Co 30 min sprawdzenie, czy aluminium nie 'pływa'")
        st.write("- Wysokość bąbla: Sprawdzenie, czy płynne LDPE nie stopiło bazy 3W")

with tab2:
    st.markdown("#### Precyzja krawędziowania:")
    st.markdown("""
    * **Ustawienie noży:** Szerokość deklarowana (np. 1200mm) musi być zachowana z dokładnością **+/- 2mm**.
    * **Czystość cięcia:** Aluminium nie może być poszarpane (ryzyko korozji krawędziowej i skaleczeń).
    * **Zarządzanie odpadem:** Ścinki brzegowe muszą być natychmiast usuwane i segregowane do recyklingu (nie mogą zanieczyszczać gotowego produktu).
    """)

with tab3:
    st.markdown("#### Identyfikowalność (Traceability):")
    st.markdown("""
    * **Licznik metrów:** Każda rolka musi mieć potwierdzoną długość (np. 50mb).
    * **Etykieta CE/B:** Musi zawierać: 
        1. Nazwę produktu.
        2. Deklarowany opór cieplny (R).
        3. **UNIKALNY NUMER PARTII** (Data + Numer Maszyny + Numer Kolejny).
    * *Bez numeru partii nie ma mowy o uznaniu normy budowlanej!*
    """)

with tab4:
    st.markdown("#### Zasady magazynowania (Często pomijane!):")
    st.error("Złe magazynowanie niszczy parametry izolacyjne produktu.")
    st.markdown("""
    1.  **Izolacja od podłoża:** Rolki/palety muszą stać na suchych paletach (brak podciągania wilgoci).
    2.  **Ochrona UV:** LDPE degraduje pod wpływem słońca. Magazyn musi być zadaszony.
    3.  **Zakaz nadmiernego piętrowania:** Zbyt duży nacisk na dolne warstwy palet powoduje trwałe zgniatanie bąbelków (utrata izolacyjności).
    4.  **Zasada FIFO:** 'First In, First Out' – najstarsza partia wyjeżdża pierwsza.
    """)

st.write("---")

# --- SEKCJA 3: PODSUMOWANIE DLA ZARZĄDU ---
st.header("3. Co musimy wdrożyć 'na wczoraj'?")
st.warning("Poniższa lista to minimalne inwestycje wymagane przez audytora norm budowlanych.")

checklist_col1, checklist_col2 = st.columns(2)
with checklist_col1:
    st.write("✅ **Sprzęt pomiarowy:**")
    st.write("- Skalibrowany mikrometr talerzykowy.")
    st.write("- Pirometr (do weryfikacji temp. stopu).")
    st.write("- Legalizowana miara stalowa (2m+).")
with checklist_col2:
    st.write("✅ **Dokumentacja:**")
    st.write("- Formularz 'Raport Dobowy Operatora'.")
    st.write("- Rejestr wyrobów niezgodnych.")
    st.write("- Procedura reklamacyjna.")

if st.button("Wygeneruj raport końcowy do druku"):
    st.success("Raport ZKP przygotowany. Użyj Ctrl+P, aby zapisać jako PDF.")

st.markdown("<br><p style='text-align: center; color: gray;'>System Zarządzania Jakością ZKP | Wersja 2.0 - Pełna Specyfikacja</p>", unsafe_allow_html=True)
