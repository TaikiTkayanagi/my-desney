<script setup lang="ts">
import { ref } from 'vue';
import LandWaiting from './components/LandWaiting.vue';
import SeaWaiting from './components/SeaWaiting.vue';

const place = ref("land")
const url = import.meta.env.VITE_RESORT_API_BASE_URL
const landPath = import.meta.env.VITE_LAND_WAITING_PATH
const seaPath = import.meta.env.VITE_SEA_WAITING_PATH
</script>

<template>
  <header>
    <h1>D混雑</h1>
    <v-radio-group v-model="place" class="radio-solid">
      <v-radio label="ランド" value="land" base-color="black" color="black" />
      <v-radio label="シー" value="sea" base-color="black" color="black" />
    </v-radio-group>
  </header>
  <main>
    <LandWaiting :url="url + landPath" v-if="place == 'land'" />
    <SeaWaiting :url="url + seaPath" v-if="place == 'sea'" />
  </main>
</template>


<style scoped>
.radio-solid {
  --v-medium-emphasis-opacity: 1;
  --v-high-emphasis-opacity: 1;
}
</style>