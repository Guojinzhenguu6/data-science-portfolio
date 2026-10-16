"""Regenerate the chart from data/interactive_daily.csv; preserve research outputs."""
import csv
from pathlib import Path
import plotly.graph_objects as go

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "data/interactive_daily.csv").open(newline="") as handle:
    rows = list(csv.DictReader(handle))
assert len(rows) == 1087 and len({r['date'] for r in rows}) == len(rows)
fig = go.Figure()
for year, color in [("2022", "#256C98"), ("2023", "#B55D32"), ("2024", "#39845A")]:
    subset = [r for r in rows if r['date'].startswith(year)]
    x, y = [float(r['precip_mm']) for r in subset], [float(r['crossings']) for r in subset]
    assert all(v >= 0 for v in x + y)
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=year,
        marker=dict(color=color, size=7, opacity=0.65),
        customdata=[[r['date'], float(r['temp_mid_c'])] for r in subset],
        hovertemplate='Date: %{customdata[0]}<br>Precipitation: %{x:.1f} mm<br>Crossings: %{y:,.0f}<br>Temperature midpoint: %{customdata[1]:.1f} °C<extra>%{fullData.name}</extra>'))
buttons = [dict(label='All years', method='update', args=[{'visible':[True]*3}])]
for i, year in enumerate(['2022','2023','2024']):
    buttons.append(dict(label=year, method='update', args=[{'visible':[j==i for j in range(3)]}]))
fig.update_layout(title=dict(text='Daily precipitation and Fremont Bridge crossings',font=dict(size=18)),
    template='plotly_white', autosize=True, height=560, margin=dict(l=65,r=20,t=110,b=65),
    xaxis=dict(title='Daily precipitation (mm)',rangemode='tozero'),
    yaxis=dict(title='Recorded crossings per day',rangemode='tozero'),
    legend=dict(title=dict(text='Year'),orientation='h',y=1.10,x=0),
    updatemenus=[dict(buttons=buttons,direction='down',x=1,xanchor='right',y=1.15,yanchor='top',showactive=True)],
    hovermode='closest',font=dict(family='Arial, sans-serif',size=13))
chart = fig.to_html(full_html=False, include_plotlyjs=True, div_id='precipitation-crossings',
    config=dict(responsive=True,displaylogo=False,scrollZoom=False,
                toImageButtonOptions=dict(filename='fremont_precipitation_crossings')))
html = '''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Interactive precipitation and crossings | Fremont Bridge</title>
<style>body{margin:0;padding:12px;font:14px/1.5 Arial,sans-serif;color:#193e5a}p{margin:8px 12px}.plotly-graph-div{width:100%}</style>
</head><body><p>Explore 1,087 usable days (2022–2024). Hover for date and values; choose a year,
click legend entries to toggle series, or use the toolbar to zoom and reset.</p>''' + chart + '''
<p>Source: City of Seattle / SDOT crossing counts and NOAA / NCEI weather at Seattle–Tacoma Airport.
Raw daily observations; no causal effect is implied. Days excluded from the original primary analysis remain excluded here.</p>
</body></html>'''
output = ROOT / 'visualizations/precipitation_crossings.html'
output.parent.mkdir(parents=True,exist_ok=True)
output.write_text(html)
print(f'Built {output.name}: {len(rows)} observations, {output.stat().st_size:,} bytes')
