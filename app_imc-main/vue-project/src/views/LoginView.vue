<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
        <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
            <div v-if="feedbackMessage" class="mb-4 p-4 rounded bg-red-100 text-red-700">
                {{ feedbackMessage }}
            </div>
            <div class="flex justify-center mb-6">
                <button
                    :class="{'bg-blue-500 text-white': isLoginMode, 'bg-gray-200 text-gray-700': !isLoginMode}"
                    class="py-2 px-4 rounded-l focus:outline-none"
                    @click="isLoginMode = true"
                >
                    Login
                </button>
                <button
                    :class="{'bg-blue-500 text-white': !isLoginMode, 'bg-gray-200 text-gray-700': isLoginMode}"
                    class="py-2 px-4 rounded-r focus:outline-none"
                    @click="isLoginMode = false"
                >
                    Register
                </button>
            </div>
            <h2 class="text-2xl font-bold mb-6 text-center">{{ isLoginMode ? 'Login' : 'Register' }}</h2>
            <form @submit.prevent="isLoginMode ? handleLogin() : handleRegister()">
                <div class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
                        Username
                    </label>
                    <input
                        v-model="username"
                        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        id="username"
                        type="text"
                        placeholder="Username"
                    />
                </div>
                <div v-if="!isLoginMode" class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
                        Email
                    </label>
                    <input
                        v-model="email"
                        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        id="email"
                        type="email"
                        placeholder="Email"
                    />
                </div>
                <div class="mb-6">
                    <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
                        Password
                    </label>
                    <input
                        v-model="password"
                        class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                        id="password"
                        type="password"
                        placeholder="Password"
                    />
                </div>
                <div class="flex items-center justify-between">
                    <button
                        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                        type="submit"
                    >
                        {{ isLoginMode ? 'Sign In' : 'Register' }}
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import { useRouter } from 'vue-router';
import http from "../http.js";

export default {
    setup() {
        const router = useRouter();
        return { router };
    },
    data() {
        return {
            isLoginMode: true,
            username: '',
            email: '',
            password: '',
            feedbackMessage: ''
        };
    },
    methods: {
        async handleLogin() {
            try {
                const response = await http.post('login', {
                    username: this.username,
                    password: this.password
                });
                if (response.status === 200) {
                    console.log('Inicio de sesión exitoso');
                    this.router.push('/');
                }
            } catch (error) {
                this.feedbackMessage = 'Error de inicio de sesion: ' + error.response.data.message;
                console.error('error de inicio de sesion', error);
            }
        },
        async handleRegister() {
            try {
                const response = await http.post('register', {
                    username: this.username,
                    email: this.email,
                    password: this.password
                });
                if (response.status === 200) {
                    console.log('Registration successful');
                    this.isLoginMode = true;
                }
            } catch (error) {
                this.feedbackMessage = 'Registration failed: ' + error.response.data.message;
                console.error('Registration failed', error);
            }
        }
    }
};
</script>

<style scoped>
/* Add any additional styles here */
</style>