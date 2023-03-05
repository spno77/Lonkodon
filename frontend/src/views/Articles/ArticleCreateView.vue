<template>
    <h1 class="text-md-center mt-10"> Create Article </h1>
   
    <v-container class="mt-3" >
        <v-form>
            
            <v-row justify="center">
                <v-col cols="5" class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    v-model="article.title"
                    label="Tile"
                    ></v-text-field>
                </v-col>
            </v-row>
 
            <v-row no-gutters >
                <v-col class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    class="content"
                    v-model="article.content"
                    label="Write article"
                    ></v-text-field>
                </v-col>
            </v-row>

        </v-form>
 
        <v-btn class="mt-n16" @click.prevent="onSubmit" color="cyan" rounded="lg"
            :style="{left: '50%', transform:'translateX(-50%)'}"> 
                        Create
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
                article:{
                    title:       '',
                    content:      '',
                },
            }
        },

        methods: {

            onSubmit() {
                const fd = new FormData()
                fd.append('title'   ,this.article.title)
                fd.append('content' ,this.article.content)
         
                axios
                    .post('http://127.0.0.1:8000/api/v1/articles/',fd,
                        { headers: {'Authorization': 'Bearer ' + this.user.access_token }}, 
                    )
                    .then( response => {
                        alert("Article " + this.article.title  +" successfully created")
                    })
                    .catch((err) => {
                        console.log(err.response.data); 
                    });
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

.content{
    height: 450px;
}
 
</style>
