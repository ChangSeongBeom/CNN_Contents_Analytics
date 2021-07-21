<template>
   

   <div>
       <div class="menu">
       <a>욜로로그 분석</a>
       <a>자막(OCR)</a>
       <a>STT</a>
   </div>

<!--a href="javascript:;" @click="fnView(`${user.id}`)">-->

     <div id="divid" v-for="user in users" @click="detailview(user.ID)">{{user.contents}} {{user.ID}} </br>
     <img width="500px":src="user.img_url"></div>
     

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
       axios.get('http://localhost:3000/view')
       .then(function(response){
           console.log(response)
           vm.users=response.data
       })
       .catch(function(){
            
       })
   },
   methods:{
   detailview(id){
       console.log(id);
       this.$router.push({
           name: 'Detailview'
           ,params:{
               contentid:id
            }
       })
   }
   }
//    },
//    methods:{
//      fnView(id) {
// 			this.body.id = id;
//             alert(id);
// 			this.$router.push({path:'./view',query:this.body}); //추가한 상세페이지 라우터
// 	}
// }
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