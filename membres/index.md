---
layout: default
ref: people
title: Membres
permalink: /membres/
---

{%- assign t = site.data.i18n[page.lang] -%}
<div class="hero">
  <div class="wrap">
    <h1>{{ t.nav.people }}</h1>
    <p class="lede">{{ t.people.lede }}</p>
  </div>
</div>

<section class="band band--paper">
  <div class="wrap">
    {%- assign members = site.data.members | where: "visible", true | sort: "name" -%}
    <ul class="member-list">
      {%- for m in members %}
      <li>
        {%- comment -%}
          Photos are self-hosted and lazy-loaded: they sit below the fold on every
          viewport, and the fixed width/height reserves the box so nothing shifts as
          they arrive. alt is empty because the name sits right beside the image.
        {%- endcomment -%}
        {%- if m.photo %}
        <img class="portrait" src="{{ '/assets/img/members/' | append: m.photo | relative_url }}"
             alt="" width="72" height="72" loading="lazy" decoding="async">
        {%- else %}
        <span class="portrait portrait--empty" aria-hidden="true"></span>
        {%- endif %}
        <div class="member-text">
          <p class="name">
            {%- if m.url %}<a href="{{ m.url }}">{{ m.name }}</a>{% else %}{{ m.name }}{% endif -%}
          </p>
          <p class="meta">
            {{- t.institutions[m.institution] -}}
            {%- if m.role %} · <span class="role">{{ t.people.roles[m.role] }}</span>{% endif -%}
          </p>
          {%- if m.axes and m.axes.size > 0 %}
          <ul class="member-axes">
            {%- for a in m.axes %}
            <li>{{ t.axes[a] }}</li>
            {%- endfor %}
          </ul>
          {%- endif %}
        </div>
      </li>
      {%- endfor %}
    </ul>
  </div>
</section>

<section class="band band--surface">
  <div class="wrap">
    <h2>{{ t.people.join_heading }}</h2>
    <p>
      Les modalités d'adhésion seront précisées d'ici la rentrée du Centre.
    </p>
  </div>
</section>
