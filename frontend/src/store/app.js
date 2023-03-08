// Utilities
import { defineStore } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import  axios  from 'axios'

export const useAppStore = defineStore('app', {
  
  state: () => ({
    user: {},
    isLoggedIn: false,
    token: '',
  }),

  getters: {
    loggedUser:(state) => state.user,
   
  },

  actions: {
    loginUser (user) {
       axios.post('http://127.0.0.1:8000/api/v1/dj-rest-auth/login/',user)	
        	 .then((response) => {
              this.user = response.data
            })
            this.isLoggedIn = true
            this.router.push('/')
    },

    logoutUser(){
      axios.post('http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/')
      
      this.isLoggedIn = false
      this.user = null
    },
    
  },

})
