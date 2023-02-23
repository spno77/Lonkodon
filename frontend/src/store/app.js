// Utilities
import { defineStore } from 'pinia'
import { axios } from 'axios'

export const useAppStore = defineStore('app', {
  state: () => ({
    user: {}
  }),
  actions: {
    loginUser (user) {
      axios.post('http://127.0.0.1:8000/api/v1/rest-auth/login/',user)	
        	
    },
  }
})
