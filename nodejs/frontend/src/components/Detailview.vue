<template>
    <div>
        <div id="ddd" v-for="user in users" >{{user.avgpercent}} {{user.cnt}} {{user.contents}} {{user.object}}
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name:'Detailview',
    data(){
        return{
            users: [],
            id: this.$route.contentid
        }
    },
    
    computed: {
        param: function () {
            return this.$route.params;
        }
    },
    
    created(){

       
       var vm=this;
       axios.get('http://localhost:3000/detailview/'+"1")
       .then(function(response){
           console.log(response)
           vm.users=response.data
       })
       .catch(function(){
            
       })
   }
}
</script>
