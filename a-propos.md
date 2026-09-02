---
layout: default
ref: about
title: À propos
description: "La mission du Centre, ses quatre axes de recherche, ses établissements partenaires, et le parcours des rencontres SEMTL au centre SERIQ."
permalink: /a-propos/
---

<div class="hero">
  <div class="wrap">
    <h1>À propos</h1>
    <p class="lede">
      SERIQ est un centre interuniversitaire de recherche en génie logiciel.
      Il prend la suite des rencontres SEMTL, tenues à Montréal depuis plus de
      dix ans.
    </p>
  </div>
</div>

<section class="band band--paper">
  <div class="wrap">
    <h2>Mission</h2>
    <p>
      Le Centre développe une recherche en génie logiciel qui vise à soutenir la
      transformation numérique de la science et de la société. Cette recherche
      s'articule autour de quatre axes complémentaires, qui répondent aux défis liés
      au développement des logiciels modernes.
    </p>
    <p>
      Le Centre compte quatre établissements partenaires. D'autres établissements
      universitaires peuvent se joindre au protocole d'entente interuniversitaire.
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
    <p>La mission du Centre s'articule aussi autour des points suivants&nbsp;:</p>
    <ul>
      <li>
        intégrer la formation d'étudiantes, d'étudiants et de stagiaires
        postdoctoraux dans ses activités scientifiques, et développer des
        perspectives de carrière pour les jeunes scientifiques&nbsp;;
      </li>
      <li>
        échanger, collaborer et établir des partenariats durables avec la
        communauté d'affaires et le secteur public&nbsp;;
      </li>
      <li>
        coopérer avec d'autres organismes œuvrant dans le domaine de la recherche
        logicielle interdisciplinaire centrée sur l'humain, au Canada et dans le
        monde.
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
    <h2>Axes de recherche</h2>
    <p>
      Les quatre axes se rejoignent sur un socle commun&nbsp;: l'ingénierie logicielle
      — exigences, modélisation, test, intégration, sécurité.
    </p>
    <ol class="axes">
      <li data-label="Axe">
        <h3>{{ site.data.i18n[page.lang].axes.cps }}</h3>
        <p>
          Le logiciel ne se limite plus à des systèmes purement numériques&nbsp;: il
          s'intègre à des contextes physiques, biologiques et sociaux. Jumeaux
          numériques, internet des objets, systèmes d'exploitation.
        </p>
      </li>
      <li data-label="Axe">
        <h3>{{ site.data.i18n[page.lang].axes.ecosystems }}</h3>
        <p>
          Les infrastructures logicielles s'appuient sur des plateformes partagées et
          des chaînes d'approvisionnement hétérogènes. Chaîne d'approvisionnement
          logicielle, infonuagique et calcul haute performance, lignes de produits.
        </p>
      </li>
      <li data-label="Axe">
        <h3>{{ site.data.i18n[page.lang].axes.design }}</h3>
        <p>
          La conception d'un système ne repose pas sur la seule expertise
          informatique&nbsp;: elle engage aussi les spécialistes des domaines.
          Low-code, modélisation spécifique aux domaines, ingénierie des exigences.
        </p>
      </li>
      <li data-label="Axe">
        <h3>{{ site.data.i18n[page.lang].axes.human }}</h3>
        <p>
          L'humain reste au cœur des systèmes logiciels, comme utilisateur, opérateur
          ou concepteur. Accessibilité, interaction humain-machine, documentation.
        </p>
      </li>
    </ol>

    <h2>Axes transversaux</h2>
    <p>
      Quatre préoccupations traversent les quatre axes plutôt que d'appartenir à
      l'un d'eux.
    </p>
    <ul class="cross-axes">
      <li>
        <h3>IA</h3>
        <ul>
          <li>IA pour le génie logiciel</li>
          <li>Génie logiciel pour l'IA</li>
        </ul>
      </li>
      <li>
        <h3>Domaines d'application</h3>
        <ul>
          <li>Science</li>
          <li>Finance</li>
          <li>Transport</li>
          <li>Infrastructure</li>
          <li>Société civile</li>
          <li>Culture</li>
          <li>Industrie</li>
          <li>Santé</li>
          <li>Aérospatiale</li>
        </ul>
      </li>
      <li>
        <h3>Préoccupations et qualités</h3>
        <ul>
          <li>Sécurité</li>
          <li>Fiabilité</li>
          <li>Adaptabilité</li>
          <li>Performance</li>
          <li>Souveraineté</li>
          <li>Transparence</li>
        </ul>
      </li>
      <li>
        <h3>Transfert de connaissances</h3>
        <ul>
          <li>Milieux scientifiques</li>
          <li>Milieux industriels</li>
          <li>Gouvernements</li>
          <li>Grand public</li>
        </ul>
      </li>
    </ul>
  </div>
</section>

<section class="band band--paper">
  <div class="wrap">
    <h2>Des rencontres SEMTL au centre SERIQ</h2>
    <p>
      SEMTL <i lang="en">(Software Engineering at Montreal)</i> réunit depuis plus
      de dix ans la communauté montréalaise de recherche en génie logiciel. Le
      registre en ligne commence en 2019&nbsp;: sept rencontres cette année-là, puis
      deux au début de 2020, avant que la pandémie ne les interrompe.
    </p>
    <p>
      Les rencontres reprennent en août 2022, environ tous les deux mois. Les six
      universités montréalaises les accueillent et les soutiennent à tour de rôle,
      et certaines se tiennent en marge de conférences comme
      <a href="{{ '/semtl/2025-04-27-icse/' | relative_url }}">ICSE</a> et
      <a href="{{ '/semtl/2026-06-03-polytechnique/' | relative_url }}">SEMLA</a>.
    </p>
    <p>
      Les discussions de groupe entre les membres de SEMTL ont aussi donné lieu à un
      article de vision, présenté dans la piste principale de
      <a href="{{ '/semtl/2024-09-27-models/' | relative_url }}">MODELS 2024</a>.
    </p>
    <p>
      En octobre 2026, SEMTL devient SERIQ. La série de rencontres se poursuit. Le
      centre s'étend à l'ensemble du Québec et structure la recherche autour des
      quatre axes ci-dessus.
    </p>
  </div>
</section>
