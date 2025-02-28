<template>
    <div class="max-w-md mx-auto mt-10">
        <h1 class="text-2xl font-bold mb-4">Formulario de Peso y Altura</h1>
        <p class="mb-4 text-gray-600">📋 ¡Registra tus datos de peso y altura para llevar un control de tu salud! 💪</p>
        <form @submit.prevent="submitForm" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="date">
                    Fecha
                </label>
                <input
                    v-model="date"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="date"
                    type="date"
                    placeholder="Seleccione una fecha"
                />
            </div>
            <div class="mb-4">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="weight">
                    Peso
                </label>
                <input
                    v-model="weight"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="weight"
                    type="number"
                    placeholder="Ingrese su peso"
                />
            </div>
            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-bold mb-2" for="height">
                    Altura
                </label>
                <input
                    v-model="height"
                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    id="height"
                    type="number"
                    step="0.01"
                    placeholder="Ingrese su altura"
                />
            </div>
            <div v-if="successMessage" class="mb-4 text-green-500">
                {{ successMessage }}
            </div>
            <div class="flex items-center justify-between">
                <button
                    class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                    type="submit"
                >
                    Enviar
                </button>
            </div>
        </form>
    </div>
</template>

<script>
import http from "@/http.js";

export default {
    data() {
        return {
            weight: '',
            height: '',
            successMessage: null,
            date: null,
        };
    },
    methods: {
        async submitForm() {
            try {
                this.successMessage = null;
                const response = await http.post('/insert', {
                    fecha: this.date,
                    peso_kg: this.weight,
                    altura_m: this.height
                });
                this.successMessage = response.data.message;
                
            } catch (error) {
                console.error('Error:', error);
            }
        }
    }
};
</script>

<style scoped>
/* Add any custom styles here */
</style>