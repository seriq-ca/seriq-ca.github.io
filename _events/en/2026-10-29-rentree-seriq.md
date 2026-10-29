---
ref: event-2026-10-29
title: Rentrée SERIQ
title_head: "Rentrée SERIQ · October 29, 2026"
description: "The rentrée of SERIQ, which expands the SEMTL research network to software engineering for the digital society. October 29, 2026, from 4:00 to 8:00 p.m. at Université de Montréal. Guest talks, a panel, a presentation of SERIQ and a networking reception."
permalink: /en/events/2026-10-29-rentree-seriq/
event_date: 2026-10-29
event_time: 4:00–8:00 p.m.
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
  SERIQ expands the SEMTL research network to software engineering for the
  digital society. Its <i lang="fr">rentrée</i> brings the community
  together for guest talks, a panel and a reception.
---

<section class="band band--feature">
  <div class="wrap">
    <div class="event event--page">
      <p class="kicker">SERIQ meeting</p>
      <h1 class="event-name" lang="fr">Rentrée SERIQ</h1>
      <p class="when">{% include date.html date=page.event_date lang=page.lang weekday=true %}</p>
      <dl class="event-details">
        <dt>Time</dt><dd>{{ page.event_time }}</dd>
        <dt>Venue</dt><dd><span lang="fr">{{ page.event_venue }},<br><span class="room">{{ page.event_building }}</span></span>, <span class="room">room {{ page.event_room }}</span></dd>
        <dt>Language</dt><dd>Bilingual (French and English)</dd>
      </dl>
      <p class="more">
        <a class="cta" href="{{ page.registration_url }}">Register</a>
        <span class="deadline">by {% include date.html date=page.registration_closes lang=page.lang %}</span>
      </p>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap wrap--gutter">
    <p>
      SERIQ expands the <a href="https://semtl.github.io/">SEMTL</a> research
      network to work on software engineering for the digital society. For its
      <i lang="fr">rentrée</i>, we invite researchers, students, industry
      partners and institutional representatives to guest talks from research
      and industry, followed by a panel on software research for society.
      Benoit Baudry will then present the history and
      scope of SERIQ, followed by remarks, before a networking reception with
      student posters.
    </p>
    <h2 class="programme-title">Programme</h2>
    <ol class="programme">
      <li>
        <p class="slot-time">3:45–4:00 p.m.</p>
        <div class="slot-body">
          <h3>Registration</h3>
          <p>Check-in for registered attendees.</p>
        </div>
      </li>
      <li>
        <p class="slot-time">4:00 p.m.</p>
        <div class="slot-body">
          <h3>Opening</h3>
          <p>Welcome and introduction to the afternoon.</p>
        </div>
      </li>
      <li>
        <p class="slot-time">4:15–5:30 p.m.</p>
        <div class="slot-body">
          <h3>Guest talks</h3>
          <p>Four speakers from research and industry each present their view on software research in 15 minutes.</p>
          {% include speakers.html event=page.speakers %}
        </div>
      </li>
      <li>
        <p class="slot-time">5:30–6:00 p.m.</p>
        <div class="slot-body">
          <h3>Break</h3>
          <p>A short break before the panel.</p>
        </div>
      </li>
      <li>
        <p class="slot-time">6:00–6:45 p.m.</p>
        <div class="slot-body">
          <h3>Panel</h3>
          <p>The speakers discuss <em>Software research for society: needs and opportunities</em>.</p>
          {% include panel.html event=page.speakers moderator="Robillard, Martin" %}
        </div>
      </li>
      <li>
        <p class="slot-time">6:45–7:15 p.m.</p>
        <div class="slot-body">
          <h3>Presentation of SERIQ</h3>
          <p>Benoit Baudry, director of SERIQ, presents its history and scope. Representatives of the universities then give remarks:</p>
          <ul class="rep-list">
            <li>
              <span class="portrait-sm"><img src="{{ '/assets/img/speakers/bouchard.jpg' | relative_url }}" alt="" width="56" height="56" loading="lazy" decoding="async"></span>
              <span><a href="https://fas.umontreal.ca/faculte/direction-et-gouvernance/bureau-du-doyen/">Frédéric Bouchard</a>, Dean of the Faculty of Arts and Science, Université de Montréal</span>
            </li>
            <li>
              <span class="portrait-sm"><img src="https://www.polymtl.ca/expertises/sites/expertises.lxpolywebprod.polymtl.ca/files/daria-camilla-boffito_1.jpg" alt="" width="56" height="56" loading="lazy" decoding="async" referrerpolicy="no-referrer"></span>
              <span><a href="https://www.polymtl.ca/expertises/en/boffito-daria-camilla">Daria Camilla Boffito</a>, Associate Director, Research and Research Support, Polytechnique Montréal</span>
            </li>
            <li>
              <span class="portrait-sm"><img src="https://www.cs.mcgill.ca/media/professors/Pientka.jpg" alt="" width="56" height="56" loading="lazy" decoding="async" referrerpolicy="no-referrer"></span>
              <span><a href="https://www.cs.mcgill.ca/~bpientka/">Brigitte Pientka</a>, Director of the School of Computer Science, McGill University</span>
            </li>
            <li>
              <span class="portrait-sm"><img src="https://www.etsmtl.ca/uploads/_700xAUTO_fit_center-center_70_none/P20220119-Carter-Alan-002.jpg" alt="" width="56" height="56" loading="lazy" decoding="async" referrerpolicy="no-referrer" style="--zoom: 1.6; --focus: 96% 0%"></span>
              <span><a href="https://www.etsmtl.ca/en/study-at-ets/professors/acarter">Alan Carter</a>, Dean of Research, ÉTS</span>
            </li>
          </ul>
        </div>
      </li>
      <li>
        <p class="slot-time">7:15–8:00 p.m.</p>
        <div class="slot-body">
          <h3>Networking reception</h3>
          <p>With around 35 student research posters.</p>
        </div>
      </li>
    </ol>
    <p class="programme-more">
      <a class="cta" href="{{ page.registration_url }}">Register</a>
      <span>by {% include date.html date=page.registration_closes lang=page.lang %}</span>
    </p>
  </div>
</section>

<section class="band band--surface">
  <div class="wrap wrap--gutter">
    <h2>Getting there</h2>
    <p>
      <span lang="fr">{{ page.event_building }}</span>, room {{ page.event_room }}<br>
      <span lang="fr">{{ page.event_street }}, Montréal (Québec)</span> {{ page.event_postcode }}
    </p>
    <p>
      The building is a few minutes' walk from Université-de-Montréal metro
      station (blue line). If you are driving, UdeM describes
      <a href="https://di.umontreal.ca/services/stationnement/" hreflang="fr">visitor
      parking</a> and has a <a href="https://plancampus.umontreal.ca/" hreflang="fr">campus
      map</a>.
    </p>
    {% include event-map.html title="Map of Pavillon Jean-Coutu" link="Open in OpenStreetMap" %}
  </div>
</section>
