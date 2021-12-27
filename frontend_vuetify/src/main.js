import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

// router ///////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////
import VueRouter from 'vue-router'
Vue.use(VueRouter);


import Inicio from './components/Inicio'
import Admin from './components/Admin'
import Especificaciones from './components/Especificaciones'
import User from './components/User'
import Compra from './components/Compra'
import AboutUs from './components/AboutUs'

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { // primero muestra el componente Inicio
      path: '/',
      component: Inicio
    },
    {
      path: '/admin',
      component: Admin
    },
    {
      path: '/specs',
      component: Especificaciones
    },
    {
      path: '/user',
      component: User
    },
    {
      path: '/compra',
      component: Compra
    },
    { // About Us
      path: '/aboutus',
      component: AboutUs
    }
  ]
});
/////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
