<template>
	
</template>


<script>
import axios from 'axios';
export default{
	created(){
            var vm=this;
            axios.get("http://localhost:3000/detailview/"+"1")
             .then(function(response){
				 
           vm.lists=response.data

       })
             .catch(function(){
                alert(error)
            })
        },
		data(){
        return{

            lists : []
        }
    },
	//data(){
		// console.log(lists);
	
	// 	return{
			
	// 		labels:arr,
	// 	datasets: [
	// 		{
				
	// 			data:[20,30,40],
	// 			backgroundColor:["Red","Yellow","Purple"]
	// 		}
	// 	],
	// 	option :{
	// 		title:{
	// 			display:true,
	// 			position:"bottom",
	// 			text:"Fruits"
	// 		}
	// 	}	
	// }
	//}
}
</script>