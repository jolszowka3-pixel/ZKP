import streamlit as st
import streamlit.components.v1 as components

# Konfiguracja strony - 'wide' sprawi, że wykres będzie mógł być szerszy
st.set_page_config(page_title="PROCES ZKP - MATA TERMO", layout="wide")

def render_large_mermaid(code):
    # Zwiększony height do 800px, aby grafika była potężna
    components.html(
        f"""
        <div style="display: flex; justify-content: center;">
            <pre class="mermaid" style="width: 100%;">
                {code}
            </pre>
        </div>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ 
                startOnLoad: true, 
                theme: 'neutral',
                flowchart: {{ useMaxWidth: false, htmlLabels: true }} 
            }});
        </script>
        """,
        height=850,
    )

st.title("📑 Pełny Schemat Technologiczny ZKP")
st.subheader("Linia Malex: Laminacja Ekstruzyjna (Bezpośrednia)")

# Bardzo rozbudowany schemat
big_mermaid = """
graph TD
    subgraph S1 [<b>ETAP 0: WEJŚCIE I KONTROLA</b>]
        A1[Dostawa Granulatu LDPE] --> A2{Kontrola TDS / Czystość}
        B1[Dostawa Alu Zbrojonego] --> B2{Kontrola Zbrojenia / Powierzchni}
    end

    subgraph S2 [<b>ETAP I: BAZA (Wytwarzanie folii 3W)</b>]
        A2 --> C1[Wytłaczarka nr 1 - Stopienie LDPE]
        C1 --> C2[Formowanie bąbla na wale chłodzącym]
        C2 --> C3[Rolka Bazy 3-warstwowej]
        C3 --> QC1{<b>TEST 1:</b><br/>Szczelność bąbla}
    end

    subgraph S3 [<b>ETAP II: PIERWSZA LAMINACJA</b>]
        C3 --> D1[Punkt Styku: Gorące LDPE z Głowicy]
        B2 --> D1
        D1 --> D2[Zespolenie warstwy Alu z folią 3W]
        D2 --> QC2{<b>TEST 2:</b><br/>Adhezja Alu}
    end

    subgraph S4 [<b>ETAP III: DRUGA LAMINACJA (Produkt 5W)</b>]
        D2 --> E1[Punkt Styku: Kolejne gorące LDPE]
        E1 --> E2[Zespolenie z drugą stroną Alu/Folią]
        E2 --> QC3{<b>TEST 3:</b><br/>Grubość całkowita maty}
    end

    subgraph S5 [<b>ETAP IV: WYKOŃCZENIE</b>]
        E2 --> F1[Przekrawacz: Odcinanie brzegów]
        F1 --> F2[Nawijak: Formowanie rolki handlowej]
        F2 --> QC4{<b>TEST 4:</b><br/>Szerokość i Nawój}
    end

    QC4 --> G1[<b>MAGAZYN WYROBU GOTOWEGO</b>]

    %% Kolorystyka
    style S1 fill:#f9f9f9,stroke:#333,stroke-dasharray: 5 5
    style S2 fill:#e3f2fd,stroke:#1565c0
    style S3 fill:#fff3e0,stroke:#ef6c00
    style S4 fill:#fff3e0,stroke:#ef6c00
    style QC1 fill:#ffcdd2,stroke:#c62828
    style QC2 fill:#ffcdd2,stroke:#c62828
    style QC3 fill:#ffcdd2,stroke:#c62828
    style QC4 fill:#ffcdd2,stroke:#c62828
    style G1 fill:#c8e6c9,stroke:#2e7d32,stroke-width:4px
"""

render_large_mermaid(big_mermaid)

st.write("---")
st.markdown("### 📋 Instrukcja Kontroli dla Operatora")
st.info("Pamiętaj: Laminacja odbywa się przez wykorzystanie ciepła własnego polimeru. Brak wałów dociskowych oznacza, że temperatura głowicy musi być monitorowana co 30 minut.")
