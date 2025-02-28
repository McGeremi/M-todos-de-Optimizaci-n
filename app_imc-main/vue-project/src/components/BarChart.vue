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
      this.lastChart = new Chart(this.$refs.canvas, {
        type: 'bar',
        data: {
          labels: this.data.map((_, index) => index + 1),
          datasets: [{
            label: this.title,
            data: this.data,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
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