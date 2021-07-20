<template>
   

   <div>
       <div class="menu">
       <a>욜로로그 분석</a>
       <a>자막(OCR)</a>
       <a>STT</a>
   </div>



     <div id="divid" v-for="user in users">{{user.contents}}<img width="500px":src="user.img_url"></div>

   </div>
</template>

<script>
import axios from 'axios';
export default{
    
    name:'Read',
    data(){
        return{
        
            users: []
        }
    },
   created(){
       var vm=this;
       axios.get('http://localhost:3000/main')
       .then(function(response){
           console.log(response)
           vm.users=response.data
       })
       .catch(function(){
            
       })
   }
}
</script>
<style scoped>
.menu{
    background: darkslateblue;
    padding: 15px;
    border-radius: 5px;
}
.menu a{
    color: white;
    padding: 10px;
}
#divid{
    font-size:30px;
}

</style>