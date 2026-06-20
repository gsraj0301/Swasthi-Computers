# Swasthi Computers — Project Memory

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

## Project 2: Swasthi Computers Website Revamp (Complete)

### Current Site State (before rebuild)
- Domain: swasthicomputers.com — expired SSL cert
- Design: ~2015-era, broken single-page template
- Content: Copied Microsoft marketing text, lorem-ipsum placeholders, dead nav links
- No real services or about page content — full rebuild needed

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

### Open Items (not yet actioned)
1. WindTrack: capacity factor realism fix
2. Deploy to Vercel / GitHub Pages for live hosting
3. Custom domain (swasthicomputers.com or .ai domain)

### Known Fixes Applied
- Removed MLOps/AIOps cards from Enterprise AI Adoption page (belonged on Automation & AIOps)
- Security page kept entirely [Aspire] with hedged language + disclaimer
- Use Cases placeholder cards replaced with 6 full-weight Microsoft industry scenarios
- Contact form replaced with mailto link + clipboard copy button
- Asset filenames with spaces renamed to hyphens
- About page placeholder leak fixed — Suryanarayanan Gopalakrishnan entry added with photo
- Custom Software section updated to only Kindled + WindTrack (linked)
- Master catalogue Security entry hedged with "emerging capability" language

### GitHub
- Repo: `github.com/gsraj0301/Swasthi-Computers`
- Branch: `main`
- All 47 files committed and pushed
