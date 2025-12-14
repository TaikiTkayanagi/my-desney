import { defineStore } from 'pinia'
import type { LandWaitingType } from '../types/landWaitingType'
import { ref } from 'vue'

export const useLandWaiting = defineStore('landWaiting', () => {
  const land = ref<LandWaitingType | null>(null)
  const areas = [
    'ワールドバザール',
    'トゥモローランド',
    'トゥーンタウン',
    'ファンタジーランド',
    'クリッターカントリー',
    'ウェスタンランド',
    'アドベンチャーランド',
  ]

  async function fetchItems(url: string) {
    try {
      const response = await fetch(url)
      land.value = (await response.json()) as LandWaitingType
    } catch (error) {
      console.log(error)
    }
  }

  return { land, areas, fetchItems }
})
