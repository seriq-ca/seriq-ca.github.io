---
ref: event-2026-10-29
title: Rentrée SERIQ
title_head: "Rentrée SERIQ · October 29, 2026"
description: "The first meeting under the SERIQ banner and the move to a larger network that will grow to cover Quebec. October 29, 2026, from 3:00 to 7:00 p.m. at Université de Montréal. Guest talks, a panel and networking."
permalink: /en/events/2026-10-29-rentree-seriq/
event_date: 2026-10-29
event_time: 3:00–7:00 p.m.
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
  The <i lang="fr">rentrée</i> marks the return of the meeting series
  under the SERIQ banner, continuing the SEMTL network and its more than
  ten years of activity.
---

<div class="hero">
  <div class="wrap">
    <p class="kicker">SERIQ meeting</p>
    <h1 lang="fr">Rentrée SERIQ</h1>
    <p class="lede">
      The first meeting under the SERIQ banner, continuing the
      <a href="https://semtl.github.io/">SEMTL</a> meeting series. It marks the
      move to a larger network, one that will grow to cover Quebec, and brings
      the community together to discuss what software engineering contributes
      to the challenges of the digital society.
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
        <strong>3:00 p.m.</strong> Opening.
      </li>
      <li>
        <strong>3:15–4:30 p.m.</strong> Guest talks from research and industry.
        Each speaker presents their view of software research in 15 minutes:
        {% include speakers.html event=page.speakers %}
      </li>
      <li>
        <strong>4:30–5:00 p.m.</strong> Break.
      </li>
      <li>
        <strong>5:00–5:45 p.m.</strong> Panel, <em>Software research for
        society: needs and opportunities</em>, where the speakers discuss the
        topics more broadly.
      </li>
      <li>
        <strong>5:45–6:15 p.m.</strong> The history and scope of SERIQ, by its
        director Benoit Baudry, followed by deans and other representatives
        (to be confirmed).
      </li>
      <li>
        <strong>6:15–7:00 p.m.</strong> Networking reception, with student
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
