<template>
   
       
      <table>
            <thead>
                <tr>
                    <th>아이디값</th>
                    <th>이름</th>
                    <th>썸네일</th>
                    <th>로그수집날짜</th>

                </tr>
            </thead>
            <tbody id="contacts">
                <tr v-for="user in users"  @click="detailview(user.ID)">
                    <td>{{user.ID}}</td>
                    <td>{{user.contents}}</td>
                    <td width=35%> <img width="100%":src="user.img_url"></td>
                    <td> {{user.LOGTIME}}</td>
                </tr>
            </tbody>
        </table>
<!--a href="javascript:;" @click="fnView(`${user.id}`)">-->
<!--     {{user.contents}}<div id="onerow" v-for="user in users" @click="detailview(user.ID)"> {{user.ID}} </br>
   
     <img width="500px":src="user.img_url"></div>-->
     

  

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
     outline: 3px solid black;
}
 table {
    width: 100%;
    border: 1px solid #444444;
    border-collapse: collapse;
  }
  tr th {
    
    background-color: #e6f1ff;
    border: 1px solid #444444;
  }
  tr td{
      font-size:22px;
      background-color: #d5e6f7;
          border: 1px solid #444444;
        

  }

</style>