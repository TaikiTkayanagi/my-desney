<script setup lang="ts">
import { computed } from 'vue';
import type { AreaType } from '../types/waitingType';
import TypeDisplay from './TypeDisplay.vue';
import { condition } from '../model/condition';

const { areaName, areaList } = defineProps<{
  areaName: string
  areaList: AreaType[] | undefined
}>()
const attractions = computed(() => areaList?.filter(v => v.type === 'attraction'))
const greetings = computed(() => areaList?.filter(v => v.type === 'greeting'))
const restaurants = computed(() => areaList?.filter(v => v.type === 'restaurant'))
const waitingTime = computed(() => {
  const currentWaitTimes = areaList?.map(v => condition(v.condition).extractionWaitTime()) ?? []
  const tmlWaitTimes = areaList?.map(v => condition(v.tml).extractionWaitTime()) ?? []
  const ohlWaitTimes = areaList?.map(v => condition(v.ohl).extractionWaitTime()) ?? []
  const vhlWaitTimes = areaList?.map(v => condition(v.thl).extractionWaitTime()) ?? []
  return {
    current: Math.round(currentWaitTimes.reduce((accumlator, current) => accumlator + current, 0) / currentWaitTimes.length),
    tml: Math.round(tmlWaitTimes.reduce((accumlator, current) => accumlator + current, 0) / tmlWaitTimes.length),
    ohl: Math.round(ohlWaitTimes.reduce((accumlator, current) => accumlator + current, 0) / ohlWaitTimes?.length),
    thl: Math.round(vhlWaitTimes.reduce((accumlator, current) => accumlator + current, 0) / vhlWaitTimes.length)
  }
})
</script>

<template>
  <v-expansion-panels variant="accordion">
    <v-expansion-panel>
      <v-expansion-panel-title color="surface">
        <v-row>
          <v-col cols="3" class="text-caption">{{ areaName }}</v-col>
          <v-col cols="2">
            <div class="text-caption">現在</div>
            <div class="text-caption">{{ waitingTime.current }}分</div>
          </v-col>
          <v-col cols="2">
            <div class="text-caption">30分後</div>
            <div class="text-caption">{{ waitingTime.tml }}分</div>
          </v-col>
          <v-col cols="2">
            <div class="text-caption">1時間後</div>
            <div class="text-caption">{{ waitingTime.ohl }}分</div>
          </v-col>
          <v-col cols="2">
            <div class="text-caption">3時間後</div>
            <div class="text-caption">{{ waitingTime.thl }}分</div>
          </v-col>
        </v-row>
      </v-expansion-panel-title>
      <v-expansion-panel-text>
        <TypeDisplay v-if="attractions?.length" type="アトラクション" :waitings="attractions || []" />
        <TypeDisplay v-if="greetings?.length" type="グリーティング" :waitings="greetings || []" />
        <TypeDisplay v-if="restaurants?.length" type="レストラン" :waitings="restaurants || []" />
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
</template>
