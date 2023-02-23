<template>
    <h1>User profile </h1>
    
    <div class="card">
        <v-card width="840" class="ma-auto">
            <v-row>
                <v-col>
                    <h2 class="ma-3">Firsname: <b class="ma-3"> Rand  </b>  </h2> 
                    <h2 class="ma-3">Lastname: <b class="ma-1"> rand </b>  </h2>
                    <h2 class="ma-3">Email:<b class="ma-4"> rand@yahoo.com     </b>  </h2>
                </v-col>
       
                <v-col>
                    <h2 class="ma-3">Phone:</h2> 
                    <h2 class="ma-3">Employment:</h2>
                    <h2 class="ma-3">Position:</h2>   
                </v-col>
            </v-row>
        </v-card>
   </div>

</template>

<script>

export default{
   name: 'Profile',
   data(){
       return{
           
       }
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
