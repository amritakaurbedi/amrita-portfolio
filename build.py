# -*- coding: utf-8 -*-
"""Generate index.html and one detail page per project from data.py."""
import os, html
from data import PROJECTS, SKILL_GROUPS, SKILL_NAMES, LEAD_SKILLS

OUT = os.path.dirname(os.path.abspath(__file__))
EMAIL = "amritabedi27@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/amritakaurbedi"
RESUME = "assets/Amrita_Kaur_Bedi_Resume.pdf"

e = html.escape


def head(title, desc, rel=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="preload" href="{rel}assets/fonts/Fraunces-SOFTWONKopszwght.woff2" as="font" type="font/woff2" crossorigin />
<link rel="preload" href="{rel}assets/fonts/IBMPlexSans-wdthwght.woff2" as="font" type="font/woff2" crossorigin />
<link rel="stylesheet" href="{rel}styles.css" />
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def header(home=True):
    p = "" if home else ""
    base = "index.html"
    return f"""<header class="site-header">
  <nav class="nav container" aria-label="Primary">
    <a class="brand" href="{base}">Amrita Kaur Bedi</a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-links" aria-label="Open navigation menu">
      <span></span><span></span><span></span>
    </button>
    <div class="nav-links" id="nav-links">
      <a href="{base}#industry">Industry Experience</a>
      <a href="{base}#work">Projects</a>
      <a href="{base}#leadership">Leadership and Involvement</a>
      <a class="resume-link" href="{RESUME}" target="_blank" rel="noopener">Resume (PDF)</a>
    </div>
  </nav>
</header>
"""


def footer():
    return f"""<footer class="footer">
  <div class="container footer-inner">
    <div class="footer-identity">
      <p>Amrita Kaur Bedi</p>
      <p>Biomedical Engineering, UC Irvine &middot; &copy; <span class="year"></span></p>
    </div>
    <div class="footer-links">
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
      <a href="{RESUME}" target="_blank" rel="noopener">Resume (PDF)</a>
    </div>
  </div>
</footer>
<script src="script.js"></script>
</body>
</html>
"""


def sub(p):
    # don't repeat the card title in the line underneath it
    if p["org"] == p["short"]:
        return e(p["role"])
    return f"{e(p['role'])} &middot; {e(p['org'])}"


def tags_html(skills, limit=None):
    picks = skills[:limit] if limit else skills
    out = "".join(
        f'<span class="tag" data-skill="{s}">{e(SKILL_NAMES[s])}</span>' for s in picks
    )
    extra = len(skills) - len(picks)
    if extra > 0:
        out += f'<span class="tag">+{extra}</span>'
    return f'<div class="tags">{out}</div>'


# ---------------------------------------------------------------- homepage
def build_index():
    work = [p for p in PROJECTS if not p.get("industry")]
    industry = [p for p in PROJECTS if p.get("industry")]

    # skills used only by an industry role (no filterable project) -> link out
    work_skills = {s for p in work for s in p["skills"]}
    goto = {}
    for p in industry:
        for s in p["skills"]:
            if s not in work_skills:
                goto.setdefault(s, f"{p['slug']}.html")
    for s in LEAD_SKILLS:
        if s not in work_skills:
            goto.setdefault(s, "#leadership")

    groups = ""
    for label, pairs in SKILL_GROUPS:
        chips = ""
        for k, v in pairs:
            attr = f' data-goto="{goto[k]}"' if k in goto else ""
            chips += (
                f'<button class="chip" type="button" aria-pressed="false" '
                f'data-skill="{k}"{attr}>{e(v)}</button>'
            )
        cls = "filter-group"
        if any(len(v) > 24 for _, v in pairs):
            cls += " filter-group--wide"
        groups += f'<div class="{cls}"><p>{e(label)}</p><div class="chips">{chips}</div></div>\n        '

    entries = ""
    for p in sorted(work, key=lambda x: x["sort"], reverse=True):
        entries += f"""
        <article class="entry" data-skills="{' '.join(p['skills'])}">
          <p class="entry-date">{e(p['dates'])}</p>
          <a class="entry-card" href="{p['slug']}.html">
            <p class="entry-kind">{e(p['kind'])}</p>
            <h3>{e(p['short'])}</h3>
            <p class="entry-org">{sub(p)}</p>
            <p>{e(p['summary'])}</p>
            {tags_html(p['skills'], 4)}
            <span class="entry-more">Read more</span>
          </a>
        </article>"""

    industry_meta = ""
    industry_html = ""
    for p in sorted(industry, key=lambda x: x["sort"], reverse=True):
        did = "".join(f"<li>{e(b)}</li>" for b in p["did"])
        industry_meta = f"{e(p['role'])} &middot; {e(p['dates'])}"
        skill_links = "".join(
            f'<span class="tag">{e(SKILL_NAMES[s])}</span>' for s in p["skills"]
        )
        industry_html += f"""
    <div class="lead-grid industry-grid">
      <div class="industry-photo">
        <img src="assets/applied-medical-amrita.png" alt="Amrita at the Applied Medical office" width="1050" height="1400" />
      </div>
      <div class="lead-copy">
        <ul class="lead-list">{did}</ul>
        <div class="tags">{skill_links}</div>
        <a class="entry-more" href="{p['slug']}.html">Read more</a>
      </div>
    </div>"""

    return (
        head(
            "Amrita Kaur Bedi &mdash; Biomedical Engineering",
            "Amrita Kaur Bedi, biomedical engineering student at UC Irvine. Medical device design, "
            "quality engineering, sensor development, and quantitative research.",
        )
        + header()
        + f"""<main id="main">

<section class="hero">
  <div class="hero-orbit orbit-one" aria-hidden="true"></div>
  <div class="hero-orbit orbit-two" aria-hidden="true"></div>
  <div class="container hero-grid">
    <div>
      <h1>Hi, I&rsquo;m Amrita.</h1>
      <p class="hero-role">What excites me most about engineering is the opportunity to make something better and see the impact it has on people.</p>
      <p class="hero-note">I love working with people just as much as I love solving technical problems, and I&rsquo;m especially drawn to projects where I can take ownership, collaborate across different perspectives, and turn an idea or challenge into something real. From medical device development and quality investigations to cancer research and student entrepreneurship, I&rsquo;m constantly looking for new ways to learn from others, understand healthcare challenges, and contribute to meaningful solutions.</p>
      <div class="hero-actions">
        <a class="button button-primary" href="#industry">View My Work</a>
        <a class="button button-secondary" href="{RESUME}" target="_blank" rel="noopener">Resume (PDF)</a>
      </div>
    </div>
    <div class="hero-visual">
      <div class="portrait-frame">
        <img src="assets/amrita-headshot.png" alt="Amrita Kaur Bedi" width="1035" height="1536" />
      </div>
    </div>
  </div>
  <div class="container">
    <dl class="facts">
      <div><dt>Degree</dt><dd>B.S. Biomedical Engineering</dd></div>
      <div><dt>Minors</dt><dd>Bioinformatics &middot; <span class="nowrap">Innovation &amp; Entrepreneurship</span></dd></div>
      <div><dt>Graduating</dt><dd>June 2028</dd></div>
    </dl>
  </div>
</section>

<section class="section lead-section industry-section" id="industry">
  <div class="container">
    <div class="work-head">
      <div>
        <h2>Applied Medical</h2>
        <p>{industry_meta}</p>
      </div>
    </div>
    {industry_html}
  </div>
</section>

<section class="section work-section" id="work">
  <div class="container">
    <div class="work-head">
      <div>
        <h2>Projects</h2>
        <p>Browse my projects from most recent to earliest, or filter by the skills you&rsquo;re interested in.</p>
      </div>
    </div>

    <details class="filter" data-filter open>
      <summary class="filter-top">
        <h3>Filter by skill</h3>
        <p class="filter-status"><span data-status aria-live="polite">Showing all {len(work)} projects</span><button class="filter-clear" type="button" data-clear hidden>Clear</button></p>
      </summary>
      <div class="filter-groups">
        {groups}
      </div>
    </details>

    <div class="track" data-track>{entries}
      <p class="track-empty" data-empty-msg hidden>No projects match that combination yet.</p>
    </div>
  </div>
</section>

<section class="section lead-section" id="leadership">
  <div class="container">
    <div class="lead-grid">
      <div class="lead-copy">
        <h2>MedTech Founders Program</h2>
        <p class="meta">Founder &amp; Project Coordinator &middot; BMES at UC Irvine &middot; 2025&ndash;present</p>
        <p class="measure">I started the MedTech Founders Program because undergraduates at UCI had plenty of ideas about healthcare and no structured route from an unmet need to a working prototype. It now runs as a mentored pipeline, and three of the teams have reached the semifinals of UCI entrepreneurship competitions.</p>
        <div class="metrics">
          <div><strong>20+</strong><span>students mentored from concept to prototype</span></div>
          <div><strong>50+</strong><span>undergraduates through the workshops</span></div>
          <div><strong>3</strong><span>teams into competition semifinals</span></div>
        </div>
      </div>
      <div>
        <ul class="lead-list">
          <li><b>Workshops</b> &mdash; ran SolidWorks, Arduino, and programming sessions to build design-for-manufacturability and rapid-prototyping skills across the chapter.</li>
          <li><b>Events</b> &mdash; coordinated cross-functional events putting 100+ students onto hands-on engineering projects.</li>
          <li><b>Side build</b> &mdash; designed a mobile app&ndash;controlled temperature probe with an ESP32, custom electronics, and a SolidWorks-modelled enclosure.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section dance-section">
  <div class="container">
    <div class="lead-grid">
      <div class="lead-copy">
        <h2>Kathak with UCI Avahita</h2>
        <p class="meta">Captain &middot; UCI Avahita Classical Dance &middot; 2024&ndash;present</p>
        <p class="measure">I&rsquo;ve trained in Kathak for years, and at UCI I captain Avahita, the classical dance team. We compete on the intercollegiate circuit &mdash; two second-place finishes this season and a place in the national top eight for Origins, the collegiate classical dance championship.</p>
        <div class="metrics">
          <div><strong>Top 8</strong><span>nationally at Origins</span></div>
          <div><strong>2&times;</strong><span>second place at qualifiers</span></div>
          <div><strong>8 min</strong><span>competition piece choreographed</span></div>
        </div>
      </div>
      <div>
        <ul class="lead-list">
          <li><b>Captain</b> &mdash; recruit and train new dancers and run rehearsals through the competitive season.</li>
          <li><b>Choreography</b> &mdash; built an eight-minute competition piece and taught it to the team.</li>
          <li><b>Competition</b> &mdash; placed 2nd at two qualifiers and reached the national top eight at Origins.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

</main>
"""
        + footer()
    )


# ------------------------------------------------------------ detail pages
def build_case(p, prev_p):
    did = "".join(f"<li>{e(b)}</li>" for b in p["did"])
    nxt = (
        f'<a class="button button-secondary" href="{prev_p["slug"]}.html">Next: {e(prev_p["short"])}</a>'
        if prev_p
        else f'<a class="button button-secondary" href="index.html#work">Back to all work</a>'
    )
    return (
        head(f"{e(p['short'])} &mdash; Amrita Kaur Bedi", e(p["summary"]))
        + header(home=False)
        + f"""<main id="main">

<section class="case-hero">
  <div class="container">
    <a class="back-link" href="index.html#work">&larr; All work</a>
    <p class="meta">{e(p['kind'])}</p>
    <h1>{e(p['title'])}</h1>
    <dl class="case-meta">
      <div><dt>Role</dt><dd>{e(p['role'])}</dd></div>
      <div><dt>Where</dt><dd>{e(p['org'])}</dd></div>
      <div><dt>When</dt><dd>{e(p['dates'])}</dd></div>
    </dl>
  </div>
</section>

<section class="case-body">
  <div class="container case-grid">
    <div>
      <div class="case-block">
        <h2>The short version</h2>
        <p class="lede">{e(p['summary'])}</p>
      </div>
      <div class="case-block">
        <h2>Context</h2>
        <p>{e(p['context'])}</p>
      </div>
      <div class="case-block">
        <h2>What I did</h2>
        <ul class="did">{did}</ul>
      </div>
    </div>
    <aside class="case-aside">
      <h3>Skills used</h3>
      {tags_html(p['skills'])}
      <p class="case-ask">{e(p['next'])}</p>
    </aside>
  </div>
</section>

<section class="case-next">
  <div class="container case-next-inner">
    <p>Want the one-page version? The resume has it.</p>
    <div class="hero-actions" style="margin:0">
      <a class="button button-primary" href="{RESUME}" target="_blank" rel="noopener">Resume (PDF)</a>
      {nxt}
    </div>
  </div>
</section>

</main>
"""
        + footer()
    )


def main():
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_index())
    ordered = sorted(
        [p for p in PROJECTS if not p.get("industry")],
        key=lambda x: x["sort"],
        reverse=True,
    )
    for i, p in enumerate(ordered):
        nxt = ordered[i + 1] if i + 1 < len(ordered) else None
        with open(os.path.join(OUT, f"{p['slug']}.html"), "w", encoding="utf-8") as f:
            f.write(build_case(p, nxt))
    for p in [p for p in PROJECTS if p.get("industry")]:
        with open(os.path.join(OUT, f"{p['slug']}.html"), "w", encoding="utf-8") as f:
            f.write(build_case(p, None))
    print("built:", ["index.html"] + [f"{p['slug']}.html" for p in PROJECTS])


if __name__ == "__main__":
    main()
