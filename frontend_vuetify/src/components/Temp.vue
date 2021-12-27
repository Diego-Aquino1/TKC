<template>
  <v-app>
    

    <v-app-bar
      app
      color="white"
    >
      <v-container class="py-0 fill-height">
        <v-avatar
          class="mr-10"
          color="grey darken-1"
          size="32"
        ></v-avatar>

        <v-btn
          elevation="2"
          class="mx-auto"
          link @click="$router.push({ path: '/' })"
        >REGISTRA TU ASISTENCIA !!!</v-btn>

        <v-spacer></v-spacer>

        <v-responsive max-width="260">
          <v-text-field
            dense
            flat
            hide-details
            rounded
            solo-inverted
          ></v-text-field>
        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      app
      width="300"
    >
      <v-sheet
        color="grey lighten-5"
        height="35"
        width="100%"
      ></v-sheet>

      <img 
        class="d-block text-center mx-auto mb-9"
        height = "250"
        width = "200"
        src="@/img/logo_unsa.png"
        alt="UNSA"
      >

      <v-sheet
        color="grey lighten-5"
        height="28"
        width="100%"
      ></v-sheet>
      <v-card-title
        rounded
        color="white"
        elevation="24"
        class="d-block text-center mx-auto mb-9"
      >
      ASSISTANCE BY FACE</v-card-title>

      <v-list
        class="pl-14"
        shaped
      >
        <v-list-item
            v-for="item in items"
            :key="item.title"
            link @click="$router.push({ path: item.route })"
            
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
    </v-navigation-drawer>

    

    <v-main>
      <!--<Task/>-->
      <router-view></router-view>
    </v-main>
  </v-app>
</template>


<script>

export default {
  name: 'App',


  data: () => ({
    //
    items: [
          { title: 'Login', icon: 'mdi-view-dashboard', route:'/' },
          { title: 'Admin', icon: 'mdi-view-dashboard', route:'/admin' },
          { title: 'Calendar', icon: 'mdi-calendar', route:'/calendar' },
          { title: 'Camara', icon: 'mdi-camera', route:'/camera' },
          { title: 'Cursos', icon: 'mdi-book', route:'/cursos' },
          { title: 'Estudiantes', icon: 'mdi-account', route:'/alumnos' },
          { title: 'Profesores', icon: 'mdi-account-box', route:'/profesores' },
          { title: 'About us', icon: 'mdi-account-group', route:'/aboutus' },
        ]
  }),
};
</script>
