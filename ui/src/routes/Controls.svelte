<script lang="ts">
  import {strike, exit, notional, optionType, startDate, endDate, data, stats} from "./store"

  async function getData() {
    try {
      //Todo this is going to be one api call
      //Need validations etc to make sure this part isn't breaking
      const url = `http://127.0.0.1:5000/${$optionType}/${$startDate}/${$endDate}/${$strike}/${$exit}/${$notional}`
      const response = await fetch(url);
      const data = await response.json();
      $data = data.results;
      $stats = data.summary;
      
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
      bind:value={$strike}
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
      bind:value={$exit}
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
      bind:value={$notional}
    />
  </div>

  <div class="flex justify-center form-control w-full max-w-xs">
    <label for="input-start" class="label">
      <span class="label-text">Start Date</span>
    </label>
    <input 
      type="date" 
      id="input-start" 
      name="input-start"
      bind:value={$startDate}
    >
  </div>

  <div class="flex justify-center form-control w-full max-w-xs">
    <label for="input-end" class="label">
      <span class="label-text">End Date</span>
    </label>
    <input 
      type="date" 
      id="input-end" 
      name="input-end"
      bind:value={$endDate}
    >
  </div>

  <div class="flex justify-center w-full max-w-xs">
    <button class="btn btn-wide" on:click={getData}>Query</button>
  </div>
</div>