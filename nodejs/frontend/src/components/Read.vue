<template>
   

   <div>
       
  
<!--a href="javascript:;" @click="fnView(`${user.id}`)">-->
    <div class="circular" v-bind:style="{ backgroundImage: 'http://www.hmgprime.com/cmm/fms/3913/2/getImage.do' }"></div>
     <div id="onerow" v-for="user in users" @click="detailview(user.ID)">{{user.contents}} {{user.ID}} </br>
   
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
<style>
body{
/*     
background-image: url('https://mdbcdn.b-cdn.net/img/new/slides/041.jpg') !important;
background-size: 150px;
  width: 300px;
  height: 300px; */
}
.menu{
    background: darkslateblue;
    padding: 15px;
    border-radius: 5px;
}
.menu a{
    color: white !important;
    padding: 10px;
}
#onerow{
    font-size:30px;
    color: black;
     outline: 5px solid blue;
}

</style>
