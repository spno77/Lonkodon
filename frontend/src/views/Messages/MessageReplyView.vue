<template>
        <v-text-field
            class="myInput" 
            color="cyan"
            v-model="user1"
            label="Reply"
        ></v-text-field>

        <v-btn class="myButton" 
               color="cyan" rounded="lg"
               :style="{left: '50%', transform:'translateX(-50%)'}"
        > 
            Reply
       </v-btn>

</template>

<script>
export default{
    data(){
        return{
            user1: ""
        }

    }
}

</script>

<style scoped>

.myInput{
    height: 660px;
    width: 400px;
    margin-top: 30px;
}

.myButton{
    margin-top: -500px;
}

h1{
    color: rgb(42, 137, 137); 
}

</style>