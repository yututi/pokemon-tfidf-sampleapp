<template>
  <v-container fluid grid-list-lg>
    <div class="display-3 text-xs-center mb-3">全文検索</div>
    <v-layout row wrap style="max-width:600px;margin:auto;">
      <v-flex xs12>
        <v-text-field v-model="query" label="検索条件" required @input="onInput"></v-text-field>
      </v-flex>
      <v-flex xs12>
        <v-subheader>検索結果</v-subheader>
        <poke-card v-for="(pokemon, index) in pokeList" :key="index" :pokemon="pokemon" :showWiki="true"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import debounce from "lodash/debounce";
import { Pokemon } from "@/types";
import axios from "axios";

@Component({
  components: {
    PokeCard: () => import("./PokeCard.vue")
  }
})
export default class TermSearch extends Vue {
  query: string = "";
  pokeList: Array<Pokemon> = [];
  onInput() {
    this.debouncedFetch();
  }
  async fetchPokeList() {
    if (!this.query) {
      this.pokeList = [];
      return;
    }
    const response = await axios.get("pokemon/fuzzyTerm", {
      params: {
        query: this.query
      }
    });
    this.pokeList = response.data;
  }
  debouncedFetch = debounce(this.fetchPokeList, 100);
}
</script>