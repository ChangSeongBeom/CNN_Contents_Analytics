<template>

<!--a href="javascript:;" @click="fnView(`${user.id}`)">-->
    <div>
        <div>sadfsfa </div>
      <div id="baa" v-for="list in lists" >사물명{{list.object}}탐지개수{{list.cnt}}정확도{{list.avgpercent}} </br>
  
    </div>   
</template>

<script>
import axios from 'axios';

export default {
    name:'Detailview',
    computed: {
        param() {
            
            return this.$route.params.contentid;
        }
    },
    
    data(){
        return{

            lists : []
        }
    },
    created(){
            var vm=this;
            axios.get("http://localhost:3000/detailview/"+this.$route.params.contentid)
             .then(function(response){
           console.log(response)
           vm.lists=response.data
       })
             .catch(function(){
                alert(error)
            })
        }
    }
//     mounted(){

//        var vm=this;
       
//        axios.get('http://localhost:3000/detailview/'+this.data.id)
       
//        .then(function(response){
//            console.log(response)
//            vm.users=response.data
//        })
//        .catch(function(){
            
//        })
//    }

</script>
