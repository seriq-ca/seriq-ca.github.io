---
ref: event-2026-10-29
title: Rentrée SERIQ
title_head: "Rentrée SERIQ · 29 octobre 2026"
description: "La rentrée de SERIQ, qui élargit le réseau de recherche SEMTL au génie logiciel pour la société numérique. Le 29 octobre 2026 de 15 h à 19 h à l'Université de Montréal. Conférences invitées, table ronde, présentation de SERIQ et réception de réseautage."
permalink: /evenements/2026-10-29-rentree-seriq/
event_date: 2026-10-29
event_time: de 15 h à 19 h
event_start: 2026-10-29T15:00:00-04:00
event_end: 2026-10-29T19:00:00-04:00
event_venue: Université de Montréal
registration_url: https://event.fourwaves.com/seriq-rentree
# Registration window, emitted as the Offer `validFrom`/`validThrough` in
# _includes/schema.html. Times are EDT (-04:00); both dates fall inside
# daylight time, so neither needs the -05:00 winter offset.
registration_opens: 2026-09-02T09:30:00-04:00
registration_closes: 2026-10-23T17:00:00-04:00
# Basename of the file under _data/speakers/. Read by _includes/speakers.html
# for the cards and by _includes/schema.html for the Event `performer` list.
speakers: rentree-2026
name_lang: fr
summary: >-
  SERIQ élargit le réseau de recherche SEMTL au génie logiciel pour la
  société numérique. Sa rentrée réunit la communauté autour de conférences
  invitées, d'une table ronde et d'une réception.
---

<div class="hero">
  <div class="wrap">
    <p class="kicker">Rencontre SERIQ</p>
    <h1>Rentrée SERIQ</h1>
    <p class="lede">
      SERIQ élargit le réseau de recherche
      <a href="https://semtl.github.io/">SEMTL</a> et se consacre au génie
      logiciel pour la société numérique. Pour sa rentrée, nous invitons
      chercheur.e.s, étudiant.e.s, partenaires de l'industrie et
      représentant.e.s des institutions à un après-midi de conférences
      invitées du milieu de la recherche comme de l'industrie, suivies d'une
      table ronde sur la recherche en logiciel pour la société. Suivront une
      présentation de l'histoire et de la portée de SERIQ par Benoit Baudry,
      des allocutions, puis une réception de réseautage autour d'affiches
      étudiantes.
    </p>
  </div>
</div>

<section class="band band--feature">
  <div class="wrap">
    <div class="event">
      <p class="when">{% include date.html date=page.event_date lang=page.lang weekday=true %}</p>
      <dl class="event-details">
        <dt>Heure</dt><dd>{{ page.event_time }}</dd>
        <dt>Lieu</dt><dd>{{ page.event_venue }}</dd>
        <dt>Langue</dt><dd>Bilingue (français et anglais)</dd>
        <dt>Inscription</dt><dd>d'ici le {% include date.html date=page.registration_closes lang=page.lang %}</dd>
      </dl>
      <p class="note">
        Le pavillon et le local seront précisés d'ici la rencontre.
      </p>
      <p class="more">
        <a class="cta" href="{{ page.registration_url }}">S'inscrire</a>
      </p>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <h2>Programme</h2>
    <ul>
      <li>
        <strong>15 h</strong> Mot d'ouverture.
      </li>
      <li>
        <strong>15 h 15 – 16 h 30</strong> Conférences invitées, du milieu de la
        recherche comme de l'industrie. Chaque invité.e expose sa vision de la
        recherche en logiciel en 15 minutes :
        {% include speakers.html event=page.speakers %}
      </li>
      <li>
        <strong>16 h 30 – 17 h</strong> Pause.
      </li>
      <li>
        <strong>17 h – 17 h 45</strong> Table ronde, <em>La recherche en logiciel
        pour la société : besoins et possibilités</em>, où les conférencières et
        conférenciers discutent plus largement des sujets abordés.
      </li>
      <li>
        <strong>17 h 45 – 18 h 15</strong> L'histoire et la portée de SERIQ, par
        son directeur Benoit Baudry, suivies d'allocutions de doyen.ne.s et
        d'autres représentant.e.s (à confirmer).
      </li>
      <li>
        <strong>18 h 15 – 19 h</strong> Réception de réseautage, avec des affiches
        étudiantes.
        <ul>
          <li>
            Les étudiant.e.s peuvent proposer une affiche avec le
            <a href="https://forms.gle/jUGuScfx11nuFTti7">formulaire de soumission</a>
            d'ici le 9 octobre 2026.
          </li>
        </ul>
      </li>
    </ul>
  </div>
</section>
