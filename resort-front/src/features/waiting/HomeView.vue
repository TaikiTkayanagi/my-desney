<script setup lang="ts">
import { ref } from 'vue';
import LandWaiting from './components/LandWaiting.vue';

const place = ref("land")
const url = import.meta.env.VITE_RESORT_API_BASE_URL
const path = import.meta.env.VITE_LAND_WAITING_PATH
</script>

<template>
  <main>
    <LandWaiting :url="url + path" v-if="place == 'land'" />
    <!--<SeaWaiting v-if="place == 'sea'" />-->
  </main>
</template>
