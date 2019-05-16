<template>
  <v-card
    class="poke-card"
    :class="{'show-stats':showStats && isHovered}"
    @mouseenter="isHovered = true"
    @mouseleave="isHovered = false"
  >
    <v-avatar :tile="false">
      <img :src="getUri(pokemon)" alt="404">
    </v-avatar>
    <div class="poke-card-body">
      <label class="text-center">{{pokemon.name}}</label>
      <div v-if="showStats" class="stats">
        <div class="poke-stat">
          <div class="stat-label">HP</div>
          <div>{{pokemon.stats.hp}}</div>
        </div>
        <div class="poke-stat">
          <div class="stat-label">こうげき</div>
          <div>{{pokemon.stats.attack}}</div>
        </div>
        <div class="poke-stat">
          <div class="stat-label">ぼうぎょ</div>
          <div>{{pokemon.stats.defence}}</div>
        </div>
        <div class="poke-stat">
          <div class="stat-label">とくこう</div>
          <div>{{pokemon.stats.spAttack}}</div>
        </div>
        <div class="poke-stat">
          <div class="stat-label">とくぼう</div>
          <div>{{pokemon.stats.spDefence}}</div>
        </div>
        <div class="poke-stat">
          <div class="stat-label">すばやさ</div>
          <div>{{pokemon.stats.speed}}</div>
        </div>
      </div>
    </div>
  </v-card>
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

  isHovered: boolean = false;

  getUri(pokemon: Pokemon): string {
    const no = ("000" + pokemon.no).slice(-3);
    return `/assets/pokemon/${no}.jpg`;
  }
}
</script>
<style lang="stylus">
.poke-card {
  display: flex;

  .poke-card-body {
    position: relative;
    flex: 1;

    .stats {
      position: absolute;
      right: 0;
      top: 0;
      width: 0px;
      height: 100%;
      display: flex;
      justify-content: space-around;
      overflow: hidden;
    }
  }

  &.show-stats {
    .stats {
      width: 100%;
    }
  }
}

.poke-stat {
  position: relative;
  flex-grow: 1;
  height: 100%;

  .stat-label {
    position: absolute;
    top: 0;
    left: 0;
    font-size: 12px;
    font-font-weight: 100;
  }
}

.text-center {
  dispay: flex;
  align-items: center;
  justify-content: center;
}
</style>
