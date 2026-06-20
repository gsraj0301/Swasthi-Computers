# Swasthi Computers — Website Rebuild Brief
**For: OpenCode (agentic build)**
**From: Raj, working with uncle Suryanarayanan Gopalakrishnan (owner, Swasthi Computers LLP)**

---

## 1. Project Context

Swasthi Computers LLP is a Chennai-based IT services company, founded 1993. Owner Surya has ~30 years in the Microsoft ecosystem. The current site (swasthicomputers.com) is a broken, half-finished template build — nav links for "Services" and "About" dead-end back to the homepage, one page has unreplaced lorem-ipsum placeholder text, and the SSL cert is expired. **Treat the old site as dead. Do not reuse its layout, design, or copy.** Some of its text was lifted near-verbatim from Microsoft's own marketing pages — that is not acceptable for the new site (see Section 5).

**Stack decision (final):** Static HTML/CSS/JS only. No backend, no server, no database. Contact via `mailto:` link with clipboard copy button — no form handler needed. Do not build a Flask/Django/Node backend — there is no functional need for one.

**Builder context:** Raj (the person directing this build) is not a dedicated frontend developer and is using agentic coding tools intentionally — he reviews and directs architecturally, writes a meaningful share of code by hand, and treats AI tools as a collaborator, not an autopilot. Flag significant decisions back to him rather than silently assuming. Treat deliverability tiers (Section 2) as load-bearing — they determine how confidently each service can be described.

---

## 2. Confirmed Service Inventory (v1.2 — locked)

Tags: **[Proven]** = actually delivered before · **[Now]** = real capability, confirmed staffed and deliverable today · **[Aspire]** = positioning/direction, not yet proven — use hedged, forward-looking language for these, never confident claims.

**Core Managed IT Services** — [Proven]
- Backend Technical Support (onsite IT, incident resolution, SLA/emergency support)
- Remote IT Automation (maintenance, patching, monitoring, log analytics/dashboards)
- IT Modernization (hybrid infrastructure, modern workplace transformation)

**AI & Process Automation** — [Now], confirmed by Surya directly
- Digital Process Automation (Power Automate / Power Platform)
- Robotic Process Automation (legacy/UI-based automation)
- AI Document Automation (form/document intelligence, extraction)
- Agentic AI (incl. Microsoft's agentic AI stack)
- AIOps (AI-driven IT operations monitoring)
- MLOps (ML model deployment & lifecycle — WindTrack's planned MRO prediction model is the proof point once it ships)

**Microsoft Copilot & Generative AI** — [Now], the headline differentiator
- Copilot for Microsoft 365
- Copilot for Dynamics 365
- Microsoft Copilot Studio (custom copilots/agents)
- AI-powered customer service / chatbots, conversational IVR
- Multi-model capability — also builds with Claude, not locked to one vendor

**Microsoft Modern Workplace & Cloud** — [Now]
- Microsoft 365, Azure, Microsoft AI Foundry, Dynamics 365, Business Central, Power Platform

**Data & Analytics** — [Now], confirmed by Surya directly
- BI / Data Warehousing
- Data Engineering
- Big Data

**Security** — [Aspire] across all capabilities
- SOC (Security Operations Center) — building capability
- AI Security — building capability

**Enterprise AI Adoption & Industry 5.0** — mixed tier, see breakdown
- Enterprise AI adoption consulting / AI readiness assessment — [Now]
- Industry 5.0 advisory, centered on predictive MRO — [Now], content direction confirmed
- IoT monitoring & predictive maintenance / MRO — anchored by WindTrack — [Proven, via WindTrack]

**Custom Software & Applied AI** — [Proven] (About page only)
- Kindled (AI-powered platform) — linked to kindled.pythonanywhere.com
- WindTrack (IoT wind turbine monitoring) — linked to live Streamlit dashboard

---

## 3. Site Structure (final, built)

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
├── About (company story + Surya team entry + Custom Software)
└── Contact (mailto + copy email button)
```

**Total: 18 files** — 1 home + 10 sub-pages + 7 catalogue PDFs.

---

## 4. Service Catalogue PDF System

- **Built with:** Python + ReportLab (not static HTML print-to-PDF)
- **Generator script:** `catalogue/generate_pdfs.py`
- **7 PDFs:** 6 per-solution + 1 master compendium
- **Content structure per PDF:** PROVEN / NOW / ASPIRE section badges with bullet points
- **Master PDF Security entry** explicitly hedged ("emerging capability in...")
- **Trigger:** `python3 catalogue/generate_pdfs.py` — regenerates all 7
- All links use the `download` HTML attribute for native browser download

---

## 5. Content Sourcing & Voice Rules — read carefully, these are not optional

1. **Never copy Microsoft's marketing copy verbatim.** Write original copy in Swasthi's voice.
2. **Use Cases page — built with original illustrative copy** based on Microsoft public industry pages, not copied material. Each card tagged "Powered by Microsoft."
3. **WindTrack** is the one fully real, non-Microsoft case study. Live at `windtrack-j4l6fmrgkx5n8r9kodjgya.streamlit.app`. Featured prominently on Industry 5.0 page and Use Cases page.
4. **Microsoft Partner** — general phrasing used throughout, official logo in all footers and About page.
5. **Deliverability tiers** control tone, not just content. [Proven] and [Now] get direct language. [Aspire] gets forward-looking, hedged language. This distinction is strictly enforced.

---

## 6. Resolved Open Items

1. ~~**WindTrack attribution**~~ — **RESOLVED.** Used neutral phrasing "developed by our technical team."
2. ~~**Microsoft Partner logo file**~~ — **RESOLVED.** WhatsApp-sourced image used, placed in all footers and About page.
3. ~~**Industry 5.0 definition**~~ — **RESOLVED.** Predictive MRO centerpiece, three-pillar framework.
4. ~~**Microsoft use-case content source**~~ — **RESOLVED.** Original illustrative copy written based on Microsoft public industry pages (Healthcare, Insurance, Banking, Professional Services, Manufacturing, Energy).
5. ~~**Surya's name/photo on About page**~~ — **RESOLVED.** Added as "Suryanarayanan Gopalakrishnan — Owner, Swasthi Computers LLP" with profile photo.
6. ~~**Service Catalogue format**~~ — **RESOLVED.** Python + ReportLab PDF generation, 7 PDFs.

---

## 7. Design Guidance

- Professional B2B enterprise consulting aesthetic. Not flashy/over-animated, not generic stock-photo MSP-template look.
- Warm color palette (blue #1F5FA8 + gold #D9A23D on warm off-white #FAF7F2). No dark mode.
- Clean typography (Inter font), intentional layout choices.
- Fully responsive. Fast-loading static pages, no unnecessary JS weight.
- Design reference: Avanade.com — mega-menu nav, hero → "How we help" → CTA page rhythm, partner badge in footer.

---

## 8. Build Stages Completed

1. **Scaffold** — folder structure, base template, global nav with mega-menu, mobile accordion, footer, shared JS
2. **Home page** — hero, 4 pillar cards, WindTrack flagship section, CTA banners
3. **Solutions audit** — MLOps/AIOps moved to Automation page, Security hedged, inventory verified
4. **Industry 5.0** — predictive MRO hero, WindTrack screenshots, related capabilities
5. **Use Cases** — WindTrack case study + 6 Microsoft industry scenario cards
6. **About** — company story, Surya team entry, Custom Software section
7. **Contact** — mailto link + clipboard copy button
8. **Service Catalogue PDFs** — 7 ReportLab-generated PDFs, downloadable site-wide
9. **QA** — all 18 pages verified (200 OK), images exist, links resolve, asset filenames clean
