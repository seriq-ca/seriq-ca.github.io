---
layout: default
ref: home
title: Accueil
event_date: 2026-10-29
event_time: de 15 h à 19 h
event_venue: Université de Montréal
---

<div class="hero">
  <div class="wrap">
    <h1>Structurer la recherche en génie logiciel au Québec</h1>
    <p class="lede">
      SERIQ réunit la communauté de recherche en génie logiciel autour des
      enjeux logiciels de la société numérique.
    </p>
  </div>
</div>

<section class="band band--feature">
  <div class="wrap">
    <div class="event">
      <p class="kicker">Rentrée SERIQ</p>
      <p class="when">{% include date.html date=page.event_date lang=page.lang weekday=true %}</p>
      <dl class="event-details">
        <dt>Heure</dt><dd>{{ page.event_time }}</dd>
        <dt>Lieu</dt><dd>{{ page.event_venue }}</dd>
      </dl>
      <p class="note">
        La rentrée marque la reprise des rencontres sous la bannière SERIQ,
        dans la continuité du réseau SEMTL et de ses plus de dix années
        d'activité.
      </p>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <h2>À propos</h2>
    <p>
      Le Centre interuniversitaire de recherche en génie logiciel pour la société
      numérique (SERIQ) est une initiative interuniversitaire qui s'inscrit dans la
      continuité du réseau <a href="https://semtl.github.io/">SEMTL</a>
      <i lang="en">(Software Engineering at Montreal)</i>
      et de ses plus de dix années d'activité. Il vise à structurer la recherche en
      génie logiciel à Montréal et au Québec.
    </p>
  </div>
</section>
