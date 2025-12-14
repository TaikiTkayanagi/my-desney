<script setup lang="ts">
import { onMounted } from 'vue';
import { useLandWaiting } from '../stores/useLandWaiting';

const { url } = defineProps<{
  url: string
}>()
const { land, areas, fetchItems } = useLandWaiting()
onMounted(fetchItems(url))
</script>

<template>
  <v-container>
    <v-row justify="space-around">
      <v-col v-for="area in areas" :key="area" cols="12" md="4">
        <v-sheet class="pa-12" color="grey-lighten-3">
          {{ area }}
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>
