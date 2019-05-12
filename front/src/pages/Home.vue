<template>
  <div class="home">
    <h3>アプリ一覧</h3>
    <ul>
      <template v-for="route in $router.options.routes">
        <li :key="route.path" v-if="route.path !== $route.path">
          <router-link :to="route.path">{{route.name}}</router-link>
        </li>
      </template>
    </ul>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class Home extends Vue {}
</script>
<style lang="stylus">
.home {
  padding: 2em;
}
</style>
