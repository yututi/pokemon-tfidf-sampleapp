<template>
    <v-card>
        <v-avatar :tile="false">
        <img :src="getUri(pokemon)" alt="404">
        </v-avatar>
        {{pokemon.name}}
    </v-card>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import { Pokemon } from "@/types";

@Component
export default class PokeCard extends Vue {
  @Prop()
  pokemon!: Pokemon;
  
  getUri(pokemon: Pokemon): string {
    const no = ("000" + pokemon.no).slice(-3);
    return `/assets/pokemon/${no}.jpg`;
  }
}
</script>
