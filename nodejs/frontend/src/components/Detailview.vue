<template>

<!--a href="javascript:;" @click="fnView(`${user.id}`)">-->

        <div>
        
        <iframe width="40%" height="500px" :src=lists[0].frame_url title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        <!--<iframe width="560" height="315" src="https://www.youtube.com/embed/-1fcHvqacQs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>-->
        <div><b-table striped hover :items="lists" :fields="fields"></b-table></div>
        </div>
     <!-- <div id="baa" v-for="list in lists" >사물명{{list.object}}탐지개수{{list.cnt}}정확도{{list.avgpercent}} </br>-->
    
   
</template>


<script>
import axios from 'axios';

// lists=data.cnt.sort((a,b)=>{return a.avgpercent-b.avgpercent})
export default {
    name:'Detailview',
    computed: {
        param() {
             
            return this.$route.params.contentid;
        }
    },
    data(){
        return{
            fields: [
                {
                    key: 'object',
                    label: '탐지사물'
                },
                {
                    key: 'cnt',
                    label: '탐지횟수'
                },
                {
                    key: 'avgpercent',
                    label: '평균정확도'
                }
            ],
            lists: []
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
