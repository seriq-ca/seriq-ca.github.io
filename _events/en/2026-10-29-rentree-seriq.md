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

<div class="hero">
  <div class="wrap">
    <p class="kicker">SERIQ meeting</p>
    <h1 lang="fr">Rentrée SERIQ</h1>
    <p class="lede">
      SERIQ expands the <a href="https://semtl.github.io/">SEMTL</a> research
      network to work on software engineering for the digital society. For its
      <i lang="fr">rentrée</i>, we invite researchers, students, industry
      partners and institutional representatives to guest talks from research
      and industry, followed by a panel on software research for society.
      Benoit Baudry will then present the history and
      scope of SERIQ, followed by remarks, before a networking reception with
      student posters.
    </p>
  </div>
</div>

<section class="band band--feature">
  <div class="wrap">
    <div class="event">
      <p class="when">{% include date.html date=page.event_date lang=page.lang weekday=true %}</p>
      <dl class="event-details">
        <dt>Time</dt><dd>{{ page.event_time }}</dd>
        <dt>Venue</dt><dd lang="fr">{{ page.event_venue }}</dd>
        <dt>Language</dt><dd>Bilingual (French and English)</dd>
        <dt>Register</dt><dd>by {% include date.html date=page.registration_closes lang=page.lang %}</dd>
      </dl>
      <p class="note">
        The building and room will be confirmed before the meeting.
      </p>
      <p class="more">
        <a class="cta" href="{{ page.registration_url }}">Register</a>
      </p>
    </div>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <h2>Programme</h2>
    <ul>
      <li>
        <strong>3:45–4:00 p.m.</strong> Registration.
      </li>
      <li>
        <strong>4:00 p.m.</strong> Opening.
      </li>
      <li>
        <strong>4:15–5:30 p.m.</strong> Guest talks from research and industry.
        Each speaker presents their view on software research in 15 minutes:
        {% include speakers.html event=page.speakers %}
      </li>
      <li>
        <strong>5:30–6:00 p.m.</strong> Break.
      </li>
      <li>
        <strong>6:00–6:45 p.m.</strong> Panel, <em>Software research for
        society: needs and opportunities</em>, where the speakers discuss the
        topics more broadly. Moderated by Martin Robillard.
      </li>
      <li>
        <strong>6:45–7:15 p.m.</strong> The history and scope of SERIQ, by its
        director Benoit Baudry, followed by deans and other representatives
        (to be confirmed).
      </li>
      <li>
        <strong>7:15–8:00 p.m.</strong> Networking reception, with student
        posters.
        <ul>
          <li>
            Students can submit a poster proposal with the
            <a href="https://forms.gle/jUGuScfx11nuFTti7">submission form</a>
            by October 9, 2026.
          </li>
        </ul>
      </li>
    </ul>
  </div>
</section>
