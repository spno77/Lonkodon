<template>

    <h1>My Messages</h1>

    <div v-show="showReply" class="message">
        <MessageReplyView :receiver="msgSender"> </MessageReplyView>
    </div>
    
    <v-container class="cont" >
      <v-row justify="center">
        <v-col cols="8">
          <v-container class="max-width">
            <v-pagination  @click="showReplyFalse()"
              v-model="pageNo"
              class="my-4"
              :length="numPages"
            ></v-pagination>
          </v-container>
        </v-col>
      </v-row>
    </v-container>

    <div v-for="(message, index) in pagedMessages" :key="index">

        <v-alert class="myAlert" color="cyan" 
            width="700"
            border="start"
        >
            <div class="sender">                 
                <v-avatar
                    class="avatar1" 
                    size=40 
                    :image="message.sender.image"> 
                </v-avatar> 

                <b>{{ message.sender.username }}:</b> 
                    {{ message.message }}
                
                <div class="date">
                   {{ message.send_date }}
                </div>

                <v-btn icon @click="deleteMsg(message.id,index)" class="trash">
                    <v-icon color="red">mdi-delete </v-icon>
                </v-btn>

                <div class="button1">
                    <v-btn @click.prevent="showReplyTrue(); setSender(message.sender.id);"
                        color="success" rounded="lg" 
                        :style="{left: '20%', transform:'translateX(-35%)'}"> 
                            reply 
                    </v-btn>
                </div>

            </div>  
        </v-alert>

    </div>

</template>

<script>
import axios from 'axios';
import { mapState, mapStores } from 'pinia';
import { useAppStore } from '@/store/app';
import MessageReplyView from '@/views/Messages/MessageReplyView'

export default{

components: {   
    MessageReplyView
},

data() {
    return{
        messages:   [],
        pageSize:    5,
        pageNo:      1,
        showReply:  false,
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

    deleteMsg(messageId,index){
        axios
            .delete('http://127.0.0.1:8000/api/v1/messages/'+ messageId + '/',
                {headers: {'Authorization': 'Bearer ' + this.user.access_token}} 
            )
        this.messages.splice(index,1)
    },

},

computed:{
    ...mapStores(useAppStore),
    ...mapState(useAppStore,['user']),

    numPages() {
        return Math.ceil(this.messages.length / this.pageSize);
    },

    pagedMessages() {      
        const startIndex = (this.pageNo - 1) * this.pageSize;
        const data = [...this.messages];

        return data.splice(startIndex, this.pageSize);
    }
},

mounted(){
    axios
        .get('http://127.0.0.1:8000/api/v1/messages/',
            { headers: {'Authorization': 'Bearer ' + this.user.access_token }}  
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
    margin-left: 380px;
}
.button1{
    float:right ;
    margin-right: 1px;
    margin-top: 6px;
}
.trash{
    float: right;
}
.sender{
    font-size: 19px;
}
.avatar1{
    margin-right: 8px;
}
.cont{
    margin-top: -20px;
}
.message{
    margin-left: 100px;
    margin-top: 125px;
    position: absolute;
    right: 25px;
}

.date{
    font-size: 12px;
    position: absolute;
    left: 44%;
}

</style>
