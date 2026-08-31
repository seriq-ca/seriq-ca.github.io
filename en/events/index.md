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

{%- comment -%}
  The include renders the next meeting and, because `include` shares this
  scope, leaves `next_event` and `t` behind for the past list below to use.
{%- endcomment -%}
{% include next-event.html %}

{%- assign events = site.events | where_exp: "e", "e.lang == page.lang" -%}
{%- assign past = "" | split: "" -%}
{%- for e in events -%}
  {%- unless next_event and e.url == next_event.url -%}
    {%- assign past = past | push: e -%}
  {%- endunless -%}
{%- endfor -%}
{%- if past.size > 0 %}
<section class="band band--paper">
  <div class="wrap">
    <h2>{{ t.events.past_heading }}</h2>
    {%- assign past = past | sort: "event_date" | reverse -%}
    {%- assign by_year = past | group_by_exp: "e", "e.event_date | date: '%Y'" -%}
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
{%- endif %}

<section class="band band--surface">
  <div class="wrap">
    <h2>Before SERIQ</h2>
    <p>
      Meetings held under the SEMTL banner, from 2019 to 2026, remain available at
      their original addresses.
    </p>
    {%- assign semtl = site.semtl | sort: "event_date" | reverse -%}
    {%- assign semtl_by_year = semtl | group_by_exp: "m", "m.event_date | date: '%Y'" -%}
    {%- for year in semtl_by_year %}
    <h3 class="year">{{ year.name }}</h3>
    <ol class="event-list event-list--archive">
      {%- for m in year.items %}
      <li>
        <p class="name"><a href="{{ m.url | relative_url }}" lang="en">{{ m.title }}</a></p>
        <p class="when">{% include date.html date=m.event_date lang=page.lang %}</p>
        {%- if m.event_venue or m.author %}
        <p class="where">{{ m.event_venue }}{% if m.event_venue and m.author %} · {% endif %}{{ m.author }}</p>
        {%- endif %}
      </li>
      {%- endfor %}
    </ol>
    {%- endfor %}
  </div>
</section>
