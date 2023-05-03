<template>
    <div ref="chartContainer" style="width: 50%; height: 50%; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);"></div>
</template>
  
  <script>
  import * as echarts from 'echarts';
  import data from '@/assets/data/server_data.json';
  
  export default {
    data() {
      return {
        chart: null,
      };
    },
    mounted() {
      this.initChart();
    },
    methods: {
      initChart() {
        const chartContainer = this.$refs.chartContainer;
        this.chart = echarts.init(chartContainer);
  
        const option = {
          tooltip: {
            trigger: 'axis',
          },
          xAxis: {
            type: 'time',
            name: 'Time',
          },
          yAxis: {
            type: 'value',
            name: 'Usage (%)',
            min: 0,
            max: 100,
          },
          series: [
            {
              name: 'CPU Usage',
              type: 'line',
              data: data.map((item) => [item.save_time, item.cpu_usage]),
            },
            {
              name: 'GPU Usage',
              type: 'line',
              data: data.map((item) => [item.save_time, item.gpu_usage]),
            },
            {
              name: 'GPU Memory',
              type: 'line',
              data: data.map((item) => [item.save_time, item.gpu_mem]),
            },
            {
              name: 'Disk Usage',
              type: 'line',
              data: data.map((item) => [item.save_time, item.disk]),
            },
            {
              name: 'Memory Usage',
              type: 'line',
              data: data.map((item) => [item.save_time, item.mem]),
            },
          ],
        };
  
        this.chart.setOption(option);
      },
    },
  };
  </script>
  