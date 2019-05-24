<template>
  <v-dialog v-model="isOpen">
    <v-card class="white--primary">
      <v-layout>
        <v-flex xs5>
          <v-img :src="pokemon.getImgUri()" height="125px" contain></v-img>
        </v-flex>
        <v-flex xs7>
          <v-card-title primary-title>
            <div>
              <div class="headline">{{pokemon.name}}</div>
              <div>タイプ：{{pokemon.types.join(", ")}}</div>
              <div>とくせい：{{pokemon.abilities.join(", ")}}</div>
            </div>
          </v-card-title>
        </v-flex>
      </v-layout>
      <v-divider light></v-divider>
      <v-card-actions class="pa-3">
          <v-button @click="close">close</v-button>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";
import { Pokemon } from "@/types";
import axios from "axios";

@Component
export default class PokeDetailDialog extends Vue {
  isOpen: boolean = false;
  pokemon: Pokemon = new Pokemon({});

  open(pokemon: Pokemon) {
    this.isOpen = true;
    this.pokemon = pokemon;
  }
  close(){
      this.isOpen = false;
      this.pokemon = new Pokemon({});
  }
  mounted() {}
}
</script>
<style lang="stylus"></style>
