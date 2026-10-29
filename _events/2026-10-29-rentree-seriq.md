---
ref: event-2026-10-29
title: Rentrée SERIQ
title_head: "Rentrée SERIQ · 29 octobre 2026"
description: "La rentrée de SERIQ, qui élargit le réseau de recherche SEMTL au génie logiciel pour la société numérique. Le 29 octobre 2026 de 16 h à 20 h à l'Université de Montréal. Conférences invitées, table ronde, présentation de SERIQ et réception de réseautage."
permalink: /evenements/2026-10-29-rentree-seriq/
event_date: 2026-10-29
event_time: de 16 h à 20 h
event_start: 2026-10-29T16:00:00-04:00
event_end: 2026-10-29T20:00:00-04:00
event_venue: Université de Montréal
event_building: Pavillon Jean-Coutu
event_room: S-1-111
event_street: 2940, chemin de Polytechnique
event_postcode: H3T 1J4
# Centre of the building, for the map on the page and the schema.org `geo`.
event_geo: [45.5001, -73.6153]
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

<section class="band band--feature">
  <div class="wrap">
    <div class="event event--page">
      <p class="kicker">Rencontre SERIQ</p>
      <h1 class="event-name">Rentrée SERIQ</h1>
      <p class="when">{% include date.html date=page.event_date lang=page.lang weekday=true %}</p>
      <dl class="event-details">
        <dt>Heure</dt><dd>{{ page.event_time }}</dd>
        <dt>Lieu</dt><dd>{{ page.event_venue }},<br><span class="room">{{ page.event_building }}</span>, <span class="room">local {{ page.event_room }}</span></dd>
        <dt>Langue</dt><dd>Bilingue (français et anglais)</dd>
      </dl>
      <p class="more">
        <a class="cta" href="{{ page.registration_url }}">S'inscrire</a>
        <span class="deadline">d'ici le {% include date.html date=page.registration_closes lang=page.lang %}</span>
      </p>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap wrap--gutter">
    <p>
      SERIQ élargit le réseau de recherche
      <a href="https://semtl.github.io/">SEMTL</a> et se consacre au génie
      logiciel pour la société numérique. Pour sa rentrée, nous invitons
      chercheur.e.s, étudiant.e.s, partenaires de l'industrie et
      représentant.e.s des institutions à des conférences invitées du milieu
      de la recherche comme de l'industrie, suivies d'une table ronde sur la
      recherche en logiciel pour la société. Suivront une
      présentation de l'histoire et de la portée de SERIQ par Benoit Baudry,
      des allocutions, puis une réception de réseautage autour d'affiches
      étudiantes.
    </p>
    <h2 class="programme-title">Programme</h2>
    <ol class="programme">
      <li>
        <p class="slot-time">15 h 45 – 16 h</p>
        <div class="slot-body">
          <h3>Accueil et inscription</h3>
          <p>Accueil des personnes inscrites.</p>
        </div>
      </li>
      <li>
        <p class="slot-time">16 h</p>
        <div class="slot-body">
          <h3>Mot d'ouverture</h3>
          <p>Mot de bienvenue et présentation de l'après-midi.</p>
        </div>
      </li>
      <li>
        <p class="slot-time">16 h 15 – 17 h 30</p>
        <div class="slot-body">
          <h3>Conférences invitées</h3>
          <p>Quatre invité.e.s du milieu de la recherche et de l'industrie exposent chacun.e leur vision de la recherche en logiciel en 15 minutes.</p>
          {% include speakers.html event=page.speakers %}
        </div>
      </li>
      <li>
        <p class="slot-time">17 h 30 – 18 h</p>
        <div class="slot-body">
          <h3>Pause</h3>
          <p>Une courte pause avant la table ronde.</p>
        </div>
      </li>
      <li>
        <p class="slot-time">18 h – 18 h 45</p>
        <div class="slot-body">
          <h3>Table ronde</h3>
          <p>Les conférencières et conférenciers discutent de <em>La recherche en logiciel pour la société : besoins et possibilités</em>.</p>
          {% include panel.html event=page.speakers moderator="Robillard, Martin" %}
        </div>
      </li>
      <li>
        <p class="slot-time">18 h 45 – 19 h 15</p>
        <div class="slot-body">
          <h3>Présentation de SERIQ</h3>
          <p>Benoit Baudry, directeur de SERIQ, en présente l'histoire et la portée. Suivent des allocutions de représentant.e.s des universités :</p>
          <ul class="rep-list">
            <li>
              <span class="portrait-sm"><img src="{{ '/assets/img/speakers/bouchard.jpg' | relative_url }}" alt="" width="56" height="56" loading="lazy" decoding="async"></span>
              <span><a href="https://fas.umontreal.ca/faculte/direction-et-gouvernance/bureau-du-doyen/">Frédéric Bouchard</a>, doyen de la Faculté des arts et des sciences, Université de Montréal</span>
            </li>
            <li>
              <span class="portrait-sm"><img src="https://www.polymtl.ca/expertises/sites/expertises.lxpolywebprod.polymtl.ca/files/daria-camilla-boffito_1.jpg" alt="" width="56" height="56" loading="lazy" decoding="async" referrerpolicy="no-referrer"></span>
              <span><a href="https://www.polymtl.ca/expertises/boffito-daria-camilla">Daria Camilla Boffito</a>, directrice associée, recherche et soutien à la recherche, Polytechnique Montréal</span>
            </li>
            <li>
              <span class="portrait-sm"><img src="https://www.cs.mcgill.ca/media/professors/Pientka.jpg" alt="" width="56" height="56" loading="lazy" decoding="async" referrerpolicy="no-referrer"></span>
              <span><a href="https://www.cs.mcgill.ca/~bpientka/">Brigitte Pientka</a>, directrice de l'École d'informatique, Université McGill</span>
            </li>
            <li>
              <span class="portrait-sm"><img src="https://www.etsmtl.ca/uploads/_700xAUTO_fit_center-center_70_none/P20220119-Carter-Alan-002.jpg" alt="" width="56" height="56" loading="lazy" decoding="async" referrerpolicy="no-referrer" style="--zoom: 1.6; --focus: 96% 0%"></span>
              <span><a href="https://www.etsmtl.ca/etudier-a-lets/corps-enseignant/acarter">Alan Carter</a>, doyen de la recherche, ÉTS</span>
            </li>
          </ul>
        </div>
      </li>
      <li>
        <p class="slot-time">19 h 15 – 20 h</p>
        <div class="slot-body">
          <h3>Réception de réseautage</h3>
          <p>Avec environ 35 affiches de recherche étudiantes.</p>
        </div>
      </li>
    </ol>
    <p class="programme-more">
      <a class="cta" href="{{ page.registration_url }}">S'inscrire</a>
      <span>d'ici le {% include date.html date=page.registration_closes lang=page.lang %}</span>
    </p>
  </div>
</section>

<section class="band band--surface">
  <div class="wrap wrap--gutter">
    <h2>Accès</h2>
    <p>
      {{ page.event_building }}, local {{ page.event_room }}<br>
      {{ page.event_street }}, Montréal (Québec) {{ page.event_postcode }}
    </p>
    <p>
      Le pavillon est à quelques minutes à pied de la station de métro
      Université-de-Montréal (ligne bleue). Pour venir en voiture, l'UdeM décrit
      le <a href="https://di.umontreal.ca/services/stationnement/">stationnement
      pour visiteurs</a> et son <a href="https://plancampus.umontreal.ca/">plan du
      campus</a>.
    </p>
    {% include event-map.html title="Carte du pavillon Jean-Coutu" link="Ouvrir dans OpenStreetMap" %}
  </div>
</section>
