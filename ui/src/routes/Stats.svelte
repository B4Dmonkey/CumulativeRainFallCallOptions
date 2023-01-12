<script lang="ts">
  import * as _ from "lodash";
  import { stats } from './store';
</script>
{#if !_.isEmpty($stats)}
  <div id='stats' class="overflow-x-auto">
    <table class="table w-full">
      <thead>
        <tr>
          <th>Stat</th>
          <th>Index</th>
          <th>Payout</th>
        </tr>
      </thead>
      <tbody>
        <tr class="hover">
            <td>Min</td>
            <td>{$stats.index.min.toFixed(5)}</td>
            <td>{$stats.payout.min.toFixed(5)}</td>
        </tr>
        <tr class="hover">
          <td>Max</td>
          <td>{$stats.index.max.toFixed(5)}</td>
          <td>{$stats.payout.max.toFixed(5)}</td>
        </tr>
        <tr class="hover">
          <td>Avg</td>
          <td>{$stats.index.avg.toFixed(5)}</td>
          <td>{$stats.payout.avg.toFixed(5)}</td>
        </tr>
        <tr class="hover">
          <td>Std</td>
          <td>{$stats.index.std.toFixed(5)}</td>
          <td>{$stats.payout.std.toFixed(5)}</td>
        </tr>
      </tbody>
    </table>
  </div>
{/if}