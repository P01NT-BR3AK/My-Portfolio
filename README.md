# Terrell — Portfolio Site

A Flask portfolio site showcasing the WedgeTail and LungVision projects,
built with an MVC structure.

## Structure

```
portfolio/
├── app.py                     # entry point — creates the Flask app
├── models/
│   └── project.py             # Project data model + in-memory project data
├── controllers/
│   └── main_controller.py     # Blueprint: routes -> models -> templates
├── templates/                 # views (Jinja2 + Bootstrap 5)
│   ├── base.html
│   ├── index.html
│   ├── project_detail.html
│   ├── about.html
│   └── 404.html
└── static/
    ├── css/style.css
    └── js/main.js
```

**Model** — `models/project.py` holds a `Project` class and the actual
content for WedgeTail and LungVision. No database is needed for a static
showcase, but this is exactly where you'd add persistence later
(e.g. swap the in-memory `PROJECTS` dict for SQLAlchemy models).

**View** — `templates/` renders the data. `base.html` holds the shared
nav/footer; the other templates extend it.

**Controller** — `controllers/main_controller.py` is a Flask Blueprint
that maps URLs to model lookups and view renders.

## Running it

```bash
pip install -r requirements.txt
python app.py
```

Then visit http://127.0.0.1:5000

## Routes

| Route                     | Page                          |
|----------------------------|-------------------------------|
| `/`                        | Home — hero + project grid    |
| `/projects/wedgetail`      | WedgeTail full writeup        |
| `/projects/lungvision`     | LungVision full writeup       |
| `/about`                   | About, skills, contact form   |

## Editing content

All project copy (summary, highlights, stats, limitations, timeline)
lives in `models/project.py` in the `PROJECTS` dict — edit it there,
no template changes needed.

## Next steps you might want

- Wire the contact form (`templates/about.html`) to a real backend route
  or email service — it currently just shows a placeholder message.
- Add project screenshots to `static/img/` and reference them in
  `project.py` / the templates.
- Deploy (e.g. Render, PythonAnywhere, Fly.io) once you're happy with
  the content.
