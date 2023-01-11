<script lang="ts">
  import Controls from './Controls.svelte';
  import Stats from './Stats.svelte';
  import Table from './Table.svelte';
	import LineGraph from './LineGraph.svelte';
</script>

<!-- <div> -->
  <!-- <h1>Stats {$stats}</h1> -->
  <!-- <h1>Strike {$strike}</h1>
  <h1>Exit {$exit}</h1>
  <h1>Notional {$notional}</h1>
  <h1>Start Date {$startDate}</h1>
  <h1>End Date {$endDate}</h1>
  <h1>Data {$data}</h1> -->
<!-- </div> -->
<div id="app" class="h-screen grid grid-cols-1 gap-10 content-center">
  <!-- Inputs -->
  <div>
    <Controls />
  </div>
  <!-- Summary -->
  <!-- <div>
    <Stats/>
  </div> -->
  <!-- <div>
    <Table/>
  </div> -->
    <!-- <h1>Data goes here</h1> -->
    <!-- <label for="show" style="display: inline;">Show Line:</label>
    <input id="show" type="checkbox" bind:checked={show} />
    <LineGraph {data} {show} /> -->
</div>
