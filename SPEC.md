# Swasthi Website — Visual Polish & Enhancement SPEC

## Overview

9 enhancements to the Swasthi site, ordered by effort/dependency. Scope: visual polish, structural improvements, and content fixes — all built on the existing honest content foundation.

---

## 1. Scroll Animation Layer

**Files:** `css/style.css`, `js/main.js`  
**Effort:** Low · **Dependencies:** None

Add CSS `@keyframes fade-in-up` + IntersectionObserver-based reveal. No JS library.

### CSS additions (`style.css`)
```css
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### JS additions (`main.js`)
- Add `IntersectionObserver` watching `.reveal` elements
- Threshold 0.15, rootMargin "0px 0px -40px 0px"
- Add `visible` class when element enters viewport

### HTML changes
- Add `class="reveal"` to: hero text container, pillar card grid, WindTrack section, Global Reach section, CTA banner, and all solution page card grids

---

## 2. Stats Strip ("By the Numbers")

**File:** `index.html` (new section between pillar cards and WindTrack)  
**Effort:** Low · **Dependencies:** None

### Content (real stats only)

| Stat | Label |
|---|---|
| 3 decades | serving enterprises since 1993 |
| Microsoft Partner | delivering on the Microsoft Cloud |
| Chennai-based | trusted across APAC, EMEA, NA |
| 1 live case study | WindTrack — IoT in production |

### Layout
- 4-column grid (`lg:grid-cols-4 sm:grid-cols-2 gap-6`)
- Each card: `card-custom rounded-xl p-6 text-center`
- Large bold number (`.text-3xl font-extrabold text-swasthi-blue`)
- Small label below (`.text-sm text-gray-600`)
- Each card gets `reveal` with staggered delay via `transition-delay: calc(var(--i) * 0.1s)`
- Section wrapper: `bg-gray-50` (`section-alt`)

---

## 3. WindTrack Case Study Card Redesign

**Files:** `index.html`, `pages/industry-5-0.html`, `pages/use-cases.html`  
**Effort:** Medium · **Dependencies:** None

### New card layout (replaces current emoji + text card)
- Left column (lg:w-2/5): gradient banner `bg-gradient-to-br from-swasthi-blue to-blue-800` with large white metric text ("100 turbines · India-realistic zones")
- Right column (lg:w-3/5): headline, 1-paragraph summary, tech tags row, CTA buttons
- Tech tags: `Python`, `Streamlit`, `Plotly`, `IoT` — each as `.text-xs px-2.5 py-1 bg-swasthi-blue/10 text-swasthi-blue rounded-md font-medium`
- "Visit live dashboard" link remains prominent

---

## 4. Contact Form Enhancement

**File:** `pages/contact.html`  
**Effort:** Medium · **Dependencies:** Formspree account setup (done — endpoint provided)

### Form block (replaces `mailto:` dashed-border box)
```
POST to: https://formspree.io/f/mvzjbdon
Method:  POST
```

### Fields
| Field | Type | Required |
|---|---|---|
| First Name | text | Yes |
| Last Name | text | No |
| Work Email | email | Yes |
| Company | text | No |
| Service of Interest | select | No |
| Message | textarea | Yes |

### Service of Interest options
1. Enterprise AI Adoption
2. Microsoft Copilot & Cloud
3. Data Engineering & Big Data
4. Automation & AIOps
5. Security
6. Managed IT Services
7. General Inquiry

### Success state
- Show success message: "Thank you! We'll be in touch within one business day."
- Reset form

Keep existing: booking buttons section above form, "Other ways to reach us" sidebar, CTA banner below.

---

## 5. Footer Polish + "certified" → "deep" Fix

**Files:** All 18 HTML files (global footer block)  
**Effort:** High (18 files) · **Dependencies:** None

### Changes per footer block

**Add Legal column** (new column between Explore and Contact):
```html
<div>
  <h4 class="text-sm font-semibold text-swasthi-text mb-4">Legal</h4>
  <ul class="space-y-2.5 text-sm text-gray-600">
    <li><a href="#" class="hover:text-swasthi-blue">Privacy Policy</a></li>
    <li><a href="#" class="hover:text-swasthi-blue">Terms of Service</a></li>
    <li><a href="#" class="hover:text-swasthi-blue">Cookie Policy</a></li>
  </ul>
</div>
```
- Links to `#` with comment: `<!-- TODO: link to actual policy pages -->`

**Add social icons** — row at bottom of footer, right side of copyright line:
- LinkedIn, Twitter/X, Facebook as inline SVGs (18×18, gray-500, hover → swasthi-blue)
- Same `transition: color 0.2s` as other links

### "certified" → "deep" fix
- Search across all 18 pages for "certified expertise"
- Replace with "deep expertise"
- Appears in: About page + Global Reach section (Home + About)

---

## 6. Section Background Alternation

**Files:** `css/style.css` + all page HTML files  
**Effort:** Medium · **Dependencies:** None

### CSS addition
```css
.section-alt {
  background-color: #F9FAFB; /* Tailwind gray-50 */
}
```

### Home page section rhythm
| Section | Background |
|---|---|
| Hero | `bg-white` (default) |
| Pillar cards | `section-alt` |
| WindTrack | `bg-white` |
| Stats strip | `section-alt` |
| Global Reach | `bg-white` |
| CTA | `#0AA0E4` (blue, existing) |
| Footer | `bg-white` |

### Solution pages rhythm
| Section | Background |
|---|---|
| Hero | `bg-white` |
| "How we help" cards | `section-alt` |
| CTA | `#0AA0E4` |
| Footer | `bg-white` |

---

## 7. Scroll-to-Top Button

**File:** `index.html` + `js/main.js` + `css/style.css`  
**Effort:** Low · **Dependencies:** None

### HTML (before `</body>`)
```html
<button id="scroll-top" aria-label="Scroll to top"
  class="fixed bottom-6 right-6 w-10 h-10 rounded-full bg-swasthi-blue text-white shadow-lg flex items-center justify-center opacity-0 pointer-events-none transition-opacity duration-300 z-50">
  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"/>
  </svg>
</button>
```

### JS (`main.js`)
```js
const scrollBtn = document.getElementById('scroll-top');
if (scrollBtn) {
  window.addEventListener('scroll', () => {
    const show = window.scrollY > 500;
    scrollBtn.classList.toggle('opacity-0', !show);
    scrollBtn.classList.toggle('pointer-events-none', !show);
  });
  scrollBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}
```

---

## 8. Microsoft Partner Badge Enhancement

**Files:** All HTML files  
**Effort:** Medium · **Dependencies:** High-res logo from Surya

### Home page trust signal row
- New section below hero: centered row with "Microsoft Partner" badge + brief text
- Layout: flex items-center justify-center gap-4
- Only add if/when Surya provides clean high-res logo

### Footer badge
- Current: `h-14 w-auto` — adequate size
- Add subtle border/background: `bg-gray-50 border border-gray-200 rounded-lg p-2`
- Keep placeholder comment

### Current state
- `assets/ms-partner-logo.jpeg` exists (WhatsApp-compressed per memory.md)
- Need Surya to generate clean version via Partner Center Logo Builder
- Until then: keep as-is with TODO comment reinforced

---

## 9. Agentic AI Use-Case Grid (DEFERRED)

**File:** `pages/enterprise-ai-adoption.html`  
**Status:** **DEFERRED** — waiting for uncle to confirm whether the use cases are real

Once confirmed, add a 4-column grid of industry use cases with [Aspire] hedging. Until then, skip.

---

## Implementation Order

```
Round 1 — High impact, low file count
  [1] Scroll animations         → 2 files
  [2] Stats strip               → 1 file
  [7] Scroll-to-top button       → 2 files
  [6] Section bg alternation     → 1 css + all pages

Round 2 — Medium impact, targeted
  [3] WindTrack card redesign    → 3 files
  [4] Contact form               → 1 file (Formspree endpoint ready)

Round 3 — High scope, global
  [5] Footer polish + fix        → 18 files (search-repeat patterns)
  [8] Partner badge              → 1 pass (needs logo from Surya)

Deferred
  [9] Agentic AI grid            → 1 file (waiting on uncle)
```

---

## File Change Summary

| File | Round |
|---|---|
| `css/style.css` | 1 |
| `js/main.js` | 1 |
| `index.html` | 1, 2, 3 |
| `pages/contact.html` | 2, 3 |
| `pages/industry-5-0.html` | 2, 3 |
| `pages/use-cases.html` | 2, 3 |
| `pages/enterprise-ai-adoption.html` | 3 |
| `pages/microsoft-copilot-cloud.html` | 3 |
| `pages/data-engineering-big-data.html` | 3 |
| `pages/automation-aiops.html` | 3 |
| `pages/security.html` | 3 |
| `pages/managed-it-services.html` | 3 |
| `pages/about.html` | 3 |
| `catalogue/*.py` | No change |
| `assets/*` | No change |
