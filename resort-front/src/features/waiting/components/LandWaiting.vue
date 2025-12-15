<script setup lang="ts">
import { onMounted } from 'vue';
import { useLandWaiting } from '../stores/useLandWaiting';
import { storeToRefs } from 'pinia';

const { url } = defineProps<{
  url: string
}>()
const landWaitingStore = useLandWaiting()
const { land } = storeToRefs(landWaitingStore)
onMounted(async () => await landWaitingStore.fetchItems(url))
</script>

<template>
  <v-expansion-panels variant="accordion">
    <v-expansion-panel>
      <v-expansion-panel-title>
        ワールドバザール
      </v-expansion-panel-title>
      <v-expansion-panel-text>
        <v-col v-for="attraction in land?.world" :key="attraction.name">
          {{ attraction.name }}
        </v-col>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
</template>
