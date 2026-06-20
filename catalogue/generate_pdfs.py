#!/tmp/pdf-venv/bin/python3
"""Generate Swasthi service catalogue PDFs matching the example style."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem,
    Table, TableStyle, PageBreak
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os, glob

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

BLUE = HexColor("#1F5FA8")
GOLD = HexColor("#D9A23D")
TEXT = HexColor("#2B2622")
GRAY = HexColor("#6B7280")
LIGHT_BG = HexColor("#F3F4F6")

styles = getSampleStyleSheet()

def make_style(name, parent='Normal', **kwargs):
    base = {
        'fontName': 'Helvetica',
        'fontSize': 10,
        'leading': 14,
        'textColor': TEXT,
        'spaceAfter': 6,
    }
    base.update(kwargs)
    return ParagraphStyle(name, parent=styles[parent], **base)

s_title = make_style('s_title', fontSize=24, leading=30, textColor=BLUE, spaceAfter=2, fontName='Helvetica-Bold')
s_subtitle = make_style('s_subtitle', fontSize=11, leading=14, textColor=GOLD, spaceAfter=14, fontName='Helvetica-Bold')
s_heading = make_style('s_heading', fontSize=16, leading=20, textColor=TEXT, spaceAfter=8, fontName='Helvetica-Bold')
s_body = make_style('s_body', fontSize=10, leading=15, textColor=TEXT, spaceAfter=10)
s_section = make_style('s_section', fontSize=11, leading=15, textColor=BLUE, spaceAfter=4, spaceBefore=12, fontName='Helvetica-Bold')
s_bullet_title = make_style('s_bullet_title', fontSize=10, leading=14, textColor=TEXT, fontName='Helvetica-Bold')
s_bullet_desc = make_style('s_bullet_desc', fontSize=10, leading=14, textColor=TEXT, leftIndent=12)
s_footer = make_style('s_footer', fontSize=10, leading=14, textColor=GRAY, alignment=TA_CENTER, spaceBefore=20)
s_footer_tagline = make_style('s_footer_tagline', fontSize=9, leading=13, textColor=GRAY, alignment=TA_CENTER)
s_contact_line = make_style('s_contact_line', fontSize=9, leading=13, textColor=GRAY, alignment=TA_CENTER, spaceBefore=4)

def bullet(title, desc):
    """Return a paragraph: bold title, then normal description."""
    return Paragraph(
        f'<b>{title}</b><br/>{desc}',
        s_bullet_desc
    )

def section_block(services):
    """Build a list of flowables for a section."""
    items = []
    for s in services:
        items.append(bullet(s['title'], s['desc']))
    return items

# Catalogue content definitions
CATALOGUES = [
    {
        'filename': 'catalogue-enterprise-ai-adoption.pdf',
        'title': 'Enterprise AI Adoption',
        'desc': (
            'Helping organisations adopt AI safely and effectively — from strategy and readiness assessment '
            'through to production-grade custom model development and Copilot agent deployment. We focus on '
            'responsible AI governance as a starting condition, not an afterthought.'
        ),
        'proven': [
            {'title': 'AI Strategy & Readiness Assessment', 'desc': 'We assess your organisation\u2019s AI readiness and build a practical, prioritised adoption roadmap.'},
            {'title': 'Prototype Development', 'desc': 'We build working prototypes to validate AI use cases before committing to full-scale investment.'},
        ],
        'now': [
            {'title': 'Custom Model Development \u2014 Azure AI Foundry (RAG)', 'desc': 'We build retrieval-augmented generation solutions on Azure AI Foundry, grounding AI outputs in your own data.'},
            {'title': 'AI Governance & Responsible AI Frameworks', 'desc': 'We put governance frameworks in place from day one, so responsible AI is a starting condition, not a retrofit.'},
            {'title': 'Model Fine-Tuning', 'desc': 'We fine-tune models to your domain, your data, and your specific use case.'},
            {'title': 'Azure OpenAI Integration', 'desc': 'We integrate Azure OpenAI into your existing systems and day-to-day workflows.'},
        ],
        'aspire': [
            {'title': 'Production-Scale Copilot Studio Agent Deployment', 'desc': 'We\u2019re building toward full production-scale deployment of Copilot Studio agents across the enterprise \u2014 talk to us about your rollout roadmap.'},
            {'title': 'Enterprise-Wide AI Adoption Rollouts', 'desc': 'Talk to us about scaling AI adoption across your full organisation.'},
        ],
    },
    {
        'filename': 'catalogue-copilot-cloud.pdf',
        'title': 'Microsoft Copilot & Cloud',
        'desc': (
            'Deploying and optimising the Microsoft cloud stack \u2014 from M365 Copilot adoption and change '
            'management through to Azure infrastructure modernisation. We help organisations get the full '
            'value from their Microsoft investment, backed by certified Microsoft Partner expertise.'
        ),
        'proven': [
            {'title': 'Microsoft 365 Copilot Deployment', 'desc': 'We deploy Copilot for M365 with structured adoption and change management to drive real productivity gains.'},
            {'title': 'Azure Infrastructure Modernisation', 'desc': 'We migrate and modernise workloads on Azure (IaaS and PaaS), reducing cost and improving agility.'},
        ],
        'now': [
            {'title': 'Copilot for Dynamics 365', 'desc': 'AI assistants for sales, customer service, marketing, and supply chain \u2014 embedded in your business applications.'},
            {'title': 'Azure Virtual Desktop & Hybrid Workplace', 'desc': 'Secure, scalable virtual desktop infrastructure enabling flexible and hybrid work models.'},
            {'title': 'Microsoft 365 Governance & Tenant Optimisation', 'desc': 'We optimise your M365 tenant for security, compliance, and cost efficiency.'},
            {'title': 'Azure Landing Zones & Cloud Adoption Framework', 'desc': 'Structured cloud adoption guidance following Microsoft best practices for security, governance, and operations.'},
        ],
        'aspire': [
            {'title': 'Copilot for Sales / Service \u2014 Full Rollout', 'desc': 'We are building toward enterprise-wide Copilot for Sales and Service deployments, integrating AI into your CRM workflows.'},
        ],
    },
    {
        'filename': 'catalogue-data-engineering.pdf',
        'title': 'Data Engineering & Big Data',
        'desc': (
            'Building scalable, AI-ready data foundations \u2014 from pipeline engineering and real-time '
            'analytics through to modern data warehousing and governance. We treat data architecture as '
            'the critical enabler for every AI and analytics initiative.'
        ),
        'proven': [
            {'title': 'Data Pipeline Engineering', 'desc': 'We build reliable data pipelines using Azure Data Factory and Microsoft Fabric, moving data from source to insight.'},
            {'title': 'Power BI & Enterprise BI Architecture', 'desc': 'Semantic models, dashboards, and governed self-service BI that puts trusted data in the hands of decision-makers.'},
        ],
        'now': [
            {'title': 'Real-Time Analytics with Azure Stream Analytics', 'desc': 'Process streaming data from IoT devices, logs, and applications with low-latency analytics.'},
            {'title': 'Data Lake & Warehouse Modernisation', 'desc': 'Modernise legacy data platforms with Fabric Lakehouse and Synapse, reducing cost and unlocking new analytical capabilities.'},
            {'title': 'Data Governance & Cataloguing', 'desc': 'We implement Microsoft Purview for data discovery, lineage, classification, and policy enforcement.'},
            {'title': 'IoT Data Ingestion Pipelines', 'desc': 'Architected for WindTrack and adaptable to any industrial IoT use case \u2014 turbines, factory lines, grid sensors.'},
        ],
        'aspire': [
            {'title': 'End-to-End Modern Data Platform', 'desc': 'Full data platform transformations combining ingestion, storage, governance, analytics, and AI readiness \u2014 a multi-phased engagement.'},
        ],
    },
    {
        'filename': 'catalogue-automation-aiops.pdf',
        'title': 'Automation & AIOps',
        'desc': (
            'Automating workflows, IT operations, and AI model lifecycles \u2014 from Power Platform '
            'automation to AI-driven operations management and predictive maintenance. We are actively '
            'developing our MLOps and predictive MRO capability through the WindTrack roadmap.'
        ),
        'proven': [
            {'title': 'Power Automate & Power Apps Solutions', 'desc': 'We build automated workflows and low-code applications that eliminate manual, repetitive processes.'},
            {'title': 'Monitoring & Alerting Pipelines', 'desc': 'Automated infrastructure monitoring with intelligent alerting, reducing mean time to detection.'},
        ],
        'now': [
            {'title': 'AI-Powered IT Operations (AIOps)', 'desc': 'We apply AI to IT operations data \u2014 logs, metrics, events \u2014 to detect anomalies and reduce alert fatigue.'},
        ],
        'aspire': [
            {'title': 'MLOps \u2014 Model Lifecycle Management', 'desc': 'We are building MLOps capabilities for model versioning, monitoring, retraining, and governance. WindTrack\u2019s predictive MRO model will serve as our proving ground.'},
            {'title': 'Predictive Maintenance for Industrial Equipment', 'desc': 'WindTrack\u2019s next phase: an ML model that predicts component wear before failure, extending turbine life and reducing unplanned downtime. This approach extends to any industrial machinery.'},
        ],
    },
    {
        'filename': 'catalogue-security.pdf',
        'title': 'Security',
        'desc': (
            'Strengthening enterprise security posture using Microsoft\u2019s security portfolio \u2014 '
            'from threat protection and SIEM through to zero-trust architecture and compliance. We assess, '
            'design, and deploy security controls tailored to your risk profile.'
        ),
        'proven': [
            {'title': 'Security Posture Assessments', 'desc': 'We evaluate your current security posture against Microsoft best-practice frameworks and deliver a prioritised remediation roadmap.'},
        ],
        'now': [
            {'title': 'Microsoft 365 Defender Deployment', 'desc': 'Deploy and configure Defender for email, endpoint, identity, and cloud apps to strengthen your threat protection.'},
            {'title': 'Identity & Access Management (Entra ID)', 'desc': 'Design and implement identity governance, conditional access, and privileged identity management with Microsoft Entra ID.'},
        ],
        'aspire': [
            {'title': 'Azure Sentinel SIEM & SOAR', 'desc': 'We are building capability in Sentinel deployment, custom analytics, and automated incident response. Talk to us about your SIEM roadmap.'},
            {'title': 'Zero-Trust Architecture Implementation', 'desc': 'Full zero-trust transformations spanning identity, endpoints, networks, and data \u2014 scoped per engagement.'},
            {'title': 'Compliance & Data Protection (Purview)', 'desc': 'We are developing Purview-based compliance solutions for data classification, retention, and insider risk management.'},
        ],
    },
    {
        'filename': 'catalogue-managed-it.pdf',
        'title': 'Managed IT Services',
        'desc': (
            'The foundation Swasthi has built since 1993. Onsite IT support, infrastructure management, '
            'and modern endpoint management \u2014 delivered to real clients for over three decades. '
            'Proven, reliable, and evolving with technology.'
        ),
        'proven': [
            {'title': 'Backend Technical Support', 'desc': 'Onsite IT support, incident resolution, and SLA-backed emergency support \u2014 delivered to real clients since 1993.'},
            {'title': 'Network & Infrastructure Management', 'desc': 'Proactive monitoring and management of networks, servers, and critical infrastructure.'},
            {'title': 'Backup, Disaster Recovery & Business Continuity', 'desc': 'We design and manage backup and DR solutions that keep your business running through disruptions.'},
        ],
        'now': [
            {'title': 'Modern Endpoint Management', 'desc': 'Intune, Autopilot, and Windows 365 deployment for secure, cloud-managed device lifecycles.'},
            {'title': 'IT Strategy & Roadmap Consulting', 'desc': 'We help you plan your IT investments \u2014 from budgeting and vendor selection to technology roadmaps aligned with business goals.'},
            {'title': 'Vendor Management & Procurement', 'desc': 'Hardware, software, and licensing procurement with vendor negotiation and lifecycle management.'},
        ],
        'aspire': [
            {'title': 'Cloud-Based IT Service Desk', 'desc': 'We are developing a modern, cloud-hosted service desk platform with self-service portal, automated ticketing, and AI-assisted routing.'},
        ],
    },
    {
        'filename': 'catalogue-master.pdf',
        'title': 'Swasthi Computers \u2014 Service Catalogue',
        'desc': (
            'Swasthi Computers LLP is a Chennai-based Microsoft Partner with 30+ years of IT expertise. '
            'We deliver enterprise AI adoption, cloud modernisation, data engineering, automation, security, '
            'and managed IT \u2014 with a growing focus on Industry 5.0 and predictive MRO. '
            'This document provides a consolidated view of every service we offer.'
        ),
        'proven': [],
        'now': [],
        'aspire': [],
        'is_master': True,
    },
]

def build_pdf(data):
    filepath = os.path.join(OUTPUT_DIR, data['filename'])
    doc = SimpleDocTemplate(
        filepath,
        pagesize=A4,
        leftMargin=54, rightMargin=54,
        topMargin=54, bottomMargin=54,
    )
    story = []

    # ── Header ──
    story.append(Paragraph('SWASTHI COMPUTERS', s_title))
    story.append(Paragraph('SERVICE CATALOGUE', s_subtitle))
    story.append(Spacer(1, 4))

    # ── Title ──
    story.append(Paragraph(data['title'], s_heading))
    story.append(Paragraph(data['desc'], s_body))

    if data.get('is_master'):
        # Master catalogue: list all services in compact paragraphs
        services_list = [
            ('Enterprise AI Adoption', 'AI strategy, custom model development (Azure AI Foundry), RAG pipelines, Copilot Studio agents, governance frameworks, model fine-tuning, Azure OpenAI integration.'),
            ('Microsoft Copilot & Cloud', 'M365 Copilot deployment, Copilot for Dynamics 365, Azure modernisation, Azure Virtual Desktop, M365 governance, cloud adoption framework.'),
            ('Data Engineering & Big Data', 'Data pipelines (Azure Data Factory, Fabric), real-time analytics, lake/warehouse modernisation, Power BI, data governance (Purview), IoT data pipelines.'),
            ('Automation & AIOps', 'Power Automate & Power Apps, AIOps, MLOps, predictive maintenance MRO models, monitoring and alerting pipelines.'),
            ('Security', 'Security posture assessments, M365 Defender deployment, and Entra ID identity management — with emerging capability in Azure Sentinel SIEM/SOAR, zero-trust architecture, and compliance (Purview). Talk to us about your security roadmap.'),
            ('Managed IT Services', 'Helpdesk support, network/infrastructure management, backup & DR, Intune/Autopilot, IT strategy consulting, vendor management.'),
        ]
        for name, desc in services_list:
            story.append(Spacer(1, 6))
            story.append(Paragraph(f'<b>{name}</b>', ParagraphStyle('svc', parent=s_body, spaceAfter=2, fontName='Helvetica-Bold')))
            story.append(Paragraph(desc, s_bullet_desc))

        # WindTrack
        story.append(Spacer(1, 8))
        story.append(Paragraph('<b>Flagship: WindTrack \u2014 IoT Wind Turbine Monitoring</b>', ParagraphStyle('wt', parent=s_body, spaceAfter=2, fontName='Helvetica-Bold')))
        story.append(Paragraph(
            'A live-deployed IoT proof of concept simulating 100 turbines across India-realistic wind zones '
            '(Tamil Nadu, Gujarat, Maharashtra, Rajasthan, Karnataka). Real-time asset and power generation '
            'dashboards. Next phase: predictive MRO model for component wear detection.',
            s_bullet_desc
        ))

    else:
        # ── PROVEN ──
        if data['proven']:
            story.append(Paragraph('PROVEN', s_section))
            story.extend(section_block(data['proven']))

        # ── NOW ──
        if data['now']:
            story.append(Paragraph('NOW', s_section))
            story.extend(section_block(data['now']))

        # ── ASPIRE ──
        if data['aspire']:
            story.append(Paragraph('ASPIRE', s_section))
            story.extend(section_block(data['aspire']))

    # ── Footer ──
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        'Ready to start your AI adoption journey?',
        s_footer
    ))
    story.append(Paragraph(
        'Swasthi Computers LLP &nbsp;|&nbsp; swasthicomputers.com &nbsp;|&nbsp; info@swasthicomputers.com &nbsp;|&nbsp; Microsoft Partner',
        s_contact_line
    ))

    doc.build(story)
    return filepath

# Generate all
print("Generating catalogue PDFs...")
for cat in CATALOGUES:
    path = build_pdf(cat)
    size = os.path.getsize(path)
    print(f"  ✓ {os.path.basename(path)} ({size} bytes)")

print(f"\nAll {len(CATALOGUES)} PDFs generated in: {OUTPUT_DIR}")
