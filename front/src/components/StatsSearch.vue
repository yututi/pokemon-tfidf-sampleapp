<template>
  <v-container fluid grid-list-lg>
    <div class="display-3 text-xs-center mb-3">種族値検索</div>
    <v-layout row wrap style="max-width:1000px;margin:auto;">
      <v-flex xs12 md6>
        <v-subheader>検索条件</v-subheader>
        <div class="stat-slider">
          <label class="stat-label">HP</label>
          <v-slider v-model="hp" max="200" thumb-label="always" @input="onInput"></v-slider>
        </div>
        <div class="stat-slider">
          <label class="stat-label">こうげき</label>
          <v-slider v-model="attack" max="200" thumb-label="always" @input="onInput"></v-slider>
        </div>
        <div class="stat-slider">
          <label class="stat-label">ぼうぎょ</label>
          <v-slider v-model="defence" max="200" thumb-label="always" @input="onInput"></v-slider>
        </div>
        <div class="stat-slider">
          <label class="stat-label">とくこう</label>
          <v-slider v-model="spAtk" max="200" thumb-label="always" @input="onInput"></v-slider>
        </div>
        <div class="stat-slider">
          <label class="stat-label">とくぼう</label>
          <v-slider v-model="spDef" max="200" thumb-label="always" @input="onInput"></v-slider>
        </div>
        <div class="stat-slider">
          <label class="stat-label">すばやさ</label>
          <v-slider v-model="speed" max="200" thumb-label="always" @input="onInput"></v-slider>
        </div>
      </v-flex>
      <v-flex xs12 md6>
        <v-subheader>検索結果</v-subheader>
        <poke-card v-for="(pokemon, index) in pokeList" :key="index" :pokemon="pokemon"/>
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
    components:{
        PokeCard: () => import("./PokeCard.vue")
    }
})
export default class StatsSearch extends Vue {
  hp: number = 100;
  attack: number = 100;
  defence: number = 100;
  spAtk: number = 100;
  spDef: number = 100;
  speed: number = 100;
  pokeList: Array<Pokemon> = [];
  onInput() {
    this.debouncedFetch();
  }
  async fetchPokeList() {
    const response = await axios
      .get("pokemon/similarStats", {
        params: {
          hp: this.hp,
          attack: this.attack,
          defence: this.defence,
          spAttack: this.spAtk,
          spDefence: this.spDef,
          speed: this.speed
        }
      });
    this.pokeList = response.data;
  }
  debouncedFetch = debounce(this.fetchPokeList, 200)
  getUri(pokemon: Pokemon): string {
    const no = ("000" + pokemon.no).slice(-3);
    return `/assets/pokemon/${no}.jpg`;
  }
  mounted() {
    this.fetchPokeList();
  }
}
</script>
<style lang="stylus">
.stat-slider {
  display: flex;
  align-items: center;

  .stat-label {
    width: 80px;
    text-align: center;
  }
}
</style>
