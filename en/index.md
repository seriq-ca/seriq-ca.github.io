---
layout: default
ref: home
title: Home
event_date: 2026-10-29
event_time: 3:00–7:00 p.m.
event_venue: Université de Montréal
---

<div class="hero">
  <div class="wrap">
    <h1 lang="fr">Centre interuniversitaire de recherche en génie logiciel pour la société numérique</h1>
    <p class="lede">
      SERIQ brings together Québec's software engineering research community
      around the software challenges of the digital society.
    </p>
  </div>
</div>

<section class="band">
  <div class="wrap">
    <div class="event">
      <p class="kicker" lang="fr">Rentrée SERIQ</p>
      <p class="when">{% include date.html date=page.event_date lang=page.lang weekday=true %}</p>
      <dl class="event-details">
        <dt>Time</dt><dd>{{ page.event_time }}</dd>
        <dt>Venue</dt><dd lang="fr">{{ page.event_venue }}</dd>
      </dl>
      <p>
        The <i lang="fr">rentrée</i> marks the return of the meeting series
        under the SERIQ banner, continuing the SEMTL network and its more than
        ten years of activity.
        <!-- TODO: building and room, programme, registration -->
      </p>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <h2>About</h2>
    <p>
      SERIQ is an inter-university research centre continuing the work of the
      SEMTL (Software Engineering at Montreal) network and its more than ten
      years of activity, structuring software engineering research in Montréal
      and across Québec. Its official name is
      French: <i lang="fr">Centre interuniversitaire de recherche en génie
      logiciel pour la société numérique</i>. SERIQ is an acronym and is not
      expanded in English.
    </p>
    <!-- TODO (PLAN.md §6.2): mission, governance, research axes, partner
         institutions. Do not publish an institution list before confirmation. -->
  </div>
</section>

<section class="band">
  <div class="wrap">
    <h2>SEMTL archive</h2>
    <p>
      The SEMTL network brought this community together for more than ten
      years. The meetings archived online, from 2019 to 2026, remain available
      at their original addresses; they are not reproduced here.
      <!-- Decision (PLAN.md §7): the archive stays on semtl.github.io. No URL
           changes, no redirects required. -->
    </p>
    <p><a href="https://semtl.github.io/">semtl.github.io</a></p>
  </div>
</section>
