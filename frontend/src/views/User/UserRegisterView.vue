<template>
    <h1 class="text-md-center mt-5"> Registration </h1>
   
    <v-container class="mt-3" >
        <v-form>
            
            <v-row no-gutters >
                <v-col class="ma-2 pa-1">
                     <v-text-field color="cyan"
                    v-model="user.username"
                    label="Username"
                    ></v-text-field>
                </v-col>
 
                <v-col class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    v-model="user.email"
                    label="Email"
                    ></v-text-field>     
                </v-col>
            </v-row>
 
            <v-row no-gutters >
                <v-col class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    v-model="user.firstname"
                    label="Firstname"
                    ></v-text-field>
                </v-col>
 
                <v-col class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    v-model="user.lastname"
                    label="Lastname"
                    ></v-text-field>
                </v-col>
            </v-row>
 
            <v-row no-gutters >
                <v-col class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    v-model="user.phone"
                    label="Phone"
                    ></v-text-field>
                </v-col>
 
                <v-col class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    v-model="user.employment"
                    label="Employment"
                    ></v-text-field>
                </v-col>
            </v-row>
 

                <v-text-field
                    v-model="user.position"
                    label="Position"
                ></v-text-field>
 
            <v-row no-gutters >
                <v-col class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    type="password"
                    v-model="user.password1"
                    label="Password"
                    ></v-text-field>
                </v-col>
 
                <v-col class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    type="password"
                    v-model="user.password2"
                    label="Re-enter password"
                    ></v-text-field>
                </v-col>
            </v-row>
        </v-form>
 
    <v-btn color="cyan" rounded="lg"
         :style="{left: '50%', transform:'translateX(-50%)'}"> 
                    Register
    </v-btn>
     
    </v-container>
    
 </template>
 
 <script>
   export default {
    data(){
     return{
         user:{
             username:   '',
             email:      '',
             password1:  '',
             password2:  '',
             firstname:  '',
             lastname:   '',
             phone:      '',
             //image:      '',
             employment: '',
             position:   '',
         },
     }
    }
   }
 </script>
 
 <style scoped>
 
 h1{
     color: rgb(42, 137, 137); 
    }
 
 </style>