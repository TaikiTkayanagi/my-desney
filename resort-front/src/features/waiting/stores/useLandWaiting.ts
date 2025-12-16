import { defineStore } from 'pinia'
import type { LandWaitingType } from '../types/waitingType'
import { ref } from 'vue'

export const useLandWaiting = defineStore('landWaiting', () => {
  const land = ref<LandWaitingType | null>(null)
  async function fetchItems(url: string) {
    try {
      const response = await fetch(`${url}?place=land`)
      land.value = (await response.json()) as LandWaitingType
      console.log('取得成功')
    } catch (error) {
      console.log(error)
    }
  }

  return { land, fetchItems }
})
