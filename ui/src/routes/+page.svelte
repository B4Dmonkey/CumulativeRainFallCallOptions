<script lang="ts">
  let startDate: Date;
  let endDate: Date;

  async function getRainFallIndex() {
    // ! need to make sure this can only be done with valid dates
    console.log(`The Start Date is ${startDate}`);
    console.log(`The End Date is ${endDate}`);
    const query = {
      start:startDate.toString(), 
      end: endDate.toString()
    };
    const response = await fetch(`http://127.0.0.1:5000/rainfall/${startDate}/${endDate}`);
    console.log('response is')
    console.dir(response)
  };

</script>

<label for="input-start">Start date:</label>
<input 
  type="date" 
  id="input-start" 
  name="trip-start"
  bind:value={startDate}
  min="2018-01-01" 
  max="2018-1-31"
>

<label for="input-start">End date:</label>
<input 
  type="date" 
  id="input-start" 
  name="trip-start"
  bind:value={endDate}
  min="2018-01-01" 
  max="2018-1-31"
>

<button on:click={getRainFallIndex}>Get Index</button>