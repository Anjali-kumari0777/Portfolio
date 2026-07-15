"""
Anjali Kumari — Portfolio
FastAPI + Jinja2 + Bootstrap

Run locally:
    pip install -r requirements.txt
    uvicorn app.main:app --reload
Open: http://127.0.0.1:8000
"""

import json
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from pathlib import Path
from datetime import date

BASE_DIR = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Site-wide constants — update these if you ever change domain / photo
# ---------------------------------------------------------------------------
SITE_URL   = "https://anjali-kumari.dev"          # change to your real domain
SITE_NAME  = "Anjali Kumari — Software Engineer"
OG_IMAGE   = f"{SITE_URL}/static/images/profile.jpg"
TWITTER_HANDLE = ""   # add "@handle" if you have one


# ---------------------------------------------------------------------------
# Security-headers middleware
# ---------------------------------------------------------------------------
class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Adds industry-standard HTTP security headers to every response.

    X-Content-Type-Options      → stops browsers sniffing MIME types
    X-Frame-Options             → blocks clickjacking (embedding in iframes)
    X-XSS-Protection            → legacy XSS filter (old IE/Edge)
    Referrer-Policy             → controls how much URL info leaks on links
    Permissions-Policy          → disables browser features we don't need
    Content-Security-Policy     → whitelist of allowed resource origins
    Strict-Transport-Security   → force HTTPS once the site is on HTTPS
    """
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"]  = "nosniff"
        response.headers["X-Frame-Options"]         = "DENY"
        response.headers["X-XSS-Protection"]        = "1; mode=block"
        response.headers["Referrer-Policy"]          = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"]       = (
            "camera=(), microphone=(), geolocation=(), payment=()"
        )
        response.headers["Content-Security-Policy"]  = (
            "default-src 'self'; "
            "script-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; "
            "style-src  'self' https://cdn.jsdelivr.net https://fonts.googleapis.com 'unsafe-inline'; "
            "font-src   'self' https://fonts.gstatic.com https://cdn.jsdelivr.net; "
            "img-src    'self' data:; "
            "connect-src 'self'; "
            "frame-ancestors 'none';"
        )
        # Enable HSTS only on production (when the site is HTTPS)
        response.headers["Strict-Transport-Security"] = (
            "max-age=63072000; includeSubDomains; preload"
        )
        return response


# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
app = FastAPI(
    title=SITE_NAME,
    docs_url=None,      # hide /docs on a public portfolio
    redoc_url=None,     # hide /redoc
    openapi_url=None,   # hide /openapi.json — no need to expose API schema
)

app.add_middleware(GZipMiddleware, minimum_size=500)   # compress responses
app.add_middleware(SecurityHeadersMiddleware)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


# ---------------------------------------------------------------------------
# Content data — edit here; no HTML changes needed
# ---------------------------------------------------------------------------
PROFILE = {
    "name":        "Anjali Kumari",
    "role":        "Software Engineer",
    "tagline":     "Backend & AI Engineer building data pipelines that don't break at 2 a.m.",
    "description": (          # used in meta description & JSON-LD
        "Software Engineer based in Noida with hands-on experience in Python, "
        "Django, FastAPI, Kafka, MongoDB, and AI/ML technologies. "
        "Building backend systems and AI-driven features for real-world products."
    ),
    "location":    "Sector 73, Noida, Uttar Pradesh, India",
    "email":       "anjali2004rai@gmail.com",
    "linkedin":    "https://www.linkedin.com/in/anjali-kumari-ak0777",
    "github":      "https://github.com/Anjali-kumari0777",
    "photo":       "/static/images/profile.jpg",
    "photo_abs":   OG_IMAGE,
    "site_url":    SITE_URL,
    "site_name":   SITE_NAME,
    "og_image":    OG_IMAGE,
    "twitter":     TWITTER_HANDLE,
}

EXPERIENCE = [
    {
        "company": "Moglix",
        "location": "Noida",
        "role":    "Software Engineer",
        "period":  "Jan 2026 — Present",
        "points": [
            "Build backend and AI features using Python, Django, FastAPI, SQL, BigQuery, MongoDB, Kafka, RAG, and Gemini.",
            "Design a multi-source PI (Proforma Invoice) validation analytics pipeline integrating Kafka, MySQL, and automated Excel reporting.",
            "Optimise query performance, response time, and processing speed across production services.",
            "Develop APIs and work with relational and NoSQL databases to ship AI-based features.",
        ],
    },
    {
        "company": "ConsultIT",
        "location": "Internship",
        "role":    "Python / Django Developer",
        "period":  "Nov 2023 — Dec 2023",
        "points": [
            "Worked on Python and Django-based backend tasks, building the foundation for later API and database work.",
        ],
    },
]

EDUCATION = [
    {
        "degree": "Master's of Computer Application (MCA)",
        "school": "Sharda University, Uttar Pradesh",
        "period": "2024 — 2026",
        "score":  "GPA: 9.5 / 10",
    },
    {
        "degree": "Bachelor's in Computer Application (BCA)",
        "school": "Netaji Subhas University, Jamshedpur",
        "period": "2021 — 2024",
        "score":  "CGPA: 8 / 10",
    },
]

PROJECTS = [
    {
        "name":        "TalentMatch",
        "tagline":     "AI-powered freelancer matching, built on semantic search.",
        "description": (
            "An AI-powered freelancer matching platform built with FastAPI and SQLite. "
            "Uses Sentence Transformers to generate embeddings and Qdrant for semantic "
            "search, matching project requirements with the right freelancer profiles "
            "based on skills and experience."
        ),
        "stack":  ["Python", "FastAPI", "SQLite", "Qdrant", "Sentence Transformers", "Semantic Search"],
        "github": "https://github.com/Anjali-kumari0777/TalentMatch",
        "icon":   "search",
    },
    {
        "name":        "Smart Home Automation System",
        "tagline":     "IoT control, energy monitoring, and ML-driven scheduling.",
        "description": (
            "An IoT-based system for remotely controlling appliances, monitoring "
            "energy usage, and scheduling device operations. Backend built in Django, "
            "integrated with ESP8266 hardware, with ML-driven analytics for smart "
            "energy management."
        ),
        "stack":  ["Python", "Django", "HTML/CSS/JS", "SQLite", "ESP8266", "Arduino/C++", "IoT"],
        "github": "https://github.com/Anjali-kumari0777/Smart_Home_Automation_system",
        "icon":   "cpu",
    },
    {
        "name":        "LinkedIn Web Scraper",
        "tagline":     "Automated profile extraction for recruitment analytics.",
        "description": (
            "A Python scraper that extracts profile information — job titles, "
            "companies, locations — and structures it into JSON for analysis. "
            "Automates data collection to support recruitment and professional "
            "profile analytics."
        ),
        "stack":  ["Python", "Selenium", "JSON"],
        "github": "https://github.com/Anjali-kumari0777/Linkedin-Webscrapdata",
        "icon":   "layers",
    },
]

SKILLS = {
    "Languages":      ["Python", "SQL"],
    "Web & APIs":     ["Django", "FastAPI", "DRF", "REST APIs", "HTML5", "CSS3", "Bootstrap", "JavaScript"],
    "Databases":      ["MySQL", "PostgreSQL", "SQLite", "MongoDB"],
    "AI & Agentic":   ["LangChain", "LangGraph", "OpenAI APIs", "RAG", "Qdrant", "AI Agents", "Prompt Engineering", "MCP"],
    "Data & Tools":   ["Pandas", "NumPy", "Matplotlib", "Kafka", "Power BI", "Git", "GitHub", "Docker"],
}

PIPELINE_STAGES = [
    {"label": "INGEST", "detail": "Python · Kafka"},
    {"label": "STORE",  "detail": "MySQL · MongoDB"},
    {"label": "REASON", "detail": "RAG · LangChain"},
    {"label": "SERVE",  "detail": "FastAPI · Django"},
]

# JSON-LD structured data for Google
JSON_LD = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Anjali Kumari",
    "jobTitle": "Software Engineer",
    "description": PROFILE["description"],
    "url": SITE_URL,
    "image": OG_IMAGE,
    "email": f"mailto:{PROFILE['email']}",
    "sameAs": [
        PROFILE["linkedin"],
        PROFILE["github"],
    ],
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "Noida",
        "addressRegion": "Uttar Pradesh",
        "addressCountry": "IN",
    },
    "alumniOf": [
        {
            "@type": "CollegeOrUniversity",
            "name": "Sharda University",
        },
        {
            "@type": "CollegeOrUniversity",
            "name": "Netaji Subhas University",
        },
    ],
    "knowsAbout": [
        "Python", "FastAPI", "Django", "Kafka", "MongoDB",
        "Machine Learning", "RAG", "LangChain", "Data Engineering",
    ],
}

# Sitemap entries
SITEMAP_URLS = [
    {"loc": SITE_URL, "priority": "1.0", "changefreq": "monthly"},
]


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "profile":         PROFILE,
            "experience":      EXPERIENCE,
            "education":       EDUCATION,
            "projects":        PROJECTS,
            "skills":          SKILLS,
            "pipeline_stages": PIPELINE_STAGES,
            "json_ld_str":     json.dumps(JSON_LD, indent=2, ensure_ascii=False),
        },
    )


@app.get("/robots.txt", response_class=Response)
async def robots():
    """
    Tells search-engine crawlers which pages to index.
    Allow everything, point to sitemap.
    """
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n"
    )
    return Response(content=content, media_type="text/plain")


@app.get("/sitemap.xml", response_class=Response)
async def sitemap():
    """
    XML sitemap — helps Google discover and rank your pages faster.
    """
    today = date.today().isoformat()
    urls_xml = "\n".join(
        f"""  <url>
    <loc>{u['loc']}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{u['changefreq']}</changefreq>
    <priority>{u['priority']}</priority>
  </url>"""
        for u in SITEMAP_URLS
    )
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls_xml}
</urlset>"""
    return Response(content=xml, media_type="application/xml")


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}
