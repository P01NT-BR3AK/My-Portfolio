"""
freeze.py
Generates a static version of the site (into build/) using
Frozen-Flask, so it can be hosted on GitHub Pages with no server.

Run manually with: python freeze.py
This also runs automatically in the GitHub Actions workflow
(.github/workflows/deploy.yml) on every push to main.
"""

from flask_frozen import Freezer
from app import app
from models.project import get_all_projects

# Serve pages via relative links (needed because GitHub Pages serves
# project sites from a subpath like username.github.io/repo-name/,
# not from the domain root).
app.config["FREEZER_RELATIVE_URLS"] = True
app.config["FREEZER_DESTINATION"] = "build"

freezer = Freezer(app)


@freezer.register_generator
def project_urls():
    # Tells Frozen-Flask which dynamic /projects/<slug> URLs exist,
    # since it can't discover them by crawling alone. Endpoint name
    # must include the blueprint prefix ("main.").
    for project in get_all_projects():
        yield "main.project_detail", {"slug": project.slug}


if __name__ == "__main__":
    freezer.freeze()
    print("Static site built into ./build")
