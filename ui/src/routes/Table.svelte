<script lang="ts">
  import { data } from './store';
</script>
{#if $data.length > 0}
  <div class="overflow-y-auto h-1/5">
    <table class="table table-fixed table-zebra table-compact w-1/2 mx-auto">
      <thead>
        <tr>
          <th>Year</th>
          <th>Index</th>
          <th>Payout</th>
        </tr>
      </thead>
      <tbody>
        {#each $data as { year, index, payout }}
        <tr class="hover">
            <td>{year}</td>
            <td>{index}</td>
            <td>{payout}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
  
{/if}

<!-- {#if $data.length > 0}
  <div class="container">
    <table class="table table-auto w-full">
      <thead class="w-full">
        <tr class="flex w-full mb-6">
          <th class="p-4 w-1/4">Year</th>
          <th class="p-4 w-1/4">Index</th>
          <th class="p-4 w-1/4">Payout</th>
        </tr>
      </thead>
      <tbody class="flex flex-col overflow-y-scroll w-full" style="height: 50vh;">
        {#each $data as { year, index, payout }}
        <tr class="flex w-full mb-6">
            <td class="p-4 w-1/4">{year}</td>
            <td class="p-4 w-1/4">{index}</td>
            <td class="p-4 w-1/4">{payout}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
{/if} -->