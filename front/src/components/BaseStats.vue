<template>
  <v-container fluid grid-list-lg>
    <div class="display-3 text-xs-center mb-3">種族値類似検索</div>
    <v-layout row wrap>
      <v-flex xs2 md1>
        <div class="stat-label">HP</div>
        <div class="stat-label">こうげき</div>
        <div class="stat-label">ぼうぎょ</div>
        <div class="stat-label">とくこう</div>
        <div class="stat-label">とくぼう</div>
        <div class="stat-label">すばやさ</div>
      </v-flex>
      <v-flex xs10 md6>
        <v-slider v-model="hp" max="200" thumb-label="always" @input="onInput"></v-slider>
        <v-slider v-model="attack" max="200" thumb-label="always" @input="onInput"></v-slider>
        <v-slider v-model="defense" max="200" thumb-label="always" @input="onInput"></v-slider>
        <v-slider v-model="spAtk" max="200" thumb-label="always" @input="onInput"></v-slider>
        <v-slider v-model="spDef" max="200" thumb-label="always" @input="onInput"></v-slider>
        <v-slider v-model="speed" max="200" thumb-label="always" @input="onInput"></v-slider>
      </v-flex>
      <v-flex xs12 md6>
        <v-card v-for="pokemon in pokeList" :key="pokemon.name">
          <v-avatar tile="false">
            <img :src="pokemon.imgUrl" alt="avatar">
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
@Component
export default class BaseStats extends Vue {
  hp: number = 100;
  attack: number = 100;
  defense: number = 100;
  spAtk: number = 100;
  spDef: number = 100;
  speed: number = 100;
  pokeList: Array<Pokemon> = [];
  onInput() {
    debounce(this.fetchPokeList, 300, { maxWait: 1000 });
  }
  async fetchPokeList() {
    const response = await fetch(`/similar_poke?\
        hp=${this.hp}&\
        attack=${this.attack}&\
        defense=${this.defense}&\
        spAtk=${this.spAtk}&\
        spDef=${this.spDef}&\
        speed=${this.speed}`);

    if (response.ok) {
      this.pokeList = await response.json();
    }
    throw new Error("fetch failed.");
  }
}
</script>
<style>
.stat-label {
  margin-top: 16px;
  height: 52px;
  text-align: center;
}
</style>
