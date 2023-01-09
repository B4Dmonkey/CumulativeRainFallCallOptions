<script lang="ts">
  let strike: Number;
  let exit: Number;
  let notional: Number;

  let startDate: Date;
  let endDate: Date;

  async function getData() {
    try {
      //Todo this is going to be one api call
      //Need validations etc to make sure this part isn't breaking
      const response = await fetch(`http://127.0.0.1:5000/rainfall/${startDate}/${endDate}`);
      const index = await response.json();
      console.log(`index is ${index}`)
    } catch (error) {
      console.error(`Error getting Rain Fall Index\n${error}`);
    }
  };
</script>

<div id="layout-login" class="grid grid-cols-3 gap-5 content-start">
  <div class="flex justify-center form-control w-full max-w-xs">
    <label for="input-strike" class="label">
      <span class="label-text">Strike</span>
    </label>
    <input 
      id="input-strike"
      class="input input-bordered w-half max-w-xs"
      type="number"
    />
  </div>

  <div class="flex justify-center form-control w-full max-w-xs">
    <label for="input-exit" class="label">
      <span class="label-text">Exit</span>
    </label>
    <input 
      id="input-exit"
      class="input input-bordered w-half max-w-xs"
      type="number"
    />
  </div>

  <div class="flex justify-center form-control w-full max-w-xs">
    <label for="input-notional" class="label">
      <span class="label-text">Notional</span>
    </label>
    <input 
      id="input-notional"
      class="input input-bordered w-half max-w-xs"
      type="number"
    />
  </div>

  <div class="flex justify-center form-control w-full max-w-xs">
    <label for="input-start" class="label">
      <span class="label-text">Start Date</span>
    </label>
    <input 
      type="date" 
      id="input-start" 
      name="trip-start"
      bind:value={startDate}
      min="2018-01-01" 
      max="2018-1-31"
    >
  </div>

  <div class="flex justify-center form-control w-full max-w-xs">
    <label for="input-end" class="label">
      <span class="label-text">End Date</span>
    </label>
    <input 
      type="date" 
      id="input-end" 
      name="trip-start"
      bind:value={endDate}
      min="2018-01-01" 
      max="2018-1-31"
    >
  </div>

  <div class="flex justify-center w-full max-w-xs">
    <button class="btn btn-wide" on:click={getData}>Query</button>
  </div>
</div>