<script setup lang="ts">
import { computed } from 'vue';
import type { AreaType } from '../types/waitingType';
import TypeDisplay from './TypeDisplay.vue';
import { condition } from '../model/condition';

const {areaName, areaList} = defineProps<{
    areaName: string
    areaList: AreaType[] | undefined
}>()
const attractions = computed(() => areaList?.filter(v => v.type === 'attraction'))
const greetings = computed(() => areaList?.filter(v => v.type === 'greeting'))
const restaurants = computed(() => areaList?.filter(v => v.type === 'restaurant'))
const totalWaitingTime = computed(() => {
    const waitTimes = areaList?.map(v => condition(v.condition).extractionWaitTime())
    if (waitTimes === undefined || waitTimes.length === 0) {
        return 0
    }
    return Math.round(waitTimes.reduce((accumlator, current) => accumlator + current, 0) / waitTimes?.length)
})
</script>

<template>
    <v-expansion-panels variant="accordion">
        <v-expansion-panel>
            <v-expansion-panel-title color="surface">
                <v-row>
                    <v-col cols="2">{{ areaName }}</v-col>
                    <v-col cols="2">現在: {{ totalWaitingTime }}分</v-col>
                    <v-col cols="2">30分後: {{ totalWaitingTime }}分</v-col>
                    <v-col cols="2">1時間後: {{ totalWaitingTime }}分</v-col>
                    <v-col cols="2">3時間後: {{ totalWaitingTime }}分</v-col>
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