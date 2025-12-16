import { defineStore } from 'pinia'
import type { SeeWaitingType } from '../types/waitingType'
import { ref } from 'vue'

export const useSeaWaiting = defineStore('seaWaiting', () => {
  const sea = ref<SeeWaitingType | null>(null)
  async function fetchItems(url: string) {
    try {
      const response = await fetch(url)
      sea.value = (await response.json()) as SeeWaitingType
      console.log("取得成功")
    } catch (error) {
      console.log(error)
    } 
  }

  return { sea, fetchItems }
})
