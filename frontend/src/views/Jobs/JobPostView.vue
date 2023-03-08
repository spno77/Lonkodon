<template>
    <h1 class="text-md-center mt-10"> Post Job </h1>
   
    <v-container class="mt-3" >
        <v-form>
            
            <v-row no-gutters >
                <v-col class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    v-model="job.title"
                    label="Job title"
                    ></v-text-field>
                </v-col>
 
                <v-col class="ma-2 pa-1">
                    <v-select color="cyan"
                    v-model="job.level"
                    :items="items"
                    label="Level"
                    ></v-select>     
                </v-col>
            </v-row>
 
            <v-row no-gutters >
                <v-col class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    v-model="job.description"
                    label="Description"
                    ></v-text-field>
                </v-col>
 
                <v-col class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    v-model="job.experience"
                    label="Experience"
                    ></v-text-field>
                </v-col>
            </v-row>
        </v-form>
 
        <v-btn @click.prevent="onSubmit" color="cyan" rounded="lg"
            :style="{left: '50%', transform:'translateX(-50%)'}"> 
                        Post
       </v-btn>
        
    </v-container>

</template>

<script>
import axios from 'axios';
import { mapState, mapStores } from 'pinia';
import { useAppStore } from '@/store/app';
    export default {
        data(){
            return {
                job:{
                    title:       '',
                    level:       '',
                    description: '',
                    experience:  '',
                    poster:      '',
                },
                items: [
                    'entry',
                    'junior',
                    'mid',
                    'senior',
                ],
            }
        },

        methods: {

            onSubmit() {
                const fd = new FormData()
                fd.append('title'       ,this.job.title)
                fd.append('level'       ,this.job.level)
                fd.append('description' ,this.job.description)
                fd.append('experience'  ,this.job.experience)
                
                axios
                    .post('http://127.0.0.1:8000/api/v1/jobs/',fd,
                        { headers: {'Authorization': 'Bearer ' + this.user.access_token }}, 
                    )
                    .then( response => {
                        alert("Job " + this.job.title  +" successfully created")
                    })
                    .catch((err) => {
                        console.log(err.response.data); 
                    });
                    this.$router.push('/jobs')
            },
        },

        computed:{
            ...mapStores(useAppStore),
            ...mapState(useAppStore,['user']),  
        },
  }
   

 </script>
 
<style scoped>
 
h1{
    color: rgb(42, 137, 137); 
}
 
</style>
