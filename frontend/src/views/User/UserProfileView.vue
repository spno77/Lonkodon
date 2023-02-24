<template>
    <h1>User profile </h1>
    
    <div class="card">
        <v-card width="840" class="ma-auto">
            <v-row>
                <v-col>
                    <h2 class="ma-3">Firsname: <b class="ma-3"> {{ user.firstname  }} </b>  </h2> 
                    <h2 class="ma-3">Lastname: <b class="ma-1"> {{ user.lastname   }} </b>  </h2>
                    <h2 class="ma-3">Email:    <b class="ma-4"> {{   user.email    }} </b>  </h2>
                </v-col>
       
                <v-col>
                    <h2 class="ma-3">Phone:     <b class="ma-3"> {{ user.phone      }} </b>  </h2>  
                    <h2 class="ma-3">Employment:<b class="ma-3"> {{ user.employmen  }} </b>  </h2>
                    <h2 class="ma-3">Position:  <b class="ma-3"> {{ user.position   }} </b>  </h2>
                </v-col>
            </v-row>
        </v-card>
   </div>

</template>

<script>

import axios from 'axios';

export default{
   name: 'Profile',
   data(){
       return{
           id: this.$route.params.id,
           user: {},
       }
   },
   mounted(){
        axios
            .get(`http://127.0.0.1:8000/api/v1/users/${ this.id }/`)
            .then(response => (this.user = response.data))
    }
}

</script>

<style scoped>
  
  h2,p{
   color: rgb(40, 151, 151);
  }

  h1 {
   color: rgb(42, 137, 137);
   text-align: center;
   margin-top: 40px;
  }

  b {
   color: rgb(34, 118, 118);
  }
  .card {
   margin-top: 40px;
  }

</style>
