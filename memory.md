# Swasthi — Project Memory

## Who You Are
- **Raj** — 18, first-year B.Tech AI&DS, Chennai. Building software/backend for uncle's company.
- **Uncle Suryanarayanan Gopalakrishnan** — Owner of Swasthi Computers LLP, Chennai IT services company founded 1993.

---

## Project 1: WindTrack (IoT Wind Turbine Monitoring)

**Status:** Deployed live, showcased on website as flagship case study.

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

## Project 2: Swasthi Website — Build v1 (Complete)

### What Was Built
- **18 pages total:** Home, 6 solution pages, Industry 5.0, Use Cases, About, Contact, 7 catalogue PDFs
- **Static HTML/CSS/JS** — Tailwind via CDN, no build step, no backend
- **Warm color system:** swasthi-blue #1F5FA8, swasthi-gold #D9A23D, swasthi-bg #FAF7F2, swasthi-text #2B2622

### Key Decisions (locked)
- Multi-page HTML (each page crawlable, no SPA)
- Contacts via `mailto:` link + clipboard copy button (no Formspree/web3forms)
- Service catalogue PDFs generated via Python + ReportLab (7 PDFs)
- All PDF links use `download` attribute for native browser download
- Hero background images on all 6 solution pages (from `assets/solutions/`)
- Deliverability tiers: [Proven] / [Now] / [Aspire] — load-bearing at sentence level

### Site Structure
```
Home
├── Solutions (mega-menu, 6 sub-pages)
│   ├── Enterprise AI Adoption
│   ├── Microsoft Copilot & Cloud
│   ├── Data Engineering & Big Data
│   ├── Automation & AIOps
│   ├── Security
│   └── Managed IT Services
├── Industry 5.0 (dedicated page)
├── Use Cases (WindTrack + 6 Microsoft industry scenarios)
├── About (company story + Surya's team entry + Custom Software section)
└── Contact (mailto + copy button)
```

### Service Catalogue PDFs
- **Generator:** `catalogue/generate_pdfs.py` (Python + ReportLab)
- **7 PDFs:** Enterprise AI Adoption, Copilot & Cloud, Data Engineering, Automation & AIOps, Security, Managed IT, Master
- **Content structure:** PROVEN / NOW / ASPIRE sections per service (except master which is flat with hedging)
- **Trigger:** `python3 catalogue/generate_pdfs.py` — regenerates all 7

### Known Fixes Applied (v1)
- Removed MLOps/AIOps cards from Enterprise AI Adoption page (belonged on Automation & AIOps)
- Security page kept entirely [Aspire] with hedged language + disclaimer
- Use Cases placeholder cards replaced with 6 full-weight Microsoft industry scenarios
- Contact form replaced with mailto link + clipboard copy button
- Asset filenames with spaces renamed to hyphens
- About page placeholder leak fixed — Suryanarayanan Gopalakrishnan entry added with photo
- Custom Software section updated to only Kindled + WindTrack (linked)
- Master catalogue Security entry hedged with "emerging capability" language

---

## Project 2: Uncle's Feedback (June 22, 2026) — Website v2 Changes Needed

### CLEAR / Actionable (no further questions needed):
1. **Brand rename:** Every occurrence of "Swasthi Computers" → "Swasthi" (including logo, titles, meta, body copy, footer copyright — everywhere). Uncle explicitly said "Computers" reads as legacy.
2. **Theme:** Blue & white only — remove all gold (#D9A23D) and warm off-white (#FAF7F2). Full blue/white color scheme.
3. **Contact page:** Add two phone numbers split by purpose:
   - Sales: +91-9940197146
   - Support: +91-9791043399
   - (Currently has single number +91 98403 97774)
4. **Logo:** Pull from existing site (swasthicomputers.com) for now, replace when uncle provides.

### VAGUE / Needs uncle clarification:
1. **"Theme is not aligning"** — could mean colors, fonts, spacing, or page-to-page inconsistency. Raj to ask: *"When you say theme isn't aligning, is it the colors, fonts, or that pages feel inconsistent with each other?"*
2. **"Use cases are not context sensitive"** — could mean they should be industry-tailored to the viewer, or something else. Raj to ask: *"Do you mean they should be tied to whoever's industry is viewing the site, or something else?"*
3. **Contact Forms / Appointment form** — no detail on what's needed (missing? broken? needs redesign?). Raj to ask uncle for specifics.
4. **"I am looking for more context"** — unclear which part needs more substance (whole site? use cases? services?). Raj to ask: *"Context on which part specifically — the use cases or the whole site?"*

### Strategy if uncle is vague again:
- Don't ask open-ended questions — give him concrete options to choose from
- "I'll push 2 versions, you pick" approach
- Propose, don't ask him to design

### Open Items (from v1, still pending):
1. WindTrack: capacity factor realism fix (~49% → 25-35%)
2. Deploy to Vercel / GitHub Pages for live hosting
3. Custom domain (swasthicomputers.com or .ai domain)

---

### GitHub
- Repo: `github.com/gsraj0301/Swasthi-Computers`
- Branch: `main`
- All files committed and pushed
