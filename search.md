---
layout: page
title: Search
comments: false
sharing: true
footer: true
exclude_from_search: true
permalink: /search/
---

<div id="search">
  <form action="/search" method="get">
    <input type="text" id="search-query" name="q" placeholder="Search" autocomplete="off">
  </form>
</div>

<section id="search-results" style="display: none;">
  <h1 id="search-results-heading">Search Results</h1>
  <div class="entries">
  </div>
</section>

{% raw %}
<script id="search-results-template" type="text/mustache">
  <ul>
  {{#entries}}
      <li class="post">
        <a href="{{url}}">{{title}}</a>
      </li>
    </article>
  {{/entries}}
  </ul>
</script>
{% endraw %}

<script type="text/javascript">
  $(function() {
    $('#search-query').lunrSearch({
      indexUrl: '/js/index.json',   // Url for the .json file containing search index data
      results : '#search-results',  // selector for containing search results element
      entries : '.entries',         // selector for search entries containing element (contained within results above)
      template: '#search-results-template'  // selector for Mustache.js template
    });
  });
</script>
