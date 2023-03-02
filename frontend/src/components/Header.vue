<template>
  <v-toolbar density="compact" color="cyan">      
    
    <v-toolbar-title style="cursor: pointer" @click="$router.push('/')">
       Lonkodon 
    </v-toolbar-title>

    <v-btn icon :to="{name: 'Messages'}">
      <v-icon >mdi-message </v-icon>
    </v-btn>
    
    <v-btn to="/connections">  Network   </v-btn>
    
    <v-btn to="/articles">  Articles   </v-btn>

    <v-btn icon>
      <v-icon> mdi-dots-vertical </v-icon>

    <v-menu activator="parent">
      <v-list>
      
        <v-list-item v-if="!isLoggedIn" :to="{name: 'Register'}">
          <v-list-item-title>
            <v-btn color="cyan" block> Register </v-btn>
          </v-list-item-title>
        </v-list-item>

        <v-list-item v-if="isLoggedIn" :to="{name: 'Profile', params:{id: loggedUser.user.id } }">
          <v-list-item-title>
            <v-btn color="cyan" block> Profile </v-btn>
          </v-list-item-title>
        </v-list-item>

        <v-list-item v-if="!isLoggedIn" :to="{name: 'Login'}">
          <v-list-item-title>
            <v-btn color="cyan" block> Log in </v-btn>
          </v-list-item-title>
        </v-list-item>
        
        <v-list-item v-if="isLoggedIn">
          <v-list-item-title>
            <v-btn @click.prevent="logoutUser" color="cyan" block> Log out </v-btn>
          </v-list-item-title>
        </v-list-item>
      </v-list>
      
    </v-menu>
 </v-btn>
</v-toolbar>
</template>

<script>
import { mapActions, mapState, mapStores } from 'pinia';
import { useAppStore } from '@/store/app';

export default{
  name: 'Header',

  computed:{
      ...mapStores(useAppStore),
      ...mapState(useAppStore,['user','loggedUser','isLoggedIn']),
    },
    methods:{
      ...mapActions(useAppStore,['logoutUser'])
    }




}
</script>
