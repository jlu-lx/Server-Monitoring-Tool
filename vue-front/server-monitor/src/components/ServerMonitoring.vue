<template>
    <h1>Server Monitoring</h1>
    <div v-if="isLoading">Loading server stats...</div>
    <div v-else>
        <p>CPU Usage: 100%</p>
        <p>GPU Usage: 1%</p>
        <p>GPU Memory: 1%</p>
        <p>Disk Usage: 1%</p>
        <p>Memory Usage: 1%</p>
    </div>
</template>

<script>
import ServerStatsChart from './ServerStatsChart.vue';
import monitoringService from '../services/monitoringService';


export default {
  data() {
    return {
      isLoading: true,
      serverStats: null,
      flag: false
    }
  }
}

</script>