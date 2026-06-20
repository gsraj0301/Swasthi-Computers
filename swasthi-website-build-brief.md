# Swasthi Computers — Website Rebuild Brief
**For: OpenCode (agentic build)**
**From: Raj, working with uncle Surya (owner, Swasthi Computers LLP)**

---

## 1. Project Context

Swasthi Computers LLP is a Chennai-based IT services company, founded 1993. Owner Surya has ~30 years in the Microsoft ecosystem. The current site (swasthicomputers.com) is a broken, half-finished template build — nav links for "Services" and "About" dead-end back to the homepage, one page has unreplaced lorem-ipsum placeholder text, and the SSL cert is expired. **Treat the old site as dead. Do not reuse its layout, design, or copy.** Some of its text was lifted near-verbatim from Microsoft's own marketing pages — that is not acceptable for the new site (see Section 5).

**Stack decision (final):** Static HTML/CSS/JS only. No backend, no server, no database. The only dynamic element is the contact form, which should POST to a free form-handling service (Formspree or web3forms) that emails info@swasthicomputers.com. Do not build a Flask/Django/Node backend — there is no functional need for one.

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

**Security** — new category
- SOC (Security Operations Center)
- AI Security

**Enterprise AI Adoption & Industry 5.0** — mixed tier, see breakdown
- Enterprise AI adoption consulting / AI readiness assessment — [Aspire]
- Industry 5.0 advisory, centered on predictive MRO (Maintenance, Repair & Overhaul) — [Now], content direction confirmed (see Section 3)
- IoT monitoring & predictive maintenance / MRO — anchored by WindTrack, the one fully real, live flagship case — [Proven, via WindTrack]

**Raj's individual differentiator** — [Proven] (belongs on the About page, not the Solutions nav — see Section 3)
- Custom Software & Applied AI Product Development
- Proof points: Kindled, Speakora, Traqo (architectural review), Agni PRIDE Hackathon Portal, WindTrack

---

## 3. Site Structure (final)

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
├── Use cases
├── About
└── Contact
```

**Why this shape:** 6 top-level nav items, not 8+. Solutions groups by client problem, not by Microsoft product name, so the nav reads "consultancy" not "Microsoft reseller catalogue." Each sub-area still gets a full page — nothing is buried, it's just one click deeper.

**Page content notes:**
- **Home** — positioning statement, links into the 4 strongest pillars (Enterprise AI Adoption, Copilot, Data Engineering/Big Data, Industry 5.0), WindTrack as flagship proof, download link for the master Service Catalogue PDF (see Section 4).
- **Solutions sub-pages** — one page per category above, each ending with a "Download the one-pager" link to its matching catalogue PDF.
- **Industry 5.0** — content direction now confirmed, no longer blocked, build it. Centerpiece is **predictive MRO (Maintenance, Repair & Overhaul)** — Surya specifically flagged this as the hottest market need right now, and WindTrack's roadmap (an MRO prediction ML model) makes it Swasthi's strongest, most concrete proof point. Structure the page around the three established Industry 5.0 pillars (human-centric, sustainable, resilient — per the EU Commission's original 2021 framing), but don't force all three equally:
  - **Resilient** — the strongest pillar, lead with this. Predictive MRO is a textbook resilience story: catching equipment failure before it cascades. WindTrack is the concrete example.
  - **Human-centric** — frame AI automation as freeing technicians from repetitive manual monitoring so they can focus on judgment-based work, not as replacing them. That distinction is the actual point of the term — get the framing right, don't just say "AI does the work now."
  - **Sustainable** — only include if there's a genuine claim (e.g. extending asset lifespan via maintenance reduces waste/replacement). Don't manufacture a sustainability angle that isn't real — underweight this pillar rather than overstate it.
  
  WindTrack should visually anchor this page, not just get a sentence — same instruction as Section 7's design guidance.
- **Use cases** — WindTrack (real, live: see Section 5 for the URL) + Microsoft-sourced illustrative industry examples (healthcare, insurance, banking/financial services, general services). See Section 5 for sourcing rules — this is not yet unblocked.
- **About** — company story, "Microsoft Partner" (general phrasing, see Section 5), Raj's Custom Software & Applied AI Product Development section, and a placeholder for Surya's name/photo (open item #2, Section 6 — build this section so it's trivial to add or remove once he decides).
- **Contact** — form (Formspree/web3forms, see Section 1), plus the master catalogue PDF download repeated here as a CTA.

---

## 4. Service Catalogue PDF System

- Static, build-time generated. No live/dynamic PDF generation, no backend.
- **One PDF per Solutions sub-page (6 total) + one master combined PDF.** Confirmed with Surya.
- Master PDF download link lives on the **Home page** and is repeated on **Contact**.
- Each Solutions sub-page has its own one-pager download link at the bottom.
- **Implementation rule: do not duplicate content.** Write each service category's copy once in a shared content source (e.g. a markdown or JSON file per category), and use that single source to render both the website section and its matching PDF. The master PDF is just all 6 sources concatenated. This keeps web copy and catalogue copy from drifting out of sync.

---

## 5. Content Sourcing & Voice Rules — read carefully, these are not optional

1. **Never copy Microsoft's marketing copy verbatim.** The old site's mistake (an entire Dynamics 365 Copilot section lifted near-word-for-word from Microsoft's own site) is not to be repeated. Use Microsoft's official pages to verify technical accuracy of Copilot/M365/Azure/Dynamics 365/Power Platform/AI Foundry claims, then write original copy in Swasthi's voice.
2. **Use cases page is the one exception, but it's conditional and currently blocked.** Surya has stated Swasthi has rights to use Microsoft's partner use-case content, and that any Microsoft-sourced use case should carry a "Powered by Microsoft" label. **However: the exact source of this content (Partner Center marketing library vs. public Microsoft case studies vs. something else) has not been confirmed yet** — a message is out to Surya asking this. Do not build out this page with placeholder/invented Microsoft content; leave it structurally ready (headings, layout, "Powered by Microsoft" badge placement) but wait for the actual source material before filling it in with real Microsoft-sourced text.
3. **WindTrack is the one fully real, non-Microsoft case study.** It's a live deployed IoT wind turbine monitoring proof-of-concept: Python synthetic data generator (100 turbines, India-realistic), Streamlit dashboards (Asset + Power Generation, Plotly), deployed via GitHub → Streamlit Cloud. Live at: `windtrack-j4l6fmrgkx5n8r9kodjgya.streamlit.app`. Its planned MRO (Maintenance, Repair & Overhaul) prediction model is the single strongest proof point for the Industry 5.0 positioning — see Section 3 for how to build that page around it. Feature WindTrack prominently on both the Industry 5.0 page and Use Cases page. **Attribution is still undecided** (Raj personally vs. Swasthi the company) — use neutral phrasing like "developed by our technical team" until Section 6 open item #1 is resolved.
4. **Microsoft Partner: use the word generally, plus the logo, once provided.** Surya has confirmed Swasthi can use "Microsoft Partner" (no specific tier/designation needed — general phrasing is fine) and the official Microsoft Partner logo. **The actual logo file and/or MPN ID has not been provided yet** (Section 6, open item #2). Build the About page (and footer, if appropriate) with a clearly marked placeholder for this logo so it's a one-line swap once the asset arrives — do not use a generic/unofficial Microsoft Partner badge graphic pulled from a web search as a stand-in.
5. **Deliverability tiers control tone, not just content.** [Proven] and [Now] items get direct, confident language ("We build and deploy X"). [Aspire] items get forward-looking, hedged language ("We're building capability in X" / "Talk to us about your X roadmap"). Do not flatten this distinction in copy — it's there specifically so Swasthi doesn't overpromise on a sales call.

---

## 6. Open Items — Not Yet Resolved (build around these, don't fake them)

1. **WindTrack attribution** — Raj personally vs. Swasthi as company. Use neutral language until decided.
2. **Microsoft Partner logo file / MPN ID** — Surya has confirmed rights to use it. Raj has asked him to generate it via Partner Center's Logo Builder and send the file — request sent, awaiting reply. Placeholder it until it arrives; do not substitute an unofficial badge graphic.
3. ~~**Industry 5.0 — Surya's actual definition.**~~ **RESOLVED.** Content direction confirmed: predictive MRO as the centerpiece, built on the three-pillar Industry 5.0 framework. See Section 3 for the full breakdown. No longer blocked — build this page now.
4. **Microsoft use-case content source** — exact origin of the licensed content Surya referenced. A question is out to him. Don't build real copy for the Use Cases page's Microsoft-sourced sections until this comes back.
5. **Surya's name/photo on About page** — undecided whether he wants personal visibility or company-only framing. Build the About page section modularly so this is a quick add/remove either way.
6. **Service Catalogue format confirmation** — static modular PDFs is Raj's recommendation and is the build approach in this brief (Section 4), but Surya hasn't explicitly confirmed over the dynamic-builder alternative. Proceed with static PDFs; this is a low-risk default that's easy to extend later if a dynamic version is ever wanted.

---

## 7. Design Guidance

- Professional B2B enterprise consulting aesthetic. Not flashy/over-animated, not generic stock-photo MSP-template look (which is exactly what the old site was).
- Clean typography, intentional layout choices — avoid the look of an unstyled framework default.
- Fully responsive. Fast-loading static pages, no unnecessary JS weight.
- WindTrack and the Microsoft Copilot capability are the two things this site needs to make feel unmistakably real and current — give them real visual weight, not just a bullet in a list.

---

## 8. How to Work Through This

1. Scaffold the page structure and nav first (Section 3) with placeholder headings — no copy yet.
2. Write Solutions sub-pages using Section 2's confirmed inventory and Section 5's tone rules.
3. Build the About and Contact pages, with the two placeholder sections from Section 6 clearly marked in code comments (e.g. `<!-- TODO: Microsoft Partner logo — pending file from Surya -->`).
4. Build the Industry 5.0 page now using Section 3's confirmed content direction (predictive MRO centerpiece, three-pillar framework) — it is no longer blocked. The Microsoft-sourced portion of Use Cases stays structurally complete but content-empty until Section 6 item #4 (use-case content source) is resolved — do not invent filler copy for that part only.
5. Build the modular Service Catalogue PDF generation last, once the per-category content exists, per Section 4's single-source rule.
6. Flag back any point where a confident capability claim is about to be written for something tagged [Aspire] — that's a tone violation, not a style choice.
