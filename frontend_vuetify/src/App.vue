<template>
  <v-app>
    
    <v-app-bar app>
      <v-row
        align="center"
        justify="space-around"
        class="text-h4 font-weight-bold"
      >
      <img
        class="my-1"
        height = "60"
        width = "230"
        src="@/img/logobarra.jpeg"
        alt="cocinaportada1"
      >
        TKC

        <v-btn
          elevation="2"
          link @click="$router.push({ path: '/' })"
        >
        Ingresa aquí
        </v-btn>

        <v-btn
          right
          x-small
          height=28
          link @click="$router.push({ path: '/aboutus' })"
          >
            Sobre nosotros
        </v-btn>

      </v-row>
      
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>

  </v-app>
</template>

<script>
import Inicio from './components/Inicio';
import Admin from './components/Admin';
import Especificaciones from './components/Especificaciones';
import User from './components/User';
import Compra from './components/Compra';
import AboutUs from './components/AboutUs';

export default {
  name: 'App',

  components: {
    Inicio,
    Admin,
    Especificaciones,
    User,
    Compra,
    AboutUs
  },
};
</script>