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
  <v-container>
    <v-row no-gutters>
      <v-col>
        ワールドバザール
      </v-col>
    </v-row>
    <v-row>

      <v-col v-for="attraction in land?.world" :key="attraction.name" cols="12" md="2" offset="0">
        <v-sheet class="pa-12" color="grey-lighten-3">
          {{ attraction.name }}
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>
