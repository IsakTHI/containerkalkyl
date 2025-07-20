# Containerkalkyl  
Detta projekt är endast avsett för rekryterare eller intresserade kontakter.
Utvecklad i Python av **Isak Tranberg-Hansen**

Ett verktyg för att räkna ut containerbehov vid internationella leveranser av bulk- och pallpackat material.

---

## Funktioner

- Stöd för både bulk och packed material  
- Inläsning av materialdata från CSV  
- Automatisk rekommendation av containerstorlek (20ft / 40ft / 40ft HC)  
- Volym- och viktberäkningar med hänsyn till legala begränsningar  
- Terminalbaserat gränssnitt  
- Lämpligt för vidareutveckling t.ex. grafisk visualisering eller API-integration  

---

## Projektstruktur

```bash
Containerkalkyl/
├── material.xlsx               # Lista över material (typ, dimensioner, densitet etc)
├── main.py                    # Huvudfil som körs
├── packed.py                  # Klass för pallar/containerberäkningar
├── bulk.py                    # Klass för bulkberäkningar
└── README.md                  # Dokumentationen (denna fil)
```

---

## Krav

- Python 3.x  
- `pandas`  
- `openpyxl`

Installera:

```bash
pip install -r requirements.txt
```

---

## Så kör du

```bash
python containerkalkyl.py
```

Ange materialkod när du uppmanas. Programmet visar rekommenderad container samt antal som behövs.

---

## Exempeloutput

```
Material: Borsyra (PACKED)
Rekommenderad: 20ft
20ft: 1 behövs (max 7768 kg/container)
40ft: 1 behövs (max 19420 kg/container)
40ft HC: 1 behövs (max 19420 kg/container)
```

---

## Framtida vidareutveckling

- Visualisering av pallplacering  
- GUI med   
- Automatisk prisjämförelse mellan containeralternativ och rederier 
- Export till PDF eller Excel med kalkyl  

---

## Om 

**Isak Tranberg-Hansen**  
Byggt för att effektivisera val av sjöcontainer. All data i material.xlsx är fiktiv, men kan bytas ut mot verkliga siffror för att användas vid val av sjöcontainer i verkliga logistikflöden.

[LinkedIn](https://se.linkedin.com/in/isak-tranberg-hansen-a299452ab)
