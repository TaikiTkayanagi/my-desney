<script setup lang="ts">
import { computed } from 'vue';
import { condition } from '../model/condition';
import type { AreaType } from '../types/waitingType';

const { type, waitings } = defineProps<{
  type: string
  waitings: AreaType[]
}>()

const waitingsForDisplay = computed(() => {
  return waitings.map(v => {
    const displayCondition = condition(v.condition).getConditionOrWaitTime()
    if (v.tml == null && v.ohl == null && v.thl == null) {
      return {
        name: v.name,
        displays: [displayCondition]
      }
    }
    if (!v.condition.includes('分')) {
      return {
        name: v.name,
        displays: [displayCondition]
      }
    }
    const tmlDisplay = condition(v.tml).getConditionOrWaitTime()
    const ohlDisplay = condition(v.ohl).getConditionOrWaitTime()
    const thlDisplay = condition(v.thl).getConditionOrWaitTime()

    return {
      name: v.name,
      displays: [displayCondition, tmlDisplay, ohlDisplay, thlDisplay]
    }
  })
})
</script>

<template>
  <v-row no-gutters class="text-caption text-decoration-underline">
    {{ type }}
  </v-row>
  <v-row no-gutters>
    <template v-for="waiting in waitingsForDisplay" :key="waiting.name">
      <v-col class="text-caption" cols="3">
        {{ waiting.name }}
      </v-col>
      <v-col class="text-caption" v-for="i in 4" :key="i" cols="2">
        {{ waiting.displays?.[i - 1] ?? '' }}
      </v-col>
    </template>

  </v-row>
</template>
