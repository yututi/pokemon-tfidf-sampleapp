import Vue from 'vue'
import './plugins/vuetify'
import 'vuetify/dist/vuetify.min.css'
import App from './App.vue'
import router from './router'

import axios from 'axios'
if (process.env.NODE_ENV === "production") {
    axios.defaults.baseURL = "api"
    Vue.config.productionTip = false
} else {
    axios.defaults.baseURL = "http://localhost:8000/api"
}


new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
