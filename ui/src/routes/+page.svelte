<script lang="ts">
  import data from './data';
  import Controls from './Controls.svelte';
	import LineGraph from './LineGraph.svelte';

  let show: boolean = false;

  let startDate: Date;
  let endDate: Date;

  async function getRainFallIndex() {
    try {
      console.log(`The Start Date is ${startDate}`);
      console.log(`The End Date is ${endDate}`);
      
      const response = await fetch(`http://127.0.0.1:5000/rainfall/${startDate}/${endDate}`);
      const index = await response.json();
      console.log(`index is ${index}`)
    } catch (error) {
      console.error(`Error getting Rain Fall Index\n${error}`);
    }
    // ! need to make sure this can only be done with valid dates
  };

</script>

<div id="app" class="h-screen grid grid-cols-1 gap-10 content-center">
  <div>
    <Controls/>
  </div>
  <div>
    <h1>Data goes here</h1>
    <!-- <label for="show" style="display: inline;">Show Line:</label>
    <input id="show" type="checkbox" bind:checked={show} />
    <LineGraph {data} {show} /> -->
  </div>
</div>
