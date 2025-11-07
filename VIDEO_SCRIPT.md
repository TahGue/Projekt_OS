# Video Script - Olympic Games Data Analysis
## Individual Video (Task 4) - 5-10 minutes

---

## 🎬 Introduction (1 minute)

**[Screen: Show GitHub repository]**

"Hej, jag heter [Ditt namn] och idag ska jag presentera min lösning för Projekt_OS - Olympic Games Data Analysis. Projektet fokuserar på att analysera historisk olympisk data från Kaggle, med särskilt fokus på Kanada."

**[Screen: Show project structure]**

"Jag har strukturerat projektet enligt best practices med separata moduler för datahantering, analys och visualisering. Låt mig gå igenom de viktigaste komponenterna."

---

## 💻 Code Walkthrough (6-7 minutes)

### 1. Data Loader - GDPR-kompatibel anonymisering (1.5 min)

**[Screen: Open `src/data_loader.py`]**

"Låt mig börja med data_loader.py. Här implementerar jag GDPR-kompatibel anonymisering av idrottarnas namn."

**[Highlight the anonymization code]**

"Jag använder SHA-256 hash-funktionen för att anonymisera namnkolumnen. Detta är en kryptografiskt säker hashfunktion som ger unika hashvärden för varje namn. Jag tar de första 16 tecknen av hashen för läsbarhet, men behåller unikheten."

**Tekniskt språk:**
- "SHA-256 är en kryptografisk hashfunktion som producerar en 256-bit hash. Hash collision är praktiskt taget omöjlig med SHA-256, vilket säkerställer att varje namn får en unik identifierare."
- "Jag använder lambda-funktioner tillsammans med pandas apply-metoden för vektoriserad bearbetning, vilket är mer effektivt än iterativ bearbetning."
- "Efter hashning tas originalnamnet bort från DataFrame för att följa GDPR-principer om dataminimering."

**[Show the function]**

"Funktionen `load_and_anonymize_data` returnerar en DataFrame där namnkolumnen är ersatt med hashade värden. Detta möjliggör analys utan att exponera personuppgifter."

---

### 2. Data Processor - OOP-struktur (2 min)

**[Screen: Open `src/data_processor.py`]**

"För analysen har jag implementerat en objektorienterad klass kallad OlympicAnalyzer. Detta följer OOP-principer och gör koden modulär och återanvändbar."

**[Highlight the class definition]**

"Klassen använder encapsulation - data och metoder är inkapslade i ett objekt. Detta möjliggör state management och återanvändbarhet."

**Tekniskt språk:**
- "Jag använder method chaining och pandas lazy evaluation för minnesoptimering. Istället för att skapa kopior av data, arbetar jag med views och filtreringar."
- "Varje metod returnerar en pandas Series eller DataFrame, vilket möjliggör method chaining för mer läsbar kod."
- "Jag använder boolean indexing i pandas för effektiv filtrering, vilket är betydligt snabbare än iterativ filtrering."

**[Show key methods]**

"Låt mig visa några viktiga metoder:"

1. **`top_sports_by_medals`**: "Denna metod använder value_counts() för att räkna medaljer per sport och head() för att begränsa resultatet. Detta är en O(1) operation tack vare pandas optimering."

2. **`medals_per_olympics`**: "Här använder jag groupby() med Year som nyckel, vilket är en effektiv aggregering. Detta möjliggör tidsbaserad analys."

3. **`sport_analysis`**: "Denna metod returnerar en dictionary med flera analyser. Detta är ett exempel på data abstraction - användaren behöver inte veta hur analysen görs internt."

**Designprinciper:**
- "Single Responsibility Principle: Varje metod har ett specifikt ansvar."
- "DRY (Don't Repeat Yourself): Gemensam logik är centraliserad i klassen."
- "Open/Closed Principle: Klassen är öppen för utökning men stängd för modifiering."

---

### 3. Dashboard - Interaktiv visualisering (2.5 min)

**[Screen: Open `src/dashboard.py`]**

"Dashboarden är byggd med Plotly Dash, vilket möjliggör interaktiva web-baserade visualiseringar."

**[Show the layout]**

"Layouten är strukturerad med HTML-komponenter från Dash. Jag använder CSS-klasser för enhetlig styling, vilket säkerställer konsistent design genom hela applikationen."

**Tekniskt språk:**
- "Jag använder Dash callbacks med decorator pattern för att hantera state management. Callbacks är reaktiva - de triggas automatiskt när input ändras."
- "Plotly Express används för deklarativ visualisering, vilket ger snygga färgskalor och interaktiva element som zoom och pan."
- "Jag använder color_continuous_scale med Viridis och Plasma palettes, vilka är färgblind-vänliga och perceptuellt uniforma."

**[Show callback functions]**

"Låt mig förklara callback-mekanismen:"

**[Highlight callback decorator]**

"`@app.callback` decorator definierar vilka outputs som uppdateras baserat på vilka inputs. Detta är ett exempel på reactive programming - UI uppdateras automatiskt när data ändras."

**Visualiseringar - Designmotivering:**

1. **Horisontella stapeldiagram**: "Jag valde horisontell orientering för sportnamn eftersom de ofta är långa. Detta förbättrar läsbarheten och undviker roterad text."

2. **Linjediagram över tid**: "Linjediagram är optimala för tidsbaserad data eftersom de visar trender tydligt. Markers gör det lätt att identifiera specifika datapunkter."

3. **Histogram för ålder**: "Histogram visar fördelningen av kontinuerlig data. Jag använder 30 bins för att balansera detaljnivå och läsbarhet."

4. **Cirkeldiagram för kategorier**: "Pie charts är lämpliga för att visa proportioner av kategoriska data, som medaljtyper eller könsfördelning."

**Färgval:**
- "Viridis och Plasma palettes är valda för att de är perceptuellt uniforma - lika steg i data ger lika steg i visuell perception."
- "Dessa palettes är också färgblind-vänliga, vilket följer accessibility best practices."

---

### 4. CSS Styling - Enhetlig design (0.5 min)

**[Screen: Open `assets/style.css`]**

"CSS-filen säkerställer enhetlig design genom hela dashboarden. Jag använder CSS-klasser för konsistent styling, vilket är viktigt för 'Väl Godkänt' eftersom dashboarden inte ska se ut som om flera personer arbetat på den."

**Designprinciper:**
- "Responsiv design med media queries för olika skärmstorlekar."
- "Enhetlig färgpalett och typografi."
- "Box shadows och border-radius för modern, professionell look."

---

## 🎯 Dashboard Demo (1.5 min)

**[Screen: Show running dashboard]**

"Låt mig demonstrera dashboarden i aktion."

**[Interact with dashboard]**

1. **Landstatistik (Kanada)**: 
   - "Här ser vi Kanadas prestation. Vi kan se vilka sporter Kanada är starkast i, medaljer över tid, åldersfördelning och medaljtyper."
   - "När jag ändrar landet i dropdown uppdateras alla visualiseringar automatiskt tack vare callback-mekanismen."

2. **Sportstatistik**:
   - "Här kan vi analysera specifika sporter. Jag väljer Swimming som exempel."
   - "Vi ser medaljfördelning mellan länder, åldersfördelning, könsfördelning och medaljtyper för denna sport."
   - "Detta ger insikter om sportens karaktär - till exempel om det är en ungdomlig sport eller om det finns könsbalans."

**Interaktivitet:**
- "Alla visualiseringar är interaktiva - användaren kan zooma, pana och hovra för mer information."
- "Callback-funktioner säkerställer att all data uppdateras i realtid när användaren ändrar val."

---

## 📊 Research Questions & Methodology (1 min)

**[Screen: Show notebook or code]**

"Min forskningsfråga var: 'Hur har Kanada presterat i olympiska spelen över tid, och vilka sporter är Kanada starkast i?'"

**Metodologi:**
1. "Jag började med explorativ dataanalys för att förstå datastrukturen."
2. "Jag implementerade anonymisering för GDPR-compliance."
3. "Jag skapade modulära analysfunktioner med OOP."
4. "Jag visualiserade resultaten med interaktiva dashboards."

**Val av visualiseringar:**
- "Horisontella stapeldiagram valdes för läsbarhet av långa sportnamn."
- "Linjediagram valdes för att visa tidsbaserade trender."
- "Histogram valdes för att visa fördelningar av kontinuerlig data."
- "Cirkeldiagram valdes för att visa proportioner av kategoriska data."

---

## 🎓 Reflection & Learnings (1 min)

**[Screen: Show code or dashboard]**

"Genom detta projekt har jag lärt mig:"

1. **Datahantering**: "Hur man hanterar stora dataset effektivt med pandas och implementerar GDPR-kompatibel anonymisering."

2. **OOP i Python**: "Hur objektorienterad programmering kan göra kod mer modulär och återanvändbar."

3. **Interaktiva visualiseringar**: "Hur Plotly Dash möjliggör skapandet av professionella, interaktiva dashboards."

4. **Designprinciper**: "Vikten av enhetlig design och användarvänlighet i data visualisering."

**Tekniska lärdomar:**
- "Method chaining och lazy evaluation i pandas för prestanda."
- "Callback decorators i Dash för state management."
- "Färgblind-vänliga palettes för accessibility."

**Framtida förbättringar:**
- "Jag skulle kunna lägga till fler filter, som tidsperiod eller medaljtyp."
- "Machine learning för att förutsäga framtida prestationer."
- "Geografiska visualiseringar med kartor."

---

## 🏁 Conclusion (30 seconds)

**[Screen: Show GitHub repo and dashboard]**

"Sammanfattningsvis har jag skapat en komplett lösning för olympisk dataanalys med fokus på Kanada. Projektet inkluderar GDPR-kompatibel anonymisering, modulär OOP-kod, och en interaktiv dashboard med välmotiverade visualiseringar."

"All kod finns tillgänglig på GitHub, och dashboarden är deployad på [länk till deployed app]."

"Tack för att ni tittade!"

---

## 📝 Tips for Recording

1. **Preparation**:
   - Testa alla funktioner innan inspelning
   - Ha GitHub repo öppet i webbläsare
   - Ha dashboarden körandes lokalt
   - Ha koden öppen i editor

2. **Recording Setup**:
   - Använd OBS Studio eller Teams screen recording
   - Se till att både skärm och kamera är synliga (om krävs)
   - Testa ljudkvalitet innan inspelning

3. **During Recording**:
   - Tala tydligt och i normal hastighet
   - Använd tekniskt språk för "Väl Godkänt"
   - Pausa vid kodgenomgångar för att ge tittaren tid att läsa
   - Demonstra interaktivitet i dashboarden

4. **Post-Production**:
   - Klipp bort långa pauser
   - Se till att video är 5-10 minuter
   - Lägg till textoverlay om nödvändigt för tydlighet

---

## ⏱️ Time Breakdown

- Introduction: 1 min
- Code Walkthrough: 6-7 min
  - Data Loader: 1.5 min
  - Data Processor: 2 min
  - Dashboard: 2.5 min
  - CSS: 0.5 min
- Dashboard Demo: 1.5 min
- Research Questions: 1 min
- Reflection: 1 min
- Conclusion: 0.5 min

**Total: ~10 minutes**

