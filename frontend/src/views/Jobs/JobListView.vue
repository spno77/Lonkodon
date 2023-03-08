<template>

<h1 class="mt-5"> Jobs </h1>

<v-col class="ml-16 mt-2">
    <router-link :to="{name: 'JobPostView'}">
        <v-btn color="indigo-darken-2"  class="ml-16"> 
            Post Job
        </v-btn>
    </router-link>
</v-col>
    
<v-container class="mt-n10" >
    <v-row justify="center">
        <v-col cols="8">
            <v-container class="max-width">
                <v-pagination
                    v-model="pageNo"
                    class="my-4"
                    :length="numPages"
                ></v-pagination>
            </v-container>
        </v-col>
    </v-row>
</v-container>
  
<v-container>
    <v-row>        
        <v-col mt-2 cols="6" v-for="(job, index) in pagedJobs" :key="index">
            <v-card 
                color="cyan"
                height="100%"
                class="myCard"
            >
  
                <v-card-title class="text-h4 text-md-center" >
                    {{ job.title }}
                </v-card-title>
  
                <v-col>
                    <div class="jobInfo"> 
                        <div> Experience: <b> 
                            <span style="margin-left: 20px">{{ job.experience }}
                            </span> </b> years 
                        </div> 
                            
                        <div> Level: <b> 
                            <span style="margin-left: 65px">{{ job.level }}
                            </span> </b>  
                        </div>

                        <div> Description: <b> 
                            <span style="margin-left: 15px">{{ job.description }}
                            </span> </b>  
                        </div> 
                                
                        <div> Job Poster: <b> 
                            <span style="margin-left: 18px">{{ job.poster.username }}
                            </span> </b>  
                        </div>
                            
                        <div> Date: <b> 
                            <span style="margin-left: 65px">{{ job.date_created }}
                            </span> </b>  
                        </div> 
                    </div>
                </v-col>
                    
                <v-btn @click="apply(job.id,index)" color="success" :style="{left: '50%', bottom: '5%', transform:'translateX(-50%)'}">
                        apply
                </v-btn>
            
            </v-card>
        </v-col>
    </v-row>
</v-container>
    
</template>
  
<script>
import axios from 'axios';
import { mapState, mapStores } from 'pinia';
import { useAppStore } from '@/store/app';
export default{
    
data() {
    return{ 
        jobs:       [],
        pageSize:    4,
        pageNo:      1,
    }
},

methods:{
    apply(jobId,index){
        axios.
            post('http://127.0.0.1:8000/api/v1/applications/',{
                source: this.user.id,
                job: jobId, 
            },
                { headers: {'Authorization': 'Bearer ' + this.user.access_token }}  
            )
            this.jobs.splice(index,1)
    }
},

computed:{
    ...mapStores(useAppStore),
    ...mapState(useAppStore,['user']),
    numPages() {
        return Math.ceil(this.jobs.length / this.pageSize);
    },
      
    pagedJobs() {      
        const startIndex = (this.pageNo - 1) * this.pageSize;
        const data = [...this.jobs];
        return data.splice(startIndex, this.pageSize);
    }
},

mounted(){
    axios
        .get('http://127.0.0.1:8000/api/v1/jobs/',
            { headers: {'Authorization': 'Bearer ' + this.user.access_token }}  
        )
        .then(response => (this.jobs = response.data))
},
}

</script>
  
<style scoped>

h1{
    color: rgb(42, 137, 137);
    text-align: center;
}
.myImage{
    margin-left: -35%;
}
.jobInfo{
      margin-left: 30px;
      font-size: 18px; 
}
.myCard {
    border-top: 5px solid rgb(2, 45, 113) !important;
    border-radius: 25px 25px 0 0;
}
.findButton{
    margin-left: 1200px;
}

</style>