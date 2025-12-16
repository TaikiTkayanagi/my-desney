<script setup lang="ts">
import { onMounted } from 'vue';
import { storeToRefs } from 'pinia';
import AreaWaiting from './AreaWaiting.vue';
import { useSeaWaiting } from '../stores/useSeaWaiting';

const { url } = defineProps<{
  url: string
}>()
const seaWaitingStore = useSeaWaiting()
const { sea } = storeToRefs(seaWaitingStore)
onMounted(async () => await seaWaitingStore.fetchItems(url))
</script>

<template>
  <p>更新日時: {{  sea?.date_time }}</p>
  <AreaWaiting area-name="メディテレーニアンハーバー" :area-list="sea?.mediterranean"/>
  <AreaWaiting area-name="アラビアンコースト" :area-list="sea?.arabian"/>
  <AreaWaiting area-name="ファンタジースプリングス" :area-list="sea?.fantasy"/>
  <AreaWaiting area-name="マーメイドラグーン" :area-list="sea?.mermaid"/>
  <AreaWaiting area-name="ミステリアスアイランド" :area-list="sea?.mysterious"/>
  <AreaWaiting area-name="アメリカンウォーターフロント" :area-list="sea?.america"/>
  <AreaWaiting area-name="ポートディスカバリー" :area-list="sea?.port"/>
  <AreaWaiting area-name="ロストリバーデルタ" :area-list="sea?.lost"/>
  <AreaWaiting area-name="その他" :area-list="sea?.other"/>
</template>