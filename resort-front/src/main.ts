import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import { createVuetify } from 'vuetify'
import 'vuetify/styles'

const app = createApp(App)
const vuetify = createVuetify()

app.use(createPinia())
app.use(router)
app.use(vuetify)

app.mount('#app')
