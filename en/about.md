---
layout: default
ref: about
title: About
description: "The Centre's mission, its four research axes, its partner institutions, and the history from the SEMTL meetings to the SERIQ centre."
permalink: /en/about/
---

<div class="hero">
  <div class="wrap">
    <h1>About</h1>
    <p class="lede">
      SERIQ is an inter-university research centre in software engineering. It
      continues the SEMTL meetings, held in Montréal for more than ten years.
    </p>
  </div>
</div>

<section class="band band--paper">
  <div class="wrap">
    <h2>Mission</h2>
    <p>
      The Centre develops software engineering research that supports the digital
      transformation of science and society. That research is organised around four
      complementary axes addressing the challenges of modern software development.
    </p>
    <p>
      The Centre has four partner institutions. Further universities may join the
      inter-university agreement.
    </p>
    <ul class="partner-logos">
      {%- for inst in site.data.institutions %}
      <li>
        <a href="{{ inst.url[page.lang] }}">
          <img class="partner-logo" src="{{ '/assets/img/institutions/' | append: inst.logo | relative_url }}"
               alt="{{ site.data.i18n[page.lang].institutions[inst.key] }}"
               width="{{ inst.width }}" height="{{ inst.height }}"
               style="--logo-h: {{ inst.height }}px"
               loading="lazy" decoding="async">
        </a>
        {%- if inst.faculties %}
        <p class="partner-faculty">
          {%- for f in inst.faculties %}
          <span>{{ site.data.i18n[page.lang].faculties[f] }}</span>
          {%- endfor %}
        </p>
        {%- endif %}
      </li>
      {%- endfor %}
    </ul>
    <p>The Centre's mission also covers the following:</p>
    <ul>
      <li>
        integrating the training of students and postdoctoral fellows into its
        scientific activities, and developing career prospects for early-career
        scientists;
      </li>
      <li>
        exchanging, collaborating and building lasting partnerships with the business
        community and the public sector;
      </li>
      <li>
        cooperating with other organisations working in human-centred
        interdisciplinary software research, in Canada and worldwide.
      </li>
    </ul>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    {%- include executive.html -%}
  </div>
</section>

<section class="band band--surface">
  <div class="wrap">
    <h2>Research axes</h2>
    <p>
      The four axes share a common foundation: software engineering — requirements,
      modelling, testing, integration, security.
    </p>
    <ol class="axes">
      <li data-label="Axis">
        <h3>{{ site.data.i18n[page.lang].axes.cps }}</h3>
        <p>
          Software is no longer confined to purely digital systems; it is embedded in
          physical, biological and social contexts. Digital twins, the internet of
          things, operating systems.
        </p>
      </li>
      <li data-label="Axis">
        <h3>{{ site.data.i18n[page.lang].axes.ecosystems }}</h3>
        <p>
          Software infrastructure now rests on shared platforms and heterogeneous
          supply chains. Software supply chain, cloud and high-performance computing,
          product lines.
        </p>
      </li>
      <li data-label="Axis">
        <h3>{{ site.data.i18n[page.lang].axes.design }}</h3>
        <p>
          Designing a system does not rest on computing expertise alone; it also
          involves domain specialists. Low-code, domain-specific modelling,
          requirements engineering.
        </p>
      </li>
      <li data-label="Axis">
        <h3>{{ site.data.i18n[page.lang].axes.human }}</h3>
        <p>
          People remain at the centre of software systems, as users, operators and
          designers. Accessibility, human-computer interaction, documentation.
        </p>
      </li>
    </ol>

    <h2>Cross-cutting axes</h2>
    <p>
      Four concerns run across the four axes rather than belonging to any one of
      them.
    </p>
    <ul class="cross-axes">
      <li>
        <h3>AI</h3>
        <ul>
          <li>AI for software engineering</li>
          <li>Software engineering for AI</li>
        </ul>
      </li>
      <li>
        <h3>Application domains</h3>
        <ul>
          <li>Science</li>
          <li>Finance</li>
          <li>Transport</li>
          <li>Infrastructure</li>
          <li>Civil society</li>
          <li>Culture</li>
          <li>Industry</li>
          <li>Health</li>
          <li>Aerospace</li>
        </ul>
      </li>
      <li>
        <h3>Concerns and qualities</h3>
        <ul>
          <li>Security</li>
          <li>Reliability</li>
          <li>Adaptability</li>
          <li>Performance</li>
          <li>Sovereignty</li>
          <li>Transparency</li>
        </ul>
      </li>
      <li>
        <h3>Knowledge transfer</h3>
        <ul>
          <li>Scientific audiences</li>
          <li>Industrial audiences</li>
          <li>Governments</li>
          <li>General public</li>
        </ul>
      </li>
    </ul>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <h2>From SEMTL meetings to the SERIQ centre</h2>
    <p>
      SEMTL (Software Engineering at Montreal) has brought together Montréal's
      software engineering research community for more than ten years. The online
      record begins in 2019: seven meetings that year, then two in early 2020,
      before the pandemic interrupted them.
    </p>
    <p>
      Meetings resumed in August 2022, roughly every two months. The six Montréal
      universities have hosted and supported them in turn, and some have been held
      alongside conferences such as
      <a href="{{ '/semtl/2025-04-27-icse/' | relative_url }}">ICSE</a> and
      <a href="{{ '/semtl/2026-06-03-polytechnique/' | relative_url }}">SEMLA</a>.
    </p>
    <p>
      Group discussions among SEMTL members also produced a vision paper, presented
      in the main track at
      <a href="{{ '/semtl/2024-09-27-models/' | relative_url }}">MODELS 2024</a>.
    </p>
    <p>
      In October 2026, SEMTL becomes SERIQ. The meeting series continues. The centre
      extends across Québec and organises its research around the four axes above.
    </p>
  </div>
</section>
