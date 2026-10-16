# Guo Jinzheng — Data Science Portfolio

Portfolio for CISC7204 Practice 09, built with GitHub Pages.

- [Live portfolio](https://Guojinzhenguu6.github.io/data-science-portfolio/)
- [Project repository](https://github.com/Guojinzhenguu6/data-science-project)
- Website entry: `index.md` in the root directory.
- Publish using Settings → Pages → Deploy from a branch → `main` → `/ (root)`.

This site showcases the existing Fremont Bridge preliminary analysis. Its status is ongoing.

## Update and publish

1. Edit `index.md` to update the introduction, skills or showcase.
2. Put calculated project figures in `images/`, then update their relative links.
3. Commit with a descriptive message and push to `main`.
4. Check the Pages deployment in Actions, open the live site and verify both images and the project link.
5. To reproduce the research, follow the project repository README; this repository contains the website only.

## Review and improvement process

The purpose, principal finding and limitation were reviewed with AI assistance. The review recommended placing these three points together before the first figure so a reader can identify them quickly. The website now includes a plain-language context paragraph before the visualization. This change is recorded in a descriptive commit. This review was conducted by AI, not a human classmate.

### Classmate feedback: interactive visualization

The student reported a classmate's suggestion to add interactive data visualization. In response, the portfolio embeds a Plotly scatter plot of daily precipitation against recorded micromobility crossings, with hover details, year selection, legend toggles, zoom/reset and image export. It uses all 1,087 usable days from the existing primary analysis. The original notebook, calculated results and static figures are preserved.

Commit message: `Add interactive visualization based on classmate feedback`.

## Rebuild the interactive chart

Use Python 3.12 and run from this repository root:

```sh
python -m pip install -r requirements-interactive.txt
python tools/build_interactive_chart.py
```

`data/interactive_daily.csv` contains date, precipitation, crossings and temperature midpoint copied from the [project's calculated daily data](https://github.com/Guojinzhenguu6/data-science-project/blob/main/results/analysis_daily.csv). Data sources and permissions are documented in the project README. The builder writes only `visualizations/precipitation_crossings.html`; it does not rerun the research analysis. The generated HTML bundles Plotly locally, avoiding an external script CDN. The website provides an embedded chart, a standalone chart link and a data download. The scatter plot shows unadjusted observations, not a causal effect or an adjusted model estimate.
