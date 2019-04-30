<template>
  <v-container fluid grid-list-lg>
    <div class="display-3 text-xs-center mb-3">あいまい単語検索</div>
    <v-layout row wrap style="max-width:600px;margin:auto;">
      <v-flex xs12>
        <v-text-field v-model="query" label="検索条件" required @input="onInput"></v-text-field>
      </v-flex>
      <v-flex xs12>
        <v-subheader>検索結果</v-subheader>
        <v-card
          style="cursor:pointer;"
          v-for="(pokemon, index) in pokeList"
          :key="index"
          @click="_window.open(`http://pokemon-wiki.net/${pokemon.name}`);"
        >
          <v-avatar :tile="false">
            <img :src="getUri(pokemon)" alt="404">
          </v-avatar>
          {{pokemon.name}}
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { debounce } from "lodash";
import { Pokemon } from "@/types";
import axios from "axios";

@Component
export default class TermSearch extends Vue {
  query: string = "";
  pokeList: Array<Pokemon> = [];
  _window!: Window;
  _debouncedFetch!: Function;
  onInput() {
    this._debouncedFetch();
  }
  fetchPokeList() {
    if (!this.query) {
      this.pokeList = [];
      return;
    }
    axios
      .get("api/fuzzyTerm", {
        params: {
          query: this.query
        }
      })
      .then(response => {
        this.pokeList = response.data;
      });
  }
  getUri(pokemon: Pokemon): string {
    const no = ("000" + pokemon.no).slice(-3);
    return `/assets/pokemon/${no}MS.png`;
  }
  mounted() {
    this._debouncedFetch = debounce(this.fetchPokeList, 500);
    this._window = window;
  }
}
</script>