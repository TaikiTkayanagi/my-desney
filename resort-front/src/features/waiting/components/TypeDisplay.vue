<script setup lang="ts">
import { condition } from '../model/condition';
import type { AreaType } from '../types/waitingType';

const { type, waitings } = defineProps<{
    type: string
    waitings: AreaType[]
}>()
</script>

<template>
    <v-row no-gutters class="text-body-1 text-decoration-underline">
        {{ type }}
    </v-row>
    <v-row no-gutters>
        <v-col v-for="waiting in waitings" :key="waiting.name" class="text-body-2" cols="12">
            {{ waiting.name }}
            {{ condition(waiting.condition).getConditionOrWaitTime() }}
        </v-col>
    </v-row>
</template>