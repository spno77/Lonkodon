
<template>
    <h1 class="mt-5"> My Requests </h1>
   
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
            <v-col mt-2 cols="6" v-for="(connection, index) in pagedConnections" :key="index">
                <v-card 
                    color="cyan"
                    height="100%"
                >

                    <v-card-title class="text-h4 text-md-center" >
                        {{ connection.source.username }}
                    </v-card-title>

                    <v-img class="myImage" :height="140" :src="connection.source.image"></v-img>

                    <v-col>
                        <div class="connInfo">
                            <div>  
                                {{ connection.source.firstname  }} 
                                {{ connection.source.lastname   }} 
                            </div>
               
                            <div> {{ connection.source.employment }} </div>
                    
                        </div>
                   </v-col>

                        <v-row justify="center" class="mb-2">
                            <v-btn color="success" @click="acceptRequest(connection.target,connection.id,index)">
                                Accept
                            </v-btn>
                            <v-btn color="red" @click="declineRequest(connection.id,index)" class="ml-6">
                                Decline
                            </v-btn>
                        </v-row>
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
        connections: [],
        pageSize:    4,
        pageNo:      1,
    }
},
methods:{
    acceptRequest(sourceId,requestId,index){
        axios
            .put('http://127.0.0.1:8000/api/v1/connections/'+ requestId + '/',{
                target: sourceId ,
                is_approved: "true" ,
            },
                {headers: {'Authorization': 'JWT ' + this.user.access_token}} 
            )
        this.connections.splice(index,1)
       
    },
    declineRequest(requestId,index){
        axios
            .delete('http://127.0.0.1:8000/api/v1/connections/'+ requestId + '/',
                {headers: {'Authorization': 'Bearer ' + this.user.access_token}} 
            )
        this.connections.splice(index,1)
    },
},
computed:{
    ...mapStores(useAppStore),
    ...mapState(useAppStore,['user']),
    numPages() {
        return Math.ceil(this.connections.length / this.pageSize);
    },
    pagedConnections() {      
        const startIndex = (this.pageNo - 1) * this.pageSize;
        const data = [...this.connections];
        return data.splice(startIndex, this.pageSize);
    }
},
mounted(){
    axios
        .get('http://127.0.0.1:8000/api/v1/conn_requests/',
            { headers: {'Authorization': 'Bearer ' + this.user.access_token }}  
        )
        .then(response => (this.connections = response.data))
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
.cont{
    margin-top: -20px;
}
</style>