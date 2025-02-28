<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
<nav class="bg-gray-800 p-4">
  <div class="container mx-auto flex justify-between items-center">
    <div class="text-white text-lg font-bold">
      <RouterLink to="/">IMC</RouterLink>
    </div>
    <div>
       <RouterLink to="/form" class="text-white px-4">Registrar</RouterLink>
      <RouterLink to="/login" class="text-white px-4">Login</RouterLink>
    </div>
  </div>
</nav>
  <RouterView />
</template>

<style scoped>
</style>
