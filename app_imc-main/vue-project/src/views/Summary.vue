<template>
  <div class="summary p-6 bg-gray-100 rounded-lg shadow-md">
    <h1 class="text-2xl font-bold mb-6">Resumen de Control dePeso y Altura </h1>
    
    <div class="statistics bg-white p-6 rounded-lg shadow-md">
      <h2 class="text-xl font-semibold mb-4">Statistics</h2>
      <div class="flex items-center mb-2">
        <svg class="w-6 h-6 text-blue-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c1.104 0 2-.896 2-2s-.896-2-2-2-2 .896-2 2 .896 2 2 2zm0 4c-1.104 0-2 .896-2 2s.896 2 2 2 2-.896 2-2-.896-2-2-2zm0 4c-1.104 0-2 .896-2 2s.896 2 2 2 2-.896 2-2-.896-2-2-2z"></path>
        </svg>
        <p class="text-lg">Peso Promedio: <span class="font-bold">{{ averageWeight }} kg</span></p>
      </div>
      <div class="flex items-center mb-2">
        <svg class="w-6 h-6 text-green-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c1.104 0 2-.896 2-2s-.896-2-2-2-2 .896-2 2 .896 2 2 2zm0 4c-1.104 0-2 .896-2 2s.896 2 2 2 2-.896 2-2-.896-2-2-2zm0 4c-1.104 0-2 .896-2 2s.896 2 2 2 2-.896 2-2-.896-2-2-2z"></path>
        </svg>
        <p class="text-lg">Altura Promedio: <span class="font-bold">{{ averageHeight }} m</span></p>
      </div>
      <div class="flex items-center">
        <svg class="w-6 h-6 text-red-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c1.104 0 2-.896 2-2s-.896-2-2-2-2 .896-2 2 .896 2 2 2zm0 4c-1.104 0-2 .896-2 2s.896 2 2 2 2-.896 2-2-.896-2-2-2zm0 4c-1.104 0-2 .896-2 2s.896 2 2 2 2-.896 2-2-.896-2-2-2z"></path>
        </svg>
        <p class="text-lg">IMC Promedio: <span class="font-bold">{{ averageIMC }}</span></p>
      </div>
    </div>
    
    
    <div class=" mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="card bg-white p-4 rounded-lg shadow-md">
        <line-chart v-if="loadCharts" :data="weightData" title="Cambio de Peso"></line-chart>
      </div>
      <div class="card bg-white p-4 rounded-lg shadow-md">
        <line-chart v-if="loadCharts" :data="heightData" title="Progreso de Altura"></line-chart>
      </div>
      <div class="card bg-white p-4 rounded-lg shadow-md">
        <bar-chart v-if="loadCharts" :data="imcData" title="Distribucion de IMC"></bar-chart>
      </div>
    </div>
    
  </div>
</template>

<script>
import LineChart from '../components/LineChart.vue';
import BarChart from '../components/BarChart.vue';
import http from '@/http';



export default {
  components: {
    LineChart,
    BarChart
  },
  data() {
    return {
      weightData: [],
      heightData: [],
      imcData: [],
      averageWeight: 0,
      averageHeight: 0,
      averageIMC: 0,
      loadCharts: false,
    };
  },
  mounted() {
    this.fetchSummaryData();
  },
  methods: {
    async fetchSummaryData() {
      try {
        const response = await http.get('/summary');
        const data = response.data;

        this.weightData = data.map(x => x.peso_kg);
        this.heightData = data.map(x => x.altura_m);
        this.imcData = data.map(x => x.imc);

        this.averageWeight = this.calculateAverage(this.weightData);
        this.averageHeight = this.calculateAverage(this.heightData);
        this.averageIMC = this.calculateAverage(this.imcData);
        this.loadCharts = true;
      } catch (error) {
        console.error('Error fetching summary data:', error);
      }
    },
    calculateAverage(data) {
      if (data.length === 0) return 0;
      const sum = data.reduce((acc, value) => acc + value, 0);
      return (sum / data.length).toFixed(2);
    }
  }
};
</script>

<style scoped>
.summary {
  padding: 20px;
}

.charts {
  display: flex;
  justify-content: space-around;
}

.statistics {
  margin-top: 20px;
}
</style>