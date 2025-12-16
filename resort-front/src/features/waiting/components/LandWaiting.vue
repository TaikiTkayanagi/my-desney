<script setup lang="ts">
import { onMounted } from 'vue';
import { storeToRefs } from 'pinia';
import AreaWaiting from './AreaWaiting.vue';
import { useLandWaiting } from '../stores/useLandWaiting';

const { url } = defineProps<{
  url: string
}>()
const landWaitingStore = useLandWaiting()
const { land } = storeToRefs(landWaitingStore)
onMounted(async () => await landWaitingStore.fetchItems(url))
</script>

<template>
  <p>更新日時: {{  land?.date_time }}</p>
  <AreaWaiting area-name="ワールドバザール" :area-list="land?.world"/>
  <AreaWaiting area-name="トゥモローランド" :area-list="land?.tommorow"/>
  <AreaWaiting area-name="トゥーンタウン" :area-list="land?.toon"/>
  <AreaWaiting area-name="ファンタジーランド" :area-list="land?.fantasy"/>
  <AreaWaiting area-name="クリッターカントリー" :area-list="land?.country"/>
  <AreaWaiting area-name="ウエスタンランド" :area-list="land?.westan"/>
  <AreaWaiting area-name="アドベンチャーランド" :area-list="land?.adventure"/>
  <AreaWaiting area-name="その他" :area-list="land?.other"/>
</template>
