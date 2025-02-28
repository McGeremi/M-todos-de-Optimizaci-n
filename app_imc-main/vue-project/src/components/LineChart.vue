<template>
  <div>
    <h3>{{ title }}</h3>
    <canvas ref="canvas"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
  props: {
    data: {
      type: Array,
      required: true
    },
    title: {
      type: String,
      required: true
    }
  },

  data: () => ({
    lastChart: null,
  }),

  mounted() {
    this.renderChart();
  },
  methods: {
    renderChart() {
      if(this.lastChart !== null && this.lastChart) {
        this.lastChart.destroy();
      }
      let data = JSON.parse(JSON.stringify(this.data));
      let title = JSON.parse(JSON.stringify(this.title));
      console.log({
        'tit': title,
        'data': data,
      })
      this.lastChart = new Chart(this.$refs.canvas, {
        type: 'line',
        data: {
          labels: data.map((_, index) => index + 1),
          datasets: [{
            label: title,
            data: data,
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
            fill: false
          }]
        },
        animation: {duration: 0}
      });
    }
  }
};
</script>

<style scoped>
canvas {
  width: 100%;
  height: 400px;
}
</style>