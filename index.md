---
layout: home
title: Guo Jinzheng — Data Science Portfolio
---

# Turning observations into evidence

I am **Guo Jinzheng**, a student studying data science and data visualization at the University of Macau. I use Python to explore questions, check data quality and communicate findings through readable visualizations. This portfolio presents my current work and the limitations behind its conclusions.

**Technical skills:** Python · pandas · NumPy · Matplotlib · Jupyter Notebook · data cleaning · exploratory analysis · statistical modelling · Git and GitHub.

## Weather and micromobility crossings at Fremont Bridge

**Research question:** During 2022–2024, how are precipitation and temperature associated with recorded Fremont Bridge crossings after adjusting for calendar factors?

**Project status: ongoing.** The preliminary analysis is completed; further validation and model improvement are planned.

The project combines Seattle's public hourly crossing counts with NOAA airport weather observations. After checking completeness and data quality, 1,087 days remain for analysis. A negative-binomial model adjusts for calendar factors and uses a moving-block bootstrap for uncertainty.

**Read the result in context:** The purpose is to examine weather–crossing associations. The main finding is about 34.4% fewer expected crossings on days with at least 1 mm precipitation, after model adjustment. The key limitation is that a single-site observational comparison cannot prove causation.

![Four-panel visualization of daily bridge crossings, weather and adjusted count ratios](images/weather_crossings_dashboard.png)

**Main finding:** Days with at least 1 mm precipitation have an adjusted expected-count ratio of **0.656**, relative to days below 1 mm: approximately **34.4% fewer crossings**, with a 95% block-bootstrap interval of **0.619–0.693**. The adjusted comparison of 20°C with 15°C suggests about 9.6% more crossings. These are model-dependent associations.

![Model residuals and residual autocorrelation](images/model_diagnostics.png)

**What the second figure shows:** Residual autocorrelation remains, including about 0.326 at a one-day lag. A model can summarize an association while still leaving time patterns unexplained.

### Explore daily precipitation and crossings

This interactive scatter plot shows the **1,087 usable daily observations** in the original analysis. Each point represents one day: precipitation on the horizontal axis and recorded micromobility crossings on the vertical axis. Colours identify the year. Hover to see the date, precipitation, crossings and temperature midpoint; select a year or use the legend, and zoom to inspect overlapping points.

<iframe src="{{ '/visualizations/precipitation_crossings.html' | relative_url }}" title="Interactive scatter plot of daily precipitation and Fremont Bridge crossings" width="100%" height="710" loading="lazy" style="border:1px solid #dce4ea;border-radius:8px;"></iframe>

[Open the interactive chart in a full window]({{ '/visualizations/precipitation_crossings.html' | relative_url }}) · [Download the plotted daily data]({{ '/data/interactive_daily.csv' | relative_url }})

The point cloud shows substantial variation and generally fewer high-count days at larger precipitation amounts. This is an **unadjusted** view: calendar, temperature and other factors can also influence crossings. Use the model results above for adjusted comparisons. The chart was added in response to a classmate's suggestion to include interactive data visualization.

**Key limitation:** An observational study at one bridge cannot prove that weather causes changes in travel. Airport weather may differ from bridge conditions, counts include repeat crossings, and unmeasured events may influence results. These estimates are not a forecast for other locations.

[Explore the project, source permissions and reproduction instructions →](https://github.com/Guojinzhenguu6/data-science-project)

## What I will improve next

Evaluate performance on later time periods, inspect seasonal assumptions and compare additional locations when suitable public data are available.

## Sources and transparency

Data: [City of Seattle / SDOT](https://data.seattle.gov/d/65db-xm6k) and [NOAA / NCEI](https://www.ncei.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00024233/detail). Full snapshot provenance and permission notes are in the project README. Figures are calculated from these observations.

This is a student project and implies no government endorsement.
