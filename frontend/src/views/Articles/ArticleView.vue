<template>

   <v-row justify="center" class="mt-4">
        <v-col cols="10" >    
            <v-card height="500" color="lime-lighten-4" class="mb-10 card1">
                <v-card-title class="text-h4 text-center mt-4" >
                    {{ article.title }}
                </v-card-title>
                
                <v-card-text class="text-center mt-4">
                    {{ article.content }}
                </v-card-text>
                    
              
                  
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

.card1 {
    border-left: 6px solid rgb(138, 100, 173) !important;
    border-right: 6px solid rgb(138, 100, 173) !important;
    border-radius: 25px 0 25px 0;
}

</style>