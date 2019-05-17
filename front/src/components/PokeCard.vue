<template>
  <div class="poke-card" @click="openWiki(pokemon.name)">
    <v-avatar :tile="false">
      <img :src="getUri(pokemon)" alt="404">
    </v-avatar>
    <div class="poke-card-body">
      <label class="poke-label">{{pokemon.name}}</label>
      <div v-if="showStats" class="poke-stats primary white--text">
        <div class="poke-stat">
          <div class="stat-label">HP</div>
          <div class="stat-value">{{pokemon.stats.hp}}</div>
        </div>
        <div class="poke-stat">
          <div class="stat-label">こうげき</div>
          <div class="stat-value">{{pokemon.stats.attack}}</div>
        </div>
        <div class="poke-stat">
          <div class="stat-label">ぼうぎょ</div>
          <div class="stat-value">{{pokemon.stats.defence}}</div>
        </div>
        <div class="poke-stat">
          <div class="stat-label">とくこう</div>
          <div class="stat-value">{{pokemon.stats.spAttack}}</div>
        </div>
        <div class="poke-stat">
          <div class="stat-label">とくぼう</div>
          <div class="stat-value">{{pokemon.stats.spDefence}}</div>
        </div>
        <div class="poke-stat">
          <div class="stat-label">すばやさ</div>
          <div class="stat-value">{{pokemon.stats.speed}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import { Pokemon } from "@/types";

@Component
export default class PokeCard extends Vue {
  @Prop()
  pokemon!: Pokemon;
  @Prop({ default: false })
  showStats!: boolean;
  @Prop({ default: false })
  showWiki!: boolean;

  isHovered: boolean = false;

  getUri(pokemon: Pokemon): string {
    const no = ("000" + pokemon.no).slice(-3);
    return `/assets/pokemon/${no}.jpg`;
  }
  openWiki(pokemonName: string) {
    if (!this.showWiki) {
      return;
    }
    let pokename: string = pokemonName;
    if (pokename.lastIndexOf("メガ", 0) === 0) {
      pokename = pokename.substring(2);
    }
    window.open("http://pokemon-wiki.net/" + pokename);
  }
}
</script>
<style lang="stylus">
.poke-card {
  display: flex;
  transition: box-shadow 0.3s ease-out;

  .poke-card-body {
    position: relative;
    flex: 1;

    .poke-stats {
      position: absolute;
      right: 0;
      top: 0;
      width: 0px;
      height: 100%;
      display: flex;
      justify-content: space-around;
      overflow: hidden;
      transition: width 0.3s ease-out;
      will-change: width;
    }
  }

  &:hover {
    box-shadow: 0 1px 3px 1px rgba(50, 50, 50, 0.2);

    .poke-stats {
      width: 100%;
    }
  }
}

.poke-stat {
  position: relative;
  flex-grow: 1;
  height: 100%;
  min-width: 30px;

  .stat-label {
    position: absolute;
    top: 0;
    left: 0;
    font-size: 10px;
    padding-left: 0.3em;
    padding-top: 0.3em;
    font-weight: 100;
  }

  .stat-value {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
  }
}

.poke-label {
  height: 100%;
  display: flex;
  align-items: center;
}
</style>
