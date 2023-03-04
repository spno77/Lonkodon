<template>
    <h1 class="mt-5"> Recommended Users </h1>
   
    <v-container class="cont" >
        <v-row justify="center">
            <v-col cols="8">
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

    <v-container>
        <v-row>        
            <v-col mt-2 cols="6" v-for="(user, index) in pagedUsers" :key="index">
                <v-card 
                    color="cyan"
                    height="100%"
                    class="myCard"
                >

                    <v-card-title class="text-h4 text-md-center" >
                        {{ user.username }}
                    </v-card-title>

                    <v-img class="myImage" :height="140" :src="user.image"></v-img>

                    <v-col>
                        <div class="connInfo">
                            <div>  
                                {{ user.firstname  }} 
                                {{ user.lastname   }} 
                            </div>
               
                            <div> {{ user.employment }} </div>
                    
                        </div>
                   </v-col>
                   
                   <v-btn color="purple-darken-4" @click="connect(user.id,index)" :style="{left: '50%', bottom: '5%', transform:'translateX(-50%)'}">
                        Connect
                    </v-btn>

                        
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>


<script>
import axios from 'axios';
import { mapState, mapStores } from 'pinia';
import { useAppStore } from '@/store/app';
export default{
  
data() {
    return{ 
        users:       [],
        pageSize:    4,
        pageNo:      1,
    }
},
methods:{
    connect(userId,index){
        axios.
            post('http://127.0.0.1:8000/api/v1/connections/',{
                source: this.user.id,
                target: userId,
                is_approved: "false" 
            },
                { headers: {'Authorization': 'Bearer ' + this.user.access_token }}  
            )
            this.users.splice(index,1)
    }
    
},
computed:{
    ...mapStores(useAppStore),
    ...mapState(useAppStore,['user']),

    numPages() {
        return Math.ceil(this.users.length / this.pageSize);
    },
    pagedUsers() {      
        const startIndex = (this.pageNo - 1) * this.pageSize;
        const data = [...this.users];
        return data.splice(startIndex, this.pageSize);
    }
},
mounted(){
    axios
        .get('http://127.0.0.1:8000/api/v1/connections/find/',
            { headers: {'Authorization': 'Bearer ' + this.user.access_token }}  
        )
        .then(response => (this.users = response.data))
   },
}
</script>

<style scoped>
h1,h2{
    color: rgb(42, 137, 137);
    text-align: center;
    margin-top: 40px;
}
.myImage{
    margin-left: -35%;
}
.connInfo{
    margin-left: 320px;
    font-size: 25px;
    position: absolute;
    margin-top: -110px;
}
.myCard {
    border-left: 6px solid rgb(138, 100, 173) !important;
    border-right: 6px solid rgb(138, 100, 173) !important;
    border-radius: 25px 0 25px 0;
}
</style>