% rebase('templates/base.tpl', use_bokeh=True)
<div>
  <h3>About this abalone:
         sex->{{ abalone.sex_str }},
         length->{{ abalone.length }}mm,
         diameter->{{ abalone.diameter }}mm,
         height->{{ abalone.height }}mm,
         weight->{{ abalone.weight }}g,
  </h3>
  <div>
    {{ !graph }}
  </div>
  <h3>Age of this abalone should be {{ abalone.age }}.</h3>
</div>
