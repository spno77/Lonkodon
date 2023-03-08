<template>

    <v-text-field
        class="myInput mt-n16" 
        color="cyan"
        v-model="message"
        label="Reply"
    ></v-text-field>

    <v-btn class="myButton" @click="replyMessage()"
        color="cyan" rounded="lg"
        :style="{left: '50%', transform:'translateX(-50%)'}"
    > 
        Send
    </v-btn>

</template>

<script>
import axios from 'axios';
import { mapState, mapStores } from 'pinia';
import { useAppStore } from '@/store/app';

export default{

data(){
    return{
        message: ""
    }
},

props:['receiver'],

methods:{

    replyMessage(){
        axios.
            post('http://127.0.0.1:8000/api/v1/messages/',{
                message:  this.message,
                sender:   this.user.id,
                receiver: this.receiver
            },
                {headers: {'Authorization': 'Bearer ' + this.user.access_token}}  
            )
            .catch((err) => {
                console.log(err.response.data);
            })

            this.message = ""
    }
},

computed:{
    ...mapStores(useAppStore),
    ...mapState(useAppStore,['user'])
},

}

</script>

<style scoped>
.myInput{
    height: 650px;
    width: 250px;
    margin-top: 10 px;
    margin-right: 40px;

}
.myButton{
    margin-top: -550px;
}

h1{
    color: rgb(42, 137, 137); 
}

</style>