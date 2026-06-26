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

## Project 2: Uncle's Feedback (June 22, 2026) — Website v2

### ✅ Completed (June 23, 2026)
1. **Brand rename:** "Swasthi Computers" → "Swasthi" — every occurrence across all 19 HTML files (titles, meta, nav, body, footer, copyright, catalogue). Email `info@swasthicomputers.com` preserved.
2. **Color scheme:** Blue & white only.
   - Primary blue: `#0AA0E4` (extracted from `logo.png`)
   - Hover blue: `#0990CC`
   - Light blue bg: `#E8F4FD` (hover states)
   - Removed: gold `#D9A23D`, warm off-white `#FAF7F2`, old navy `#1F5FA8`
   - Cards: white with gray border (`card-custom`), warm bg removed
   - Text: dark `#1A202C` for readability
3. **Contact page:**
   - Sales: +91-9940197146
   - Support: +91-9791043399
   - Old single number (+91 98403 97774) removed from all pages
4. **Logo:** `assets/logo.png` placed by Raj, replaces text logo in nav + footer across all 18 pages.

### 🛠 Additional Fix
- **CTA button contrast:** Added `.btn-cta` CSS class (white bg, blue text) for buttons on the blue CTA banners. Applied to 11 CTA "Contact us"/"Email us" buttons. Nav/hero buttons stay as `.btn-primary` (blue on white).

### Current Color System
| Token | Hex | Usage |
|-------|-----|-------|
| `swasthi-blue` | `#0AA0E4` | Primary brand blue — buttons, links, CTA banners |
| `swasthi-text` | `#1A202C` | Dark text for body and headings |
| White | `#FFFFFF` | Page backgrounds, cards, nav, footer |
| `#E8F4FD` | Light blue | Hover states on white bg |
| `#0990CC` | Darker blue | Button hover state |

### VAGUE / Needs uncle clarification:
1. **"Theme is not aligning"** — could mean colors, fonts, spacing, or page-to-page inconsistency. Raj to ask: *"When you say theme isn't aligning, is it the colors, fonts, or that pages feel inconsistent with each other?"*
2. **"Use cases are not context sensitive"** — could mean they should be industry-tailored to the viewer, or something else. Raj to ask: *"Do you mean they should be tied to whoever's industry is viewing the site, or something else?"*
3. **Contact Forms / Appointment form** — no detail on what's needed (missing? broken? needs redesign?). Raj to ask uncle for specifics.
4. **"I am looking for more context"** — unclear which part needs more substance (whole site? use cases? services?). Raj to ask: *"Context on which part specifically — the use cases or the whole site?"*

### Strategy if uncle is vague again:
- Don't ask open-ended questions — give him concrete options to choose from
- "I'll push 2 versions, you pick" approach
- Propose, don't ask him to design

### Open Items (still pending):
1. WindTrack: capacity factor realism fix (~49% → 25-35%)
2. Deploy to Vercel / GitHub Pages for live hosting
3. Custom domain (swasthicomputers.com or .ai domain)

---

### ✅ Completed (June 26, 2026) — Round 3 changes
1. **Global Reach location map** — Hub-and-spoke SVG map (APAC, EMEA, North America → Chennai HQ) added to:
   - **About page** — full two-column section between Microsoft Partner and Custom Software
   - **Home page** — two-column section between WindTrack and CTA banner (enlarged from 32px icon to 300px SVG on second commit)
   - CSS: `.map-line` class with pulse animation for connecting lines
2. **"since 1993" → "for three decades"** — replaced across all 11 HTML files (meta descriptions, hero text, footer, managed-it page descriptions, About page story). Removed bare year reference from "founded in 1993" on About page.

---

### ✅ Completed (June 26, 2026) — Round 4 changes (Section 9.1-9.3)
1. **9.1 — Added granular capability cards across 4 pages:**
   - **Managed IT Services:** +3 cards — Custom Application Development [Proven], Infrastructure Migration & Modernization [Now], Application Migration & Modernization [Now] (6 total, `lg:grid-cols-3`)
   - **Microsoft Copilot & Cloud:** +2 cards — Power Platform Governance [Now], M365 & Modern Workplace [Now] (8 total)
   - **Data Engineering & Big Data:** +1 card — Microsoft Fabric [Now] with OneLake/dataflows/notebooks (4 total)
   - **Security:** +1 card — Compliance & Risk Management [Aspire] (hedged tone, disclaimer preserved, 3 total)
   - **No changes:** Automation & AIOps, Enterprise AI Adoption

2. **9.2 — Two real booking links live:**
   - **Contact page:** New "Book a meeting" section above email form with two buttons — "Schedule a Consulting Appointment" (Surya 30-min booking) + "Schedule Technical & Implementation Support" (Helpdesk)
   - **Home page hero:** "Talk to an expert" replaced with "Book a Consultation" linking to Surya's booking URL. Hero stays at 2 clean buttons (book now + browse services)

3. **9.3 — Microsoft source cross-reference:**
   - Fetched 6 official Microsoft pages (Adoption, Copilot Studio, Fabric, Security, M365 Enterprise, Dynamics 365, Microsoft Foundry)
   - **Key find:** "Azure AI Foundry" renamed to "Microsoft Foundry" — updated on Copilot & Cloud page (card title, description, meta description), Enterprise AI Adoption page (Agentic AI card), and Use Cases page (Insurance card)
   - Enterprise AI Adoption: Agentic AI card now explicitly mentions "Microsoft Foundry with Foundry Agent Service and Copilot Studio"
   - Fabric card confirmed accurate against Microsoft's own page
   - Security page correctly stays generic/hedged — no specific Microsoft product claims (appropriate for [Aspire])

### Hosting/Domain update (June 26)
- **Final host:** Cloudflare Pages (free tier, commercial-use-permitted, keeps GitHub auto-deploy pipeline)
- **Domain:** Keeping existing swasthicomputers.com (not buying .ai — too costly, 2-year minimum)
- **DNS approach:** Single CNAME for `www` + domain forwarding at registrar — avoids touching existing email DNS (MX/SPF/DKIM). Raj & Surya handling at registrar level.
- **Vercel rejected:** Hobby tier forbids commercial use.
- **Replit rejected:** Credit-pool billing has surprise-bill track record.

### Open Items (still pending):
1. WindTrack: capacity factor realism fix (~49% → 25-35%)
2. "Certified expertise" phrase on About page + Global Reach section — needs Surya to confirm certifications, or default to "deep expertise"
3. Microsoft Partner logo file — the `ms-partner-logo.jpeg` was WhatsApp-compressed; needs higher-quality original
4. WindTrack attribution (Raj vs. company) — still undecided
5. Global Reach map SVG color fix needed (uses `#0AA0E4` instead of real brand colors from warm scheme)
6. Surya's photo on About page — still undecided

### GitHub
- Repo: `github.com/gsraj0301/Swasthi-Computers`
- Branch: `main`
- All files committed and pushed
