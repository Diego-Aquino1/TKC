<template>
  <v-app>    
    <v-main 
    class="blue-grey lighten-2"
    >
    
      <v-container fluid>
      <!--<Task/>-->
        <router-view></router-view>

          <v-row
            align="center"
            justify="center"
            no-gutters
          >
            <v-sheet
              color="white"
              elevation="9"
              height="680"
              width="1100"
              class="text-center"
            >
              <br><br>
              <v-row
                align="center"
                justify="center"
                no-gutters
              >
                <v-row
                  align="center"
                  justify="center"
                  no-gutters
                >
                  <v-dialog
                    max-width="600px"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                        x-large
                        color="white"
                        v-bind="attrs"
                        v-on="on"
                      >
                        USUARIOS
                      </v-btn>
                    </template>
                    <v-card>
                    <br>
                      <v-card-title>
                        <span class="text-h5">Iniciar Sesión - Usuarios</span>
                      </v-card-title>
                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="12">
                              <v-text-field
                                label="Nombre de usuario*"
                                required
                                v-model='newTask.Username'
                                :rules="nameRules"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12">
                              <v-text-field
                                label="Contraseña*"
                                type="password"
                                v-model='newTask.Password'
                                required
                              ></v-text-field>
                            </v-col>
                          </v-row>
                        </v-container>
                        <small>*Campos requeridos</small>
                      </v-card-text>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                          color="blue darken-1"
                          text
                          @click="addTask"
                        >
                          REGISTRARSE
                        </v-btn>
                        <v-btn
                          color="blue darken-1"
                          text
                          link @click="$router.push({ path: '/user' })"
                        >
                          INGRESAR
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-row>
                <v-divider
                  vertical
                ></v-divider>
                <v-row
                  align="center"
                  justify="center"
                  no-gutters
                >
                  <v-dialog
                    v-model="dialog"
                    max-width="600px"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                        x-large
                        color="white"
                        v-bind="attrs"
                        v-on="on"
                      >
                        ADMIN
                      </v-btn>
                    </template>
                    <v-card>
                    <br>
                      <v-card-title>
                        <span class="text-h5">Iniciar Sesión - Administradores</span>
                      </v-card-title>
                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="12">
                              <v-text-field
                                label="Nombre de usuario*"
                                required
                                v-model='newTask2.Username'
                                :rules="nameRules"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12">
                              <v-text-field
                                label="Contraseña*"
                                type="password"
                                required
                                v-model='newTask2.Password'
                                :rules="nameRules"
                              ></v-text-field>
                            </v-col>
                          </v-row>
                        </v-container>
                        <small>*Campos requeridos</small>
                      </v-card-text>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                          color="blue darken-1"
                          text
                          @click="addTask2"
                        >
                          REGISTRARSE
                        </v-btn>
                        <v-btn
                          color="blue darken-1"
                          text
                          link @click="$router.push({ path: '/admin' }), dialog = false"
                        >
                          INGRESAR
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-row>
              </v-row>
              <br>
              <v-sheet
                color="white"
                height="55"
                width="800"
                class="mx-auto my-auto text-h4 text-center font-weight-bold"
              >
              INICIA SESION !!!
              </v-sheet>
                  <img
                    height = "480"
                    width = "860"
                    src="@/img/portada.jpg"
                    alt="cocinaportada1"
                  >
            </v-sheet>
          </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios'

export default{    
    data(){ 
        return { 
            tasks: [],
            newTask: {},
            newTask2: {},
            postURL: 'http://127.0.0.1:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }       
        }
    },
    methods:{
        addTask(){ 
            axios.post(this.postURL + '/task/add_user', this.newTask, this.config_request)
                .then(res => {                                         
                    this.tasks.push(res.data);
                    console.log(res.data)        ;
                })
                .catch((error) => {
                    console.log(error)
                });

            this.newTask = {};
        },

        addTask2(){ 
            axios.post(this.postURL + '/task/add_admin', this.newTask2, this.config_request)
                .then(res => {                                         
                    this.tasks.push(res.data);
                    console.log(res.data)        ;
                })
                .catch((error) => {
                    console.log(error)
                });

            this.newTask2 = {};
        },

        created(){ 
            axios.post(this.postURL + '/task/get_students')
                .then(res => { this.tasks = res.data; })
                .catch((error) => { console.log(error) })
        }

    }
}
</script>