import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony na tryb szeroki (Wide) dla czytelności tabel
st.set_page_config(page_title="SYSTEM ZKP TOTAL - LINIA MALEX", layout="wide")

def render_pro_mermaid(code):
    components.html(
        f"""
        <div style="display: flex; justify-content: center; background-color: #ffffff; padding: 25px; border-radius: 15px; border: 2px solid #1E3A8A;">
            <pre class="mermaid" style="width: 100%;">
                {code}
            </pre>
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.9.5/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ 
                startOnLoad: true, 
                theme: 'neutral',
                securityLevel: 'loose',
                flowchart: {{ useMaxWidth: false, htmlLabels: true, curve: 'stepBefore' }} 
            }});
            mermaid.run();
        </script>
        """,
        height=1200,
    )

# --- NAGŁÓWEK ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>KOMPLEKSOWY SYSTEM ZKP: PRODUKCJA MAT TERMOIZOLACYJNYCH</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em;'>Dokumentacja techniczna wdrożenia normy budowlanej (System 3/4)</p>", unsafe_allow_html=True)
st.write("---")

# --- SEKCJA 1: WIELKI SCHEMAT LOGICZNY ---
st.header("1. Mapa Procesu Operacyjnego A-Z")

# Uproszczona składnia Mermaid (z cudzysłowami) dla stabilności wersji 10.9.5
full_flow = """
graph TD
    subgraph S1 ["I. KONTROLA WEJŚCIOWA (SUROWCE)"]
        A["Dostawa Granulatu LDPE"] --> A1{"Badanie MFR / Wilgotność"}
        B["Dostawa Alu Zbrojonego"] --> B1{"Badanie grubości / Czystości"}
        C["Dostawa Tulei Tekturowych"] --> C1{"Kontrola średnicy i wagi"}
        A1 & B1 & C1 -->|"Zatwierdzenie"| D["Zwolnienie surowców do produkcji"]
    end

    subgraph S2 ["II. EKSTRUZJA I LAMINACJA (MALEX)"]
        D --> E["Wytłaczanie bazy 3W (Bąbel)"]
        E --> F{{"PUNKT STYKU 1: Hot-Melt Alu"}}
        F --> G["Formowanie wstęgi 5-warstwowej"]
        G --> QC1{{"CCP 1: Test adhezji i bąbla"}}
    end

    subgraph S3 ["III. WYKOŃCZENIE (KRAWĘDZIOWANIE)"]
        QC1 -->|"OK"| H["PRZEKRAWACZ: Noże boczne"]
        H --> H1{"CCP 2: Szerokość wstęgi"}
        H1 --> H2["Odprowadzenie odpadu LDPE/Alu"]
    end

    subgraph S4 ["IV. KONFEKCJA I ZNAKOWANIE"]
        H2 --> I["Nawijanie na tuleję (Licznik m)"]
        I --> J["Pakowanie w rękaw foliowy"]
        J --> K["Znakowanie CE: Etykieta z Nr Partii"]
    end

    subgraph S5 ["V. MAGAZYNOWANIE I LOGISTYKA"]
        K --> L["Paletyzacja (Max 2 poziomy)"]
        L --> M{"CCP 3: Kontrola składowania"}
        M -->|"Wydanie"| N["Dokumentacja WZ / Certyfikat ITT"]
    end

    style QC1 fill:#ffcdd2,stroke:#c62828,stroke-width:2px
    style H1 fill:#ffcdd2,stroke:#c62828,stroke-width:2px
    style M fill:#ffcdd2,stroke:#c62828,stroke-width:2px
    style F fill:#fff9c4,stroke:#fbc02d,stroke-width:2px
"""
render_pro_mermaid(full_flow)

st.write("---")

# --- SEKCJA 2: SZCZEGÓŁOWE PROCEDURY ---
st.header("2. Szczegółowe Wytyczne Techniczne")

col1, col2 = st.columns(2)

with col1:
    with st.expander("📂 KROK 1: Przyjęcie Surowców", expanded=True):
        st.markdown("""
        * **Granulat:** Każdy 'Big-Bag' musi mieć numer partii zgodny z atestem producenta.
        * **Aluminium:** Sprawdzenie siatki zbrojącej – brak przerw w splotach.
        * **Kwarantanna:** Surowiec bez certyfikatu trafia do strefy czerwonej.
        """)
        
    with st.expander("🔥 KROK 2: Proces Malex", expanded=True):
        st.markdown("""
        * **Temperatury głowicy:** 205°C - 215°C (stały monitoring co 30 min).
        * **Test Adhezji:** Operator próbuje rozdzielić warstwę Alu od bąbla co 500m bieżących. 
        * **Woda chłodząca:** Stała temp. 16°C – zapobieganie 'szokowi termicznemu' aluminium.
        """)

with col2:
    with st.expander("✂️ KROK 3: Krawędziowanie i Odpad", expanded=True):
        st.markdown("""
        * **Precyzja noży:** Tolerancja szerokości produktu końcowego to **+/- 2mm**. 
        * **Stan noży:** Kontrola szczerbień po każdej zmianie.
        * **Zarządzanie odpadem:** Ścinki muszą być nawijane na osobną szpulę lub odsysane – nie mogą zanieczyszczać pola pracy.
        """)
        
    with st.expander("📦 KROK 4: Magazynowanie (Kluczowe dla Normy)", expanded=True):
        st.markdown("""
        * **Ochrona UV:** Zakaz składowania przy otwartych dokach (słońce niszczy strukturę LDPE).
        * **Nacisk:** Maksymalnie **2 palety w pionie**. Większy nacisk trwale zgniata pęcherzyki powietrza, obniżając izolacyjność (reklamacja gwarantowana).
        * **Wilgoć:** Magazyn musi być ogrzewany/suchy, by uniknąć korozji aluminium.
        """)

st.write("---")

# --- SEKCJA 3: TABELA ODPOWIEDZIALNOŚCI ---
st.header("3. Podział Odpowiedzialności (Kadry)")

st.table([
    {"Rola": "Magazynier", "Zadanie": "Kontrola certyfikatów wejściowych i stanu palet gotowych", "Częstotliwość": "Przy każdej dostawie/wydaniu"},
    {"Rola": "Operator Malex", "Zadanie": "Monitoring temperatur, test adhezji i zmiana noży", "Częstotliwość": "Ciągła (co 30 min zapis)"},
    {"Rola": "Kontroler Jakości", "Zadanie": "Weryfikacja parametrów z całego dnia i archiwizacja próbek", "Częstotliwość": "Raz na dobę"},
    {"Rola": "Kierownik Produkcji", "Zadanie": "Zwalnianie partii do obrotu (Znakowanie CE)", "Częstotliwość": "Przed wysyłką"}
])

# --- SEKCJA 4: NARZĘDZIA POMIAROWE ---
st.header("4. Wymagane Wyposażenie Pomiarowe")
st.warning("Bez tych narzędzi audytor nie zatwierdzi systemu ZKP!")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Mikrometr Talerzykowy", "Dokładność 0.01mm", "Pomiar grubości")
c2.metric("Pirometr Laserowy", "Kalibracja roczna", "Pomiar temp. stopu")
c3.metric("Waga Precyzyjna", "Zatwierdzona", "Gramatura produktu")
c4.metric("Przymiar Stalowy", "Klasa II", "Szerokość krawędzi")

# --- STOPKA ---
st.write("---")
if st.button("Drukuj Pełny Raport Wdrożeniowy (PDF)"):
    st.info("Użyj skrótu klawiszowego Ctrl+P, aby zapisać widok jako PDF.")

st.markdown("<p style='text-align: center; color: gray;'>Opracował: System Wspomagania Jakości ZKP | 2026-04-03</p>", unsafe_allow_html=True)
