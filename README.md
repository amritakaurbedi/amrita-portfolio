# Amrita Kaur Bedi — portfolio

Open `index.html` in a browser. No build step, no server needed.

## Files

```
index.html              one long homepage: hero, work, leadership, contact
applied-medical.html    \
petalgrip.html           |
laparoscopic-trainer.html > one detail page per project
suture-sensor.html       |
downing-lab.html        /
styles.css              all styling, commented, grouped by section
script.js               mobile nav, skill filter, footer year
assets/                 headshot, LinkedIn banner, resume PDF, fonts
```

## Things you should edit before this goes live

1. **"What I'm looking for" (contact section, `index.html`).** I wrote *Summer 2027
   internship* and three areas you're targeting. That's my guess from your resume —
   change it to what's actually true. This is the most important sentence on the page
   for a recruiter, so it should be your words.
2. **The "Context" paragraph on each project page.** One paragraph per project,
   explaining why the work mattered. I wrote these from your resume bullets, so they're
   accurate but general. You know the real reason each project existed — say it.
3. **The "Ask me about…" line** in the sidebar of each project page. These are meant to
   be conversation starters in an interview. Swap in whatever you'd actually want to
   be asked.
4. **Add images.** The project pages have room for them and will look thin until you do —
   CAD screenshots, prototype photos, a calibration curve, a stained cell image. Drop
   files in `assets/` and add `<img src="assets/your-file.jpg" alt="what it shows" />`
   inside a `<div class="case-block">`.

Everything else — bullets, dates, metrics, GPA — comes straight from your resume.

## Editing content

All project content lives in **one place**: the `PROJECTS` list at the top of
`data.py`, plus `build.py` which turns it into HTML. If you have Python, edit
`data.py` and run `python3 build.py` to regenerate every page at once.

If you'd rather not use Python, just edit the `.html` files directly — they're plain
HTML and nothing depends on the build script. Only remember that a project appears in
two places: the timeline card in `index.html` and its own detail page.

## Adding a new project

In `data.py`, copy an existing entry in `PROJECTS` and change the fields. `sort` is
`YYYY-MM` and controls timeline order (newest first). `skills` must use the keys
defined in `SKILL_GROUPS` at the top of the same file. Then run `python3 build.py`.

## The skill filter

Selecting skills keeps any project that uses **at least one** of them (not all of them),
so picking more skills shows more projects, not fewer. Matching skills get highlighted
inside each card. It's plain JavaScript in `script.js` — no libraries.

## Colours

The palette is sampled from your LinkedIn banner. Every colour is a variable at the top
of `styles.css`; change one there and it updates across all six pages.

| Variable  | Hex       | Used for                        |
|-----------|-----------|---------------------------------|
| `--cream` | `#fdefe2` | page background                 |
| `--white` | `#fffaf4` | alternating sections, cards     |
| `--plum`  | `#572c3d` | headings, buttons, contact band |
| `--coral` | `#d9634f` | the single accent               |
| `--rose`  | `#97576f` | small labels                    |
| `--gold`  | `#ba7a3a` | hairlines, timeline spine       |

## Fonts

Fraunces (headings) and IBM Plex Sans (body), both open-licence and stored in
`assets/fonts/`. They're self-hosted rather than loaded from Google, so the site works
offline and doesn't depend on an outside service.

## Publishing

Upload the whole folder to any static host — GitHub Pages, Netlify, Cloudflare Pages.
Nothing here needs a server.
