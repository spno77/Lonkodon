<template>

    <h1 class="text-md-center mt-10"> Login </h1>
    
    <v-sheet width="400" class="mx-auto">
        <v-form class="mt-10">
            <v-text-field
                v-model="user.username"
                label="Username"
            ></v-text-field>
  
            <v-text-field
                type="password"
                v-model="user.password"
                label="Password"
            ></v-text-field>
        </v-form>
    </v-sheet>

    <v-btn @click.prevent ="loginRedirect(this.user);" color="cyan"   rounded="lg"
        :style="{left: '50%', transform:'translateX(-50%)'}"> 
                    Login
    </v-btn>

</template>
  
<script>
import { mapActions,mapStores } from 'pinia';
import { useAppStore } from '@/store/app';

export default {
data() {
    return {
        user:{
            username: '',
            password: '',
            is_staff: null
        },
    }
},

computed:{
    ...mapStores(useAppStore),
},

methods:{
    ...mapActions(useAppStore,['loginUser']),

    loginRedirect(userLogin){
        this.loginUser(userLogin)
        if(this.user.username !== ''){
            this.$router.push('/')
        }
    }
}
}

</script>

<style scoped>

h1{
    color: rgb(42, 137, 137); 
}

</style>