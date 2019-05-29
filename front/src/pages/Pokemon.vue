<template>
  <v-app>
    <v-tabs v-model="tab" dark slider-color="orange">
      <v-tab ripple href="#fuzzy">全文</v-tab>
      <v-tab ripple href="#stats">種族値</v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab" touchless>
      <v-tab-item value="fuzzy">
        <term-search></term-search>
      </v-tab-item>
      <v-tab-item value="stats">
        <stats-search></stats-search>
      </v-tab-item>
    </v-tabs-items>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({
  components: {
    StatsSearch:()=> import("@/components/StatsSearch.vue"),
    TermSearch:()=>import("@/components/TermSearch.vue")
  }
})
export default class Pokemon extends Vue {
  tab: string = "fuzzy";
}
</script>
