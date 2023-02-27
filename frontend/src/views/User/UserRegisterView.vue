<template>
    <h1 class="text-md-center mt-10"> Registration </h1>
   
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
 
            <v-row no-gutters >
                <v-col class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    v-model="user.position"
                    label="Position"
                    ></v-text-field>
                </v-col>
 
                <v-col class="ma-2 pa-1">
                    <v-file-input 
                    @change="onFileSelected" prepend-icon="" 
                    v-model="user.image" 
                    label="Upload image">
                    </v-file-input>
                </v-col>
            </v-row>
 
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
 
        <v-btn @click.prevent="onSubmit" color="cyan" rounded="lg"
            :style="{left: '50%', transform:'translateX(-50%)'}"> 
                        Register
       </v-btn>
        
     
    </v-container>

</template>

<script>
import axios from 'axios';
    export default {
        data(){
            return {
                user:{
                    username:   '',
                    email:      '',
                    password1:  '',
                    password2:  '',
                    firstname:  '',
                    lastname:   '',
                    phone:      '',
                    image:      '',
                    employment: '',
                    position:   '',
                },
            }
        },
        methods: {

            onFileSelected(event){
                this.user.image = event.target.files[0]     
            },
      
            onSubmit() {
                const fd = new FormData()
                fd.append('username'   ,this.user.username)
                fd.append('firstname'  ,this.user.firstname)
                fd.append('lastname'   ,this.user.lastname)
                fd.append('phone'      ,this.user.phone)
                fd.append('email'      ,this.user.email)
                fd.append('password1'  ,this.user.password1)
                fd.append('password2'  ,this.user.password2)
        
                fd.append('employment' ,this.user.employment)
                fd.append('position'   ,this.user.position)
                fd.append('image'      ,this.user.image,this.user.image.name)
       
                axios
                    .post('http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/',fd)
                    .then( response => {
                        alert("User " + this.user.username  +" successfully registered")
                        this.$router.push('/login')
                    })
                    .catch((err) => {
                        console.log(err.response.data);
                        if(err.response.data.username){
                            alert(err.response.data.username)
                        }
                        if(err.response.data.email){
                            alert(err.response.data.email)
                        }
                        if(err.response.data.non_field_errors){
                            alert(err.response.data.non_field_errors)
                        }  
                    });
            },
        }
  }
   

 </script>
 
<style scoped>
 
h1{
    color: rgb(42, 137, 137); 
}
 
</style>
