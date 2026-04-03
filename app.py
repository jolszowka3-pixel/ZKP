import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony
st.set_page_config(page_title="ZKP TOTAL - LINIA MALEX", layout="wide")

def render_full_mermaid(code):
    # Kluczowe zmiany: securityLevel: 'loose' oraz stopOnLoad: true
    components.html(
        f"""
        <div style="display: flex; justify-content: center; background-color: #ffffff; padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0;">
            <pre class="mermaid">
                {code}
            </pre>
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.9.5/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ 
                startOnLoad: true, 
                theme: 'neutral',
                securityLevel: 'loose',
                flowchart: {{ useMaxWidth: false, htmlLabels: true, curve: 'basis' }} 
            }});
            mermaid.run();
        </script>
        """,
        height=1100,
    )

# --- NAGŁÓWEK ---
st.title("🛡️ Kompletny Obieg Kontroli Produkcji (A-Z)")
st.write("---")

# --- POPRAWIONY SCHEMAT (Z CUDZYSŁOWAMI) ---
# Dodanie cudzysłowów " " wokół tekstów w węzłach eliminuje Syntax Error w v10.9.5
full_zkp_flow = """
graph TD
    subgraph S1 ["ETAP 1: SUROWCE"]
        A["Dostawa Surowców"] --> A1{"Weryfikacja Dokumentów"}
        A1 -->|OK| A2["Pobranie próbki / Archiwum"]
        A2 --> A3["Magazyn Surowców"]
    end

    subgraph S2 ["ETAP 2: PROCES MALEX"]
        A3 --> B1["Wytłaczanie warstwy płynnej"]
        B1 --> B2{{"LAMINACJA BEZPOŚREDNIA"}}
        B2 --> B3["Formowanie 5 warstw"]
        B3 --> QC1{{"CCP 1: TEST ZGRZEWU"}}
    end

    subgraph S3 ["ETAP 3: KRAWĘDZIOWANIE"]
        QC1 --> C1["Przekrawacz: Noże boczne"]
        C1 --> C2{"CCP 2: GEOMETRIA"}
        C2 --> C3["Odsysanie odpadu"]
    end

    subgraph S4 ["ETAP 4: KONFEKCJA"]
        C3 --> D1["Nawijak: Licznik metrów"]
        D1 --> D2["Pakowanie ochronne"]
        D2 --> D3["ETYKIETA CE / Nr Partii"]
    end

    subgraph S5 ["ETAP 5: LOGISTYKA"]
        D3 --> E1["Paletyzacja"]
        E1 --> E2{"CCP 3: SKŁADOWANIE"}
        E2 --> E3["Wydanie / Dokument WZ"]
    end

    style QC1 fill:#ffcdd2,stroke:#c62828
    style C2 fill:#ffcdd2,stroke:#c62828
    style E2 fill:#ffcdd2,stroke:#c62828
    style B2 fill:#fff9c4,stroke:#fbc02d
"""

render_full_mermaid(full_zkp_flow)

# --- SEKCJE SZCZEGÓŁOWE ---
st.header("📋 Instrukcje operacyjne")

c1, c2 = st.columns(2)
with c1:
    st.subheader("✂️ Krawędziowanie")
    st.markdown("""
    - **Szerokość:** Tolerancja +/- 2mm.
    - **Noże:** Sprawdzenie ostrości co 8h pracy.
    - **Odpad:** Segregacja do recyklingu LDPE.
    """)

with c2:
    st.subheader("📦 Magazynowanie")
    st.markdown("""
    - **Palety:** Tylko suche, certyfikowane.
    - **Piętrowanie:** Max 2 poziomy (ochrona bąbla).
    - **Nasłonecznienie:** Zakaz składowania na zewnątrz.
    """)

st.warning("⚠️ Każda partia bez numeru na etykiecie jest uznawana za NIEZGODNĄ z normą budowlaną.")
