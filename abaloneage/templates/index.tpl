% rebase('templates/base.tpl')
<div>
  <h3>How about the abalone has been catched ?</h3>
</div>
<form action="/abaloneage" method="post">
  <fieldset>
    <legend align="left">Enter information</legend>

    <!-- sex -->
    <div class="input-group fluid">
      <div class="col-sm-12 col-md-2">
        <label for="sex">Sex</label>
      </div>
      <div class="col-sm-12 col-md">
        <select id="sex" name="sex">
          <option value="0">Female</option>
          <option value="1">UnKnown</option>
          <option value="2">Male</option>
        </select> </div>
    </div>

    <!-- length -->
    <div class="input-group fluid">
      <div class="col-sm-12 col-md-2">
        <label for="length">length</label>
      </div>
      <div class="col-sm-12 col-md">
        <input type="number" id="length" name="length" min="0" style="width:20%;" required>
      </div>
    </div>

    <!-- diameter-->
    <div class="input-group fluid">
      <div class="col-sm-12 col-md-2">
        <label for="diameter">diameter</label>
      </div>
      <div class="col-sm-12 col-md">
        <input type="number" id="diameter" name="diameter" min="0" style="width:20%;" required>
      </div>
    </div>

    <!-- height -->
    <div class="input-group fluid">
      <div class="col-sm-12 col-md-2">
        <label for="height">height</label>
      </div>
      <div class="col-sm-12 col-md">
        <input type="number" id="height" name="height" min="0" style="width:20%;" required>
      </div>
    </div>

    <!-- weight -->
    <div class="input-group fluid">
      <div class="col-sm-12 col-md-2">
        <label for="weight">weight</label>
      </div>
      <div class="col-sm-12 col-md">
        <input type="number" id="weight" name="weight" min="0" style="width:20%;" required>
      </div>
    </div>

    <!-- Send button -->
    <div class="input-group">
      <input type="submit" class="primary" value="Guess Age">
    </div>
  </fieldset>
</form>
