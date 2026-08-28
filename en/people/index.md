---
layout: default
ref: people
title: Members
permalink: /en/people/
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
    {%- assign members = site.data.members | sort: "name" -%}
    <ul class="member-list">
      {%- for m in members %}
      <li>
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
      Membership arrangements will be set out before the Centre's first meeting.
    </p>
  </div>
</section>
