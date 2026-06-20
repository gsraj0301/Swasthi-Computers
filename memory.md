# Swasthi Computers — Project Memory

## Who You Are
- **Raj** — 18, first-year B.Tech AI&DS, Chennai. Building software/backend for uncle's company.
- **Uncle Surya** — Owner of Swasthi Computers LLP, Chennai IT services company founded 1993.

---

## Project 1: WindTrack (IoT Wind Turbine Monitoring)

**Status:** Deployed live, uncle liked it but wants real-data readiness proof.

**Live URL:** `windtrack-j4l6fmrgkx5n8r9kodjgya.streamlit.app`

**Built with:** Python synthetic data generator (100 turbines, India-realistic), Streamlit Asset Dashboard + Power Generation Dashboard (Plotly), deployed GitHub → Streamlit Cloud.

**Known issues:**
- Capacity factor too high (~49%, should be 25-35%) — needs fixing
- Uncle felt "too virtual" — needs proof of real-data readiness

**Next planned work (not started):**
1. Fix capacity factor realism
2. Build live data simulator + ingestion API (prove real-sensor readiness)
3. Eventual MRO prediction ML model (the actual licensable product)

**Team setup:** Raj = software/backend. Uncle has separate hardware people lined up if investors come through.

---

## Project 2: Swasthi Computers Website Revamp (Active)

### Current Site State
- Domain: swasthicomputers.com — expired SSL cert
- Design: ~2015-era, broken single-page template
- Content: Copied Microsoft marketing text, lorem-ipsum placeholders, dead nav links (Home/Services/About all point to same page)
- No real services or about page content — full rebuild needed

### Uncle's Requirements
- Full rebuild, Raj has free hand
- Reposition toward: Enterprise AI Adoption, Data Engineering, Big Data, Industry 5.0
- Dedicated Industry 5.0 page
- Microsoft Copilot capability featured (genuinely sellable today)
- Use-case examples: healthcare, insurance, banking, financial services, general services — **illustrative/hypothetical, NOT real client claims**
- WindTrack = one real, live flagship case study
- Eventually wants to buy a .ai domain

### Tech Decision
- **Static HTML/CSS/JS.** No Flask/Django. No backend needed.
- Contact form → email info@swasthicomputers.com via Formspree/web3forms (free, no server).

### Key Fact: Swasthi is a Microsoft Partner
- Not yet confirmed which specific Solutions Partner designation(s) Swasthi holds (Data & AI, Modern Work, Business Applications, Infrastructure, etc.)
- Partner Center access would give official co-branded marketing assets (licensed for reuse) and partner badge logos
- Partner badge is a third-party trust signal — more credible than any self-claimed service description
- **Open question:** which designation(s) and does Surya have Partner Center login?

### Content Sourcing Rule
- Use Microsoft's site for technical accuracy (what Copilot, AI Foundry, Dynamics 365 etc. actually do)
- Rewrite in Swasthi's own voice — do NOT copy-paste Microsoft marketing paragraphs
- Old site's main problem was verbatim Microsoft copy; avoid copyright exposure and generic positioning
- If Partner Center access exists, use official partner content kits (licensed for reuse)

### Open Questions (still need uncle's input)
1. WindTrack: credit Raj personally or present as Swasthi Computers' delivered work?
2. About/Team page: uncle's name/photo or keep it company-only?
3. Which Microsoft Partner designation(s) does Swasthi hold? Does he have Partner Center login?
4. What does "Industry 5.0" mean specifically to him? (broad term — needs concrete definition)

### Proposed Site Structure (pending uncle's input)
Homepage → Enterprise AI Adoption → Data Engineering → Big Data → Industry 5.0 → Use Cases (WindTrack + 5 illustrative industries) → About → Contact

---

## V1 Service Inventory (Draft — needs uncle's confirmation)

Each item tagged: [Proven] = delivered before · [Now] = can execute today · [Aspire] = positioning/direction

### Core Managed IT Services
- Backend Technical Support — onsite IT, incident resolution, SLA/emergency support [Proven]
- AI-Infused Remote IT Automation — remote maintenance, patching, log analytics/dashboards [Proven]
- IT Modernization — hybrid infra & modern workplace transformation [Proven]

### Intelligent Process Automation
- Digital Process Automation (Power Automate cloud flows) [Now]
- Robotic Process Automation (legacy/UI-based automation) [Now]
- AI Document Automation (form/document intelligence, extraction) [Now]
- End-to-end IPA (combining the above) [Now]

### Microsoft Copilot & Generative AI
- Copilot for Microsoft 365 (Teams/Outlook/Word/Excel) [Now]
- Copilot for Dynamics 365 (Sales, Customer Service, Customer Insights/Marketing) [Now]
- AI-powered customer service (chatbots, conversational IVR) [Now]
- Generative AI adoption advisory [Now] — Surya confirmed
- **Agentic AI** — autonomous AI agents for multi-step business processes [Now]
- **Azure AI Foundry** — Microsoft platform for building/customizing AI models and agents [Now]

### Microsoft Modern Workplace & Cloud
- Microsoft 365 deployment & management [Proven]
- Azure [Now]
- Dynamics 365 (CRM/ERP) [Now]
- Business Central (ERP) [Now]

### Data & Analytics
- Modern BI / Data Warehousing [Now]
- Data Engineering [Now] — Surya confirmed staffable/executable
- Big Data [Now] — Surya confirmed staffable/executable

### Enterprise AI Adoption & Industry 5.0
- Enterprise AI adoption consulting / AI readiness assessment [Now]
- Industry 5.0 advisory [Aspire] — still need concrete definition from Surya
- IoT monitoring & predictive maintenance (WindTrack flagship) [Proven, via WindTrack]

### Confirmed by Surya (moved from open questions)
- ✅ Data Engineering / Big Data are deliverable, not just positioning
- ✅ IPA/RPA/DPA has been delivered to real clients
- ✅ Swasthi is a Microsoft Partner (specific designation TBD)
- ✅ Agentic AI and AI Foundry are real offerings to include

---

## Working Style
- Raj wants 5+ steps at a time, concepts before code
- Copy-paste fine for scaffolding/boilerplate (reading/understanding > typing)
- Honest mentor feedback over validation
- Questions asked in plain text at end of response (not button-style multi-choice)
- Raj reads everything first then answers together
- Not a frontend dev — will use agentic coding (OpenCode) for HTML/CSS/JS
- But has some frontend tricks up sleeve too

---

## Website Build Plan — 9 Stages

**Stack:** Multi-page static HTML · Tailwind CSS (CDN `<script>` tag, zero build step) · Vanilla JS

### Key Decisions (locked)

| Decision | Choice |
|---|---|
| **Architecture** | Multi-page HTML (separate `.html` files per page, no SPA/JS routing). Each page crawlable, no router edge cases, no state-persistence need. |
| **Tailwind** | CDN script tag — no Node/npm. Larger CSS payload is fine for a 6-page marketing site. |
| **Color system** | Warm, not cold/dark. Custom Tailwind theme colors (set once in config, reused across all pages):<br>`swasthi-blue: #1F5FA8` (headers, nav, primary buttons)<br>`swasthi-gold: #D9A23D` (CTAs, highlights, hovers — use sparingly)<br>`swasthi-bg: #FAF7F2` (warm off-white backgrounds)<br>`swasthi-text: #2B2622` (warm charcoal body text)<br>No dark/black sections, no stark white-on-white. |
| **Microsoft Partner logo** | WhatsApp-sourced image in project root. Referenced from code — placeholder-ready until official file arrives. |

### Stage 1 — Project Scaffold
- Folder structure: `index.html` + `pages/` (solutions sub-pages, industry-5.0, use-cases, about, contact)
- Base template with Tailwind CDN + custom CSS override block with Tailwind theme config (`swasthi-*` colors)
- Global nav with mega-menu: "Solutions" expands to 6 sub-items, rest are direct links
- Global footer: Microsoft Partner badge, nav links, copyright
- Shared JS file for nav interactivity (mega-menu toggle, mobile hamburger)

### Stage 2 — Home Page
- Hero section: positioning statement, primary CTA (amber)
- 4 pillar highlight cards: Enterprise AI Adoption, Microsoft Copilot, Data & Big Data, Industry 5.0
- WindTrack flagship proof section (visual weight, not just a list item)
- Master Service Catalogue PDF download CTA

### Stage 3 — Solutions Sub-Pages (×6)
- Shared page template: Hero → "How we help" → Capability breakdown (tagged [Proven]/[Now]/[Aspire]) → "Download one-pager" CTA
- **Do NOT force a "Client proof" section onto every page** — that would fabricate testimonials for Aspire-tier services (Security, parts of Enterprise AI Adoption). Only reference WindTrack or real delivery where genuinely earned (Copilot & Cloud, Automation & AIOps), and only as a light "see it in action" link — never invent client claims.
- Each page has a per-category PDF download link at bottom
- 6 pages:
  1. Enterprise AI Adoption
  2. Microsoft Copilot & Cloud
  3. Data Engineering & Big Data
  4. Automation & AIOps
  5. Security
  6. Managed IT Services

### Stage 4 — Industry 5.0 Page
- Hero positioning around predictive MRO
- Three pillars: **Resilient** (lead — WindTrack as anchor), **Human-centric** (framing: AI frees technicians for judgment work, not replaces them), **Sustainable** (only if genuine claim — underweight rather than overstate)
- WindTrack as full-width visual case study (dashboard screenshots, key metrics)

### Stage 5 — Use Cases Page
- WindTrack full case study section
- Microsoft-sourced sections: structure built (headings, "Powered by Microsoft" badge placement, layout), content left as placeholder — blocked until Surya confirms exact source (Section 6 item #4)

### Stage 6 — About Page
- Company story (founded 1993 Chennai, Microsoft partner)
- Microsoft Partner logo section (placeholder until official asset)
- Raj's Custom Software & Applied AI section (Kindled, Speakora, Traqo, Agni PRIDE, WindTrack)
- Surya name/photo section — built modularly, trivial to add or remove (open item)

### Stage 7 — Contact Page
- Form POST → Formspree/web3forms → info@swasthicomputers.com
- Master catalogue PDF download CTA repeated here
- Office/location info

### Stage 8 — Service Catalogue PDF System
- Single content source per category (shared with web copy — no drift)
- 6 one-pagers + master combined PDF
- Static build-time generation, not dynamic
- Linked from: home page (master), contact page (master), each solution page (its matching one-pager)

### Stage 9 — Polish & QA
- Responsive review: mobile / tablet / desktop
- Mega-menu mobile behavior (hamburger → accordion or slide-out)
- Load-time check (images, font loading)
- Content pass: verify every [Aspire] item uses hedged language, not confident claims
- Confirm all TODOs (partner logo, Surya photo, use case content) are marked with visible code comments

### Design Reference: Avanade.com patterns to mirror
- Mega-menu nav (services visible without drilling into sub-pages)
- Page rhythm: Hero → "How we help" → Capability breakdown → CTA
- Partner badge in footer (not just About page)
- Every page ends with a contact CTA bar
- Card-based layout for service listings
- Lots of whitespace, clean typography, no flashy animation
- WindTrack and Copilot get prominent visual weight, not just bullets
