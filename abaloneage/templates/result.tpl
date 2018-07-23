% rebase('templates/base.tpl')
<div>
  <h3>About this abalone:
         sex->{{ sex }},
         length->{{ length }}mm,
         diameter->{{ diameter }}mm,
         height->{{ height }}mm,
         weight->{{ weight }}g,
  </h3>
  <h3>Age of this abalone should be {{ age }}.</h3>
  <a href="/" class="secondary button">Get back to home page → </a>
</div>
