<template>
  <v-app>
    <v-tabs v-model="tab" dark slider-color="orange">
      <v-tab ripple href="#aimai">あいまい</v-tab>
      <v-tab ripple href="#shuzoku">種族値</v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item value="aimai">
        <term-search></term-search>
      </v-tab-item>
      <v-tab-item value="shuzoku">
        <stats-search></stats-search>
      </v-tab-item>
    </v-tabs-items>
  </v-app>
</template>

<script lang="ts">
import StatsSearch from "@/components/StatsSearch.vue";
import TermSearch from "@/components/TermSearch.vue";
import { Component, Vue } from "vue-property-decorator";

@Component({
  components: {
    StatsSearch,
    TermSearch
  }
})
export default class App extends Vue {
  tab: string = "aimai";
  mounted(){
      document.title = "機械学習サンプル"
  }
}
</script>
