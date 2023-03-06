<template>

   <v-row justify="center" class="mt-4">
        <v-col cols="10" >    
            <v-card height="500" color="lime-lighten-4" class="mb-10 articleCard">
                <v-card-title class="text-h4 text-center mt-4" >
                    {{ article.title }}
                </v-card-title>
                
                <v-card-text class="text-center mt-4">
                    {{ article.content }}
                </v-card-text>
                                    
            
               
            </v-card>
            
            <router-link :to="{name: 'CommentCreateView',params: {id: articleId}}">
                <v-btn color="purple" class="mb-1" 
                    :style="{left: '50%', bottom: '5%', transform:'translateX(-50%)'}">
                        Comment 
                </v-btn>
            </router-link>
        </v-col>
    </v-row>

    <v-row justify="center" class="mb-10">
        <h1 class="mt-n10"> Comments </h1>
    </v-row>

     <v-row v-for=" (comment,index) in article.comments" justify="center" class="mt-n6">
        <v-col cols="10" >

            <v-card height="60" color="lime-lighten-4" class="mb-5 commentCard ">        
             {{ comment.author.username }} : 
                
               <v-card-title class="text-center">
                <p> {{ comment.comment }} </p> 
               </v-card-title>
              
                                    
            </v-card>
        </v-col>
    </v-row>

</template>

<script>
import axios from 'axios';
export default{
  
    data() {
        return{
            article: {},
            articleId: this.$route.params.id,
        }
    },
    mounted(){
        axios
        .get('http://127.0.0.1:8000/api/v1/articles/'+this.articleId+'/',
        )
        .then(response => (this.article = response.data))
   },
}
</script>

<style scoped>
h1,h2{
    color: rgb(42, 137, 137);
    text-align: center;
  
}
.articleCard {
    border-left: 6px solid rgb(138, 100, 173) !important;
    border-right: 6px solid rgb(138, 100, 173) !important;
    border-radius: 25px 0 25px 0;
}
.commentCard {
    border-left: 6px solid rgb(138, 100, 173) !important;
    border-right: 6px solid rgb(138, 100, 173) !important;
    border-radius: 2px 4px 2px 4px;
}
</style>