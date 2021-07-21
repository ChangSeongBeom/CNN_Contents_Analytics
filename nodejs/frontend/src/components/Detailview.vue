<!--<template>
  <vc-donut
    background="white" foreground="grey"
    :size="200" unit="px" :thickness="30"
    has-legend legend-placement="top"
    :sections="sections" :total="100"
    :start-angle="0" :auto-adjust-text-size="true"
    @section-click="handleSectionClick">
    <h1>75%</h1>
  </vc-donut>
</template>
<script>
  export default {
    data() {
      return {
        sections: [
          { label: 'Red section', value: 25, color: 'red' },
          { label: 'Green section', value: 25, color: 'green' },
          { label: 'Blue section', value: 25, color: 'blue' }
        ]
      };
    },
    methods: {
      handleSectionClick(section, event) {
        console.log(`${section.label} clicked.`);
      }
    }
  };
</script>-->

<template>
    <div>

        {{ $route.params.contentid }}
        <div id="ddd" v-for="user in users" >{{user.avgpercent}} {{user.cnt}} {{user.contents}} {{user.object}}
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
    // data(){
    //     return{

    //         // users: [],in
    //     }
    // },
    created(){
        console.log("route"+this.$route.params.contentid);
        console.log("router"+this.$router);
    },
    

    mounted(){
 
            axios.get("http://localhost:3000/detailview/"+this.$route.params.contentid)
            .then(response=>{
                const data=response
                console.log(data)
            })
            .catch(error=>{
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
