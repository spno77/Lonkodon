<template>

    <h1 class="mt-5">Top Articles</h1>

    <v-container class="cont" >
        <v-row justify="center">
            <v-col cols="10">
                <v-container class="max-width">
                    <v-pagination 
                        v-model="pageNo"
                        class="my-4"
                        :length="numPages"
                     ></v-pagination>
                </v-container>
            </v-col>
        </v-row>
    </v-container>

    

    <div v-for="(article, index) in pagedArticles" :key="index">

        <v-row justify="center" class="mt-n10">
            <v-col cols="9" >    
                <v-card color="lime-lighten-4" class="mb-10 card1">
                    <v-card-title class="text-h4 text-md-center" >
                        {{ article.title }}
                    </v-card-title>

                    <v-card-subtitle class="text-md-center mt-1">
                        <b> By:  {{ article.author.username }} </b>
                    </v-card-subtitle>

                    <v-col class="mb-2"> {{ article.date_created }} </v-col>

                    <router-link :to="{name: 'Article',params: {id: article.id}}">
                        <v-btn color="purple" class="mb-1" :style="{left: '50%', bottom: '5%', transform:'translateX(-50%)'}">
                            Read 
                        </v-btn>
                    </router-link>

                </v-card>
            </v-col>
        </v-row>

    </div>

</template>

<script>
import axios from 'axios';
import { mapState, mapStores } from 'pinia';
import { useAppStore } from '@/store/app';


export default{

components: {   
    
},

data() {
    return{
        articles:    [],
        pageSize:    5,
        pageNo:      1,
    }
},

methods:{
	

},

computed:{
    ...mapStores(useAppStore),
    ...mapState(useAppStore,['user']),

    numPages() {
        return Math.ceil(this.articles.length / this.pageSize);
    },

    pagedArticles() {      
        const startIndex = (this.pageNo - 1) * this.pageSize;
        const data = [...this.articles];

        return data.splice(startIndex, this.pageSize);
    }
},

mounted(){
    axios
        .get('http://127.0.0.1:8000/api/v1/articles/',
           
        )
        .then(response => (this.articles = response.data))
   },
}
</script>

<style scoped>
h1,h2{
    color: rgb(42, 137, 137);
    text-align: center;
  
}
.card1 {
    border-left: 6px solid rgb(138, 100, 173) !important;
    border-radius: 25px 0 0 0;
}

</style>
