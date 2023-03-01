<template>

  <h1> My Network </h1>
  
  <v-col class="ml-16">
    <router-link :to="{name: 'Requests'}">
        <v-btn color="indigo-darken-2"  class="ml-16"> 
            Requests
        </v-btn>
    </router-link>
  </v-col>
  
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

                    <router-link :to="{name: 'Profile',params: {id: connection.source.id}}">
                        <v-btn color="success" theme="dark" :style="{left: '50%', bottom: '5%', transform:'translateX(-50%)'}">
                            Profile
                        </v-btn>
                    </router-link>
          
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
        .get('http://127.0.0.1:8000/api/v1/connections/',
            { headers: {'Authorization': 'Bearer ' + this.user.access_token }}  
        )
        .then(response => (this.connections = response.data))
   },
}

</script>

<style scoped>

h1{
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
tree/main/backend.cont{
    margin-top: -20px;
}

</style>