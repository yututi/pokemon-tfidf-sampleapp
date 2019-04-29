<template>
  <v-app>
    <v-tabs v-model="tab" color="cyan" dark slider-color="yellow">
      <v-tab ripple href="#aimai">あいまい</v-tab>
      <v-tab ripple href="#shuzoku">種族値</v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item value="aimai"></v-tab-item>
      <v-tab-item value="shuzoku">
        <base-stats></base-stats>
      </v-tab-item>
    </v-tabs-items>
  </v-app>
</template>

<script lang="ts">
import BaseStats from "@/components/BaseStats.vue";
import { Component, Vue } from "vue-property-decorator";

@Component({
  components: {
    BaseStats
  }
})
export default class App extends Vue {
  tab: string = "aimai";
}
</script>
