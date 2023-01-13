<script lang="ts">
  import Controls from './Controls.svelte';
  import Stats from './Stats.svelte';
  import Table from './Table.svelte';
	import LineGraph from './LineGraph.svelte';
	import BarGraph from './BarGraph.svelte';
  import { data } from "./store"
</script>

<div id="app" class="h-screen grid grid-cols-1 gap-10">
  <div>
    <Controls />
  </div>
  <!-- Results -->
  <div class="grid grid-cols-3 justify-items-center">
    <!-- Line Graph -->
    <div> 
      <LineGraph data={$data}/>
    </div>
    <!-- Bar Graph -->
    <div>
      <h1>Bar Graph</h1>
      <!-- <BarGraph/> -->
    </div>
    <!-- Summary -->
    <div>
      <Stats/>
    </div>
  </div>
  <div>
    <Table/>
  </div>
</div>
