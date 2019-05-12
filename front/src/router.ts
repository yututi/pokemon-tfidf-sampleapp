import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
        path: '/',
        name: 'アプリ',
        component: () => import(/* webpackChunkName: "about" */ './pages/Home.vue')
    },
    {
        path: '/pokemon',
        name: 'ポケモン検索',
        component: () => import(/* webpackChunkName: "about" */ './pages/Pokemon.vue')
    },
  ]
})
