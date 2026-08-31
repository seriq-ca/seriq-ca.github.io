---
layout: default
ref: events
title: Events
description: "SERIQ meetings, along with the Centre's schools, workshops and seminars. The SEMTL meetings from 2019 to 2026 remain available online."
permalink: /en/events/
---

<div class="hero">
  <div class="wrap">
    <h1>Events</h1>
    <p class="lede">
      SERIQ meetings, along with the Centre's schools, workshops and seminars.
    </p>
  </div>
</div>

<section class="band band--paper">
  <div class="wrap">
    <h2>Meetings</h2>
    {%- assign events = site.events | where_exp: "e", "e.lang == page.lang" | sort: "event_date" | reverse -%}
    {%- assign by_year = events | group_by_exp: "e", "e.event_date | date: '%Y'" -%}
    {%- for year in by_year %}
    <h3 class="year">{{ year.name }}</h3>
    <ol class="event-list">
      {%- for e in year.items %}
      <li>
        <p class="name"><a href="{{ e.url | relative_url }}" lang="fr">{{ e.title }}</a></p>
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
    <h2>Before SERIQ</h2>
    <p>
      Meetings held under the SEMTL banner, from 2019 to 2026, remain available at
      their original addresses.
    </p>
    <p><a href="https://semtl.github.io/">SEMTL archive</a></p>
  </div>
</section>
