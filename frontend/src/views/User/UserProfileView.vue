<template>
<div>
    <h1> {{ userProfile.username }} </h1>

    <div v-show="showReply" class="message">
        <MessageSendView :receiver="msgSender"> </MessageSendView>
    </div>
    
    <div class="card">
        <v-card width="840" class="ma-auto">
            <v-row>
                <v-col>
                    <h2 class="ma-3">Firsname: <b class="ma-3"> {{ userProfile.firstname  }} </b>  </h2> 
                    <h2 class="ma-3">Lastname: <b class="ma-1"> {{ userProfile.lastname   }} </b>  </h2>
                    <h2 class="ma-3">Email:    <b class="ma-4"> {{ userProfile.email    }} </b>  </h2>
                </v-col>
       
                <v-col>
                    <h2 class="ma-3">Phone:     <b class="ma-3"> {{ userProfile.phone      }} </b>  </h2>  
                    <h2 class="ma-3">Employment:<b class="ma-3"> {{ userProfile.employment  }} </b>  </h2>
                    <h2 class="ma-3">Position:  <b class="ma-3"> {{ userProfile.position   }} </b>  </h2>
                </v-col>
            </v-row>
        </v-card>

        <v-btn class="mt-5" color="purple-darken-4" @click="showReplyTrue(); setSender(userProfile.id)" :style="{left: '50%', bottom: '5%', transform:'translateX(-50%)'}">
            Message
        </v-btn>
   </div>
</div>

</template>

<script>
import MessageSendView from '@/views/Messages/MessageSendView'
import axios from 'axios';
import { mapState, mapStores } from 'pinia';
import { useAppStore } from '@/store/app';

export default{

name: 'Profile',
   
components: {   
    MessageSendView
},
   
data(){
    return{
        id: this.$route.params.id,
        userProfile: {},
        showReply: false,
        msgSender:  0,
    }
},

methods:{
    showReplyTrue(){
        this.showReply = true   
    },
    
    showReplyFalse(){
        this.showReply = false
    },
    
    setSender(senderId){
        this.msgSender = senderId
    },

    printUser(){
        console.log(this.user)
    },
},

computed:{
    ...mapStores(useAppStore),
    
    ...mapState(useAppStore,['user']),

},

mounted(){
        axios
            .get(`http://127.0.0.1:8000/api/v1/users/${ this.id }/`)
            .then(response => (this.userProfile = response.data))
}

}
</script>

<style scoped>
  
h2,p{
    color: rgb(40, 151, 151);
}
h1{
    color: rgb(42, 137, 137);
    text-align: center;
    margin-top: 40px;
}
b{
    color: rgb(34, 118, 118);
}
.card{
    margin-top: 40px;
}
.message{
    margin-left: 100px;
    margin-top: 140px;
    position: absolute;
    right: 10px;
}
</style>