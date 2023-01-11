<script lang="ts">
  import * as _ from "lodash";
  import { stats } from './store';
</script>
{#if !_.isEmpty($stats)}
  <div id='stats'>
    <table>
      <thead>
        <tr>
          <th>Stats</th>
          <th>Index</th>
          <th>Payout</th>
        </tr>
      </thead>
      <tbody>
        <tr class="flex w-full mb-6">
            <td class="p-4 w-1/4">Min</td>
            <td class="p-4 w-1/4">{$stats.index.min}</td>
            <td class="p-4 w-1/4">{$stats.payout.min}</td>
        </tr>
        <tr class="flex w-full mb-6">
          <td class="p-4 w-1/4">Max</td>
          <td class="p-4 w-1/4">{$stats.index.max}</td>
          <td class="p-4 w-1/4">{$stats.payout.max}</td>
        </tr>
        <tr class="flex w-full mb-6">
          <td class="p-4 w-1/4">Avg</td>
          <td class="p-4 w-1/4">{$stats.index.avg}</td>
          <td class="p-4 w-1/4">{$stats.payout.avg}</td>
        </tr>
        <tr class="flex w-full mb-6">
          <td class="p-4 w-1/4">Std</td>
          <td class="p-4 w-1/4">{$stats.index.std}</td>
          <td class="p-4 w-1/4">{$stats.payout.std}</td>
        </tr>
      </tbody>
    </table>
  </div>
{/if}