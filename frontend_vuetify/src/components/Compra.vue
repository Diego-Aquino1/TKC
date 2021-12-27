<template>
<v-app>
  <v-main class="blue-grey lighten-2">
  <v-container fill-height>

        <v-layout row wrap align>
          <v-card
          height="600" text-h4 class="mx-auto my-12 text-center" width="400" outlined elevation="20">
          <v-form
            ref="form"
            v-model="valid"
            lazy-validation
          >
          <br>
            <v-text-field
              class="mx-10"
              v-model='newTask.ID_Orden'
              :rules="nameRules"
              label="ID_Orden"
              required
            ></v-text-field>

            <v-text-field
              class="mx-10"
              v-model='newTask.DNI'
              :rules="nameRules"
              label="DNI"
              required
            ></v-text-field>

            <v-text-field
              class="mx-10"
              v-model='newTask.ID_Metodo_de_pago'
              :rules="nameRules"
              label="Metodo_de_pago"
              required
            ></v-text-field>

            <v-text-field
              class="mx-10"
              v-model='newTask.ID_Comprobante_de_pago'
              :rules="nameRules"
              label="Comprobante_de_pago"
              required
            ></v-text-field>

            <v-text-field
              class="mx-10"
              v-model='newTask.ID_Domicilio'
              :rules="nameRules"
              label="Domicilio"
              required
            ></v-text-field>
            <br>
            <v-text-field
              class="mx-10"
              v-model='newTask.Total'
              :rules="nameRules"
              label="Total"
              required
            ></v-text-field>
            <br>
            <v-btn
              :disabled="!valid"
              color="success"
              class="mr-4"
              @click="addTask"
            >
              COMPRAR !!!
            </v-btn>

            <v-btn
              color="error"
              class="mr-4"
              @click="reset"
            >
              Reset
            </v-btn>    
          </v-form>
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
            axios.post(this.postURL + '/task/add_pago', this.newTask, this.config_request)
                .then(res => {                                         
                    this.tasks.push(res.data);
                    console.log(res.data)        ;
                })
                .catch((error) => {
                    console.log(error)
                });

            this.newTask = {};
        },
        reset(){                      
            this.newTask = {};
        }
    },

}
</script>