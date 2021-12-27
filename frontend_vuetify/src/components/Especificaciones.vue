<template>
<v-app>
  <v-main class="blue-grey lighten-2">
  <v-container fill-height>
    <v-row
          align="center"
          justify="center"
          no-gutters
        >
          <v-dialog
             max-width="700px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="white"
                v-bind="attrs"
                v-on="on"
              >
                Agregar Especificaciones
              </v-btn>

            </template>
            <v-card>
              <br>
              <v-card-title>
                <span class="text-h5 mx-auto">Especificaciones</span>
              </v-card-title>
              <v-card-text class="text-h6 text-center">
                <v-text-field
                  class="mx-10"
                  v-model='newTask.ID_Cocina'
                  :rules="nameRules"
                  label="ID_Cocina"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Numero_de_quemadores'
                  :rules="nameRules"
                  label="Numero_de_quemadores"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Material_de_la_parrilla'
                  :rules="nameRules"
                  label="Material_de_la_parrilla"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Material_de_la_cubierta'
                  :rules="nameRules"
                  label="Material_de_la_cubierta"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Capacidad_del_horno'
                  :rules="nameRules"
                  label="Capacidad_del_horno"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Encendido_electronico'
                  :rules="nameRules"
                  label="Encendido_electronico"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Tipo_de_energia'
                  :rules="nameRules"
                  label="Tipo_de_energia"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Timer'
                  :rules="nameRules"
                  label="Timer"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Incluye_tapa'
                  :rules="nameRules"
                  label="Incluye_tapa"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Marca'
                  :rules="nameRules"
                  label="Marca"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Modelo'
                  :rules="nameRules"
                  label="Modelo"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Tipo'
                  :rules="nameRules"
                  label="Tipo"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Alto'
                  :rules="nameRules"
                  label="Alto"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Ancho'
                  :rules="nameRules"
                  label="Ancho"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Profundidad'
                  :rules="nameRules"
                  label="Profundidad"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Peso'
                  :rules="nameRules"
                  label="Peso"
                  required
                ></v-text-field>
                <v-text-field
                  class="mx-10"
                  v-model='newTask.Hecho_en'
                  :rules="nameRules"
                  label="Hecho_en"
                  required
                ></v-text-field>

              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="success"
                  class="mr-4"
                  @click="addTask"
                >
                  AGREGAR
                </v-btn>
              </v-card-actions>
              <br>
            </v-card>
          </v-dialog>
          <v-btn
            color="white"
            v-bind="attrs"
            v-on="on"
            link @click="$router.push({ path: '/admin' })"
          >
            Volver a cocinas
          </v-btn>
        </v-row>

      <v-layout row wrap align>
          <v-card
          height="650" text-h4 class="mx-auto my-2 text-center" width="1600" outlined elevation="20">
          <v-simple-table>
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-center">
                    ID Cocina
                  </th>
                  <th class="text-center">
                    Nro de quemadores
                  </th>
                  <th class="text-center">
                    Material de la parrilla
                  </th>
                  <th class="text-center">
                    Capacidad del horno
                  </th>
                  <th class="text-center">
                    Encendido electronico
                  </th>
                  <th class="text-center">
                    Tipo de energia
                  </th>
                  <th class="text-center">
                    Timer
                  </th>
                  <th class="text-center">
                    Incluye tapa
                  </th>
                  <th class="text-center">
                    Marca
                  </th>
                  <th class="text-center">
                    Modelo
                  </th>
                  <th class="text-center">
                    Tipo
                  </th>
                  <th class="text-center">
                    Alto
                  </th>
                  <th class="text-center">
                    Ancho
                  </th>
                  <th class="text-center">
                    Profundidad
                  </th>
                  <th class="text-center">
                    Peso
                  </th>
                  <th class="text-center">
                    Hecho en
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="task in tasks" :key="task"
                >
                    <td>{{ task.ID_Cocina }} </td>
                    <td>{{ task.Material_de_la_parrilla }} </td>
                    <td>{{ task.Numero_de_quemadores }} </td>
                    <td>{{ task.Material_de_la_parrilla }} </td>
                    <td>{{ task.Material_de_la_cubierta }} </td>
                    <td>{{ task.Capacidad_del_horno }} </td>
                    <td>{{ task.Encendido_electronico }} </td>
                    <td>{{ task.Tipo_de_energia }} </td>
                    <td>{{ task.Timer }} </td>
                    <td>{{ task.Incluye_tapa }} </td>
                    <td>{{ task.Marca }} </td>
                    <td>{{ task.Modelo }} </td>
                    <td>{{ task.Tipo }} </td>
                    <td>{{ task.Alto }} </td>
                    <td>{{ task.Ancho }} </td>
                    <td>{{ task.Profundidad }} </td>
                    <td>{{ task.Peso }} </td>
                    <td>{{ task.Hecho_en }} </td>
                    <td><v-btn
                        small
                        color="error"
                        dark
                        class="grey  mx-2"
                        v-on:click='deleteTask(task)'
                        @click="messages--"
                      >

                        <v-icon dark>
                          mdi-delete
                        </v-icon>
                      </v-btn>

                      </td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
          </v-card>
      </v-layout>
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
            postURL: 'http://127.0.0.1:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }       
        }
    },
    methods:{
        addTask(){ 
            axios.post(this.postURL + '/task/add_specification', this.newTask, this.config_request)
                .then(res => {                                         
                    this.tasks.push(res.data);
                    console.log(res.data)        ;
                })
                .catch((error) => {
                    console.log(error)
                });

            this.newTask = {};
        },

        deleteTask(task){                      
            axios.post(this.postURL + '/task/delete_specification', {CUI: task.CUI}, this.config_request)
                .then((res) => {                      
                    this.tasks.splice(this.tasks.indexOf(task), 1);                    
                })
                .catch((error) => {
                    console.log(error)
                });  
        },
        reset(){                      
            this.newTask = {};
        }
    },

    created(){ 
        axios.post(this.postURL + '/task/get_specifications')
            .then(res => { this.tasks = res.data; })
            .catch((error) => { console.log(error) })
    }

}
</script>