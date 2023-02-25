<template>
    <h1>My messages</h1>
    
    <div v-for="message in messages">
        <v-alert class="myAlert" color="cyan" width="640">
            {{ message.message }}
        </v-alert>
    </div>

 </template>

<script>
import axios from 'axios';
import { mapState, mapStores } from 'pinia';
import { useAppStore } from '@/store/app';

export default{

data() {
    return{
        messages:   [],
        perPage:     3,
        currentPage: 1,
    }
},

computed:{
    ...mapStores(useAppStore),
    ...mapState(useAppStore,['user']),

    rows(){
        return this.messages.length
    },

    pageCount(){
        return this.messages.length / this.perPage
    }

},

mounted(){
    axios
        .get('http://127.0.0.1:8000/api/v1/messages/',
            {headers: {'Authorization': 'Bearer ' + this.user.access_token}}  
        )
        .then(response => (this.messages = response.data))
   },
}
</script>


<style scoped>

h1{
    color: rgb(42, 137, 137);
    text-align: center;
    margin-top: 40px;
}

.myAlert{
    margin-top: 20px;
    margin-left: 20px;
}

</style>
