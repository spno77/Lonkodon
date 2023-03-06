<template>
    <h1 class="text-md-center mt-10"> New Comment </h1>
   
    <v-container class="mt-3" >
        <v-form>
            
            <v-row justify="center">
                <v-col cols="8" class="ma-2 pa-1">
                    <v-text-field color="cyan"
                    class="content"
                    v-model="comment.comment"
                    label="Tile"
                    ></v-text-field>
                </v-col>
            </v-row>

        </v-form>
 
        <v-btn class="mt-n16" @click.prevent="onSubmit" color="cyan" rounded="lg"
            :style="{left: '50%', transform:'translateX(-50%)'}"> 
                    Comment
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
        articleId: this.$route.params.id,
        comment:{},
    }
},

methods: {

    onSubmit() {
        const fd = new FormData()
        fd.append('comment'   ,this.comment.comment)
        fd.append('article'   ,this.articleId)
         
        axios
            .post('http://127.0.0.1:8000/api/v1/comments/',fd,
                { headers: {'Authorization': 'Bearer ' + this.user.access_token }}, 
            )
            .then( response => {
                alert("Comment " + this.comment.comment  +" successfully posted")
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
    height: 250px;
}
 
</style>
