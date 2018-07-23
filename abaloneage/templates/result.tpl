% rebase('templates/base.tpl')
<div>
  <h3>About this abalone:
         sex->{{ abalone.sex_str }},
         length->{{ abalone.length }}mm,
         diameter->{{ abalone.diameter }}mm,
         height->{{ abalone.height }}mm,
         weight->{{ abalone.weight }}g,
  </h3>
  <h3>Age of this abalone should be {{ abalone.age }}.</h3>
  <a href="/" class="secondary button">Get back to home page → </a>
</div>
