// Utilities
import { defineStore } from 'pinia'
import  axios  from 'axios'

export const useAppStore = defineStore('app', {
  state: () => ({
    user: {},
    isLoggedIn: false,
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
            console.log(this.isLoggedIn)
    },

    logoutUser(){
      axios.post('http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/')
      this.isLoggedIn = false
    },
    
  },

})
