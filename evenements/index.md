---
layout: default
ref: events
title: Événements
description: "Les rencontres SERIQ, ainsi que les écoles, ateliers et séminaires du Centre. Les rencontres SEMTL de 2019 à 2026 demeurent consultables en ligne."
permalink: /evenements/
---

<div class="hero">
  <div class="wrap">
    <h1>Événements</h1>
    <p class="lede">
      Les rencontres SERIQ, ainsi que les écoles, ateliers et séminaires du Centre.
    </p>
  </div>
</div>

<section class="band band--paper">
  <div class="wrap">
    <h2>Rencontres</h2>
    {%- assign events = site.events | where_exp: "e", "e.lang == page.lang" | sort: "event_date" | reverse -%}
    {%- assign by_year = events | group_by_exp: "e", "e.event_date | date: '%Y'" -%}
    {%- for year in by_year %}
    <h3 class="year">{{ year.name }}</h3>
    <ol class="event-list">
      {%- for e in year.items %}
      <li>
        <p class="name"><a href="{{ e.url | relative_url }}">{{ e.title }}</a></p>
        <p class="meta">
          {% include date.html date=e.event_date lang=page.lang %}{% if e.event_venue %} · {{ e.event_venue }}{% endif %}
        </p>
      </li>
      {%- endfor %}
    </ol>
    {%- endfor %}
  </div>
</section>

<section class="band band--surface">
  <div class="wrap">
    <h2>Avant SERIQ</h2>
    <p>
      Les rencontres tenues sous la bannière SEMTL, de 2019 à 2026, demeurent
      consultables à leur adresse d'origine.
    </p>
    <p><a href="https://semtl.github.io/">Archives SEMTL</a></p>
  </div>
</section>
