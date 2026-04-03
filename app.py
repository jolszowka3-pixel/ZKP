import streamlit as st
import streamlit.components.v1 as components

# Tryb Wide, żeby wszystko było czytelne
st.set_page_config(page_title="ZKP TOTAL - PEŁNY PROCES", layout="wide")

def render_bulletproof_mermaid(code):
    # Uproszczony i bardziej stabilny skrypt ładowania Mermaid
    html_code = f"""
    <div class="mermaid" style="display: flex; justify-content: center;">
        {code}
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ 
            startOnLoad: true, 
            theme: 'neutral',
            flowchart: {{ useMaxWidth: false, htmlLabels: true }} 
        }});
    </script>
    """
    components.html(html_code, height=1000)

# --- NAGŁÓWEK ---
st.markdown("<h1 style='text-align: center; color: #b22222;'>STRATEGIA ZKP: OD SUROWCA PO MAGAZYN WYDAŃ</h1>", unsafe_allow_html=True)
st.write("---")

# --- SEKCJA 1: KOMPLETNY SCHEMAT (NAJBARDZIEJ SZCZEGÓŁOWY) ---
# Uwaga: Używam najprostszej składni Mermaid, by uniknąć błędów wersji 10.9
mermaid_code = """
graph TD
    subgraph SUROWCE ["1. PRZYJĘCIE I KONTROLA WEJŚCIOWA"]
        A1["Dostawa Granulatu LDPE"] --> A2["Kontrola MFR i czystości"]
        B1["Dostawa Aluminium zbrojonego"] --> B2["Kontrola grubości i siatki"]
        C1["Dostawa Tulei / Folii opak."] --> C2["Weryfikacja wymiarów"]
        A2 & B2 & C2 --> D["Zwolnienie do produkcji (Karta Surowca)"]
    end

    subgraph PROCES ["2. PRODUKCJA MALEX (LAMINACJA BEZPOŚREDNIA)"]
        D --> E["Wytłaczanie bazy 3W - Formowanie bąbla"]
        E --> F["Laminacja I: Gorące LDPE + Alu strona A"]
        F --> G["Laminacja II: Gorące LDPE + Alu strona B"]
        G --> QC1{{"CCP 1: TEST ADHEZJI (ZGRZEW)"}}
    end

    subgraph WYKONCZENIE ["3. KRAWĘDZIOWANIE I CIĘCIE"]
        QC1 --> H["Przekrawacz: Precyzyjne odcinanie brzegów"]
        H --> I["System odsysania i belowania odpadu"]
        I --> QC2{{"CCP 2: GEOMETRIA (Szerokość +/- 2mm)"}}
    end

    subgraph KONFEKCJA ["4. PAKOWANIE I ZNAKOWANIE"]
        QC2 --> J["Nawijanie: Kontrola licznika metrów"]
        J --> K["Pakowanie w rękaw ochronny / Foliowanie"]
        K --> L["Znakowanie: ETYKIETA CE + NR PARTII"]
    end

    subgraph LOGISTYKA ["5. MAGAZYNOWANIE I WYDANIE"]
        L --> M["Paletyzacja (Zabezpieczenie narożników)"]
        M --> N["Składowanie (Strefa sucha, ochrona UV)"]
        N --> QC3{{"CCP 3: KONTROLA PRZEDWYDANIOWA"}}
        QC3 --> O["Załadunek i wydanie Dokumentacji WZ"]
    end

    style QC1 fill:#ff9999,stroke:#333
    style QC2 fill:#ff9999,stroke:#333
    style QC3 fill:#ff9999,stroke:#333
    style PROCES fill:#fff4dd,stroke:#d4a017
"""
render_bulletproof_mermaid(mermaid_code)

st.write("---")

# --- SEKCJA 2: SZCZEGÓŁOWY ROZPIS KONTROLI ---
st.header("2. Szczegółowe instrukcje stanowiskowe")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("✂️ Etap Krawędziowania")
        st.markdown("""
        **Punkty krytyczne:**
        1. **Ustawienie noży:** Sprawdzenie wymiaru po każdym nowym nawoju (tolerancja $ \pm 2mm $).
        2. **Stan ostrzy:** Jeśli krawędź aluminium jest poszarpana - natychmiastowa wymiana/ostrzenie noży.
        3. **Gospodarka odpadem:** Ścinki boczne muszą być separowane od razu (brak zanieczyszczeń na rolce gotowej).
        """)

    with st.container(border=True):
        st.subheader("📦 Etap Pakowania i Etykiety")
        st.markdown("""
        **Wymogi CE (Normy Budowlane):**
        1. **Numer Partii:** Musi pozwalać na identyfikację: dnia, godziny i operatora maszyny.
        2. **Parametr R (Opór):** Musi być zgodny z Deklaracją Właściwości Użytkowych (DoP).
        3. **Zabezpieczenie:** Każda rolka szczelnie zamknięta (ochrona aluminium przed kurzem i tłuszczem).
        """)

with col2:
    with st.container(border=True):
        st.subheader("🏬 Magazynowanie (Zasady Krytyczne)")
        st.markdown("""
        **Ochrona produktu:**
        1. **UV:** Zakaz składowania w miejscach z dostępem światła słonecznego (degradacja LDPE).
        2. **Nacisk (Piętrowanie):** Maksymalnie 2 palety w pionie. Przekroczenie nacisku trwale zgniata pęcherzyki powietrza – **utrata parametrów izolacyjnych!**
        3. **Wilgoć:** Magazyn musi zapobiegać korozji aluminium (powstawaniu białego nalotu).
        4. **Separacja:** Wyroby niezgodne (II gatunek) muszą być fizycznie oddzielone od wyrobów CE.
        """)

    with st.container(border=True):
        st.subheader("🔬 Laboratorium / Archiwum")
        st.markdown("""
        **Zadania KJ:**
        - Pobieranie próbki 1m z każdej partii (przechowywanie 10 lat).
        - Weryfikacja gramatury i grubości mikrometrem talerzykowym.
        - Archiwizacja wyników testu adhezji (rozdarcie ręczne).
        """)

# --- SEKCJA 3: PODSUMOWANIE DLA ZARZĄDU ---
st.write("---")
st.header("3. Co zyskujemy dzięki temu systemowi?")
c1, c2, c3 = st.columns(3)
c1.metric("Bezpieczeństwo", "Legalny znak CE/B", "Brak kar")
c2.metric("Oszczędność", "Mniej odpadu", "Optymalizacja")
c3.metric("Jakość", "0 reklamacji", "Zadowolenie")

st.markdown("<p style='text-align: center; color: #888;'>Dokumentacja wdrożeniowa ZKP - v3.0 stable</p>", unsafe_allow_html=True)
