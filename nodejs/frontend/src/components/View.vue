<template>
<canvas class="statistics-charts-line" ref="lineChart" width="500" height="400"></canvas>
</template>


<script>
import Chart from "chart.js";
export default{
	data() {
    return {
      Chart,
    };
  }, 
  async created() {
    // 필요 시 데이터 가져오는 로직
    // 차트생성에 사용할 옵션과 데이터가 결정될 것이다.
  },
  async mounted() {
    // 마운트 된 두 ref에 접근할 수 있으므로 마운트 뒤 차트를 그린다.
    await this.drawChart();
  },
  methods: {
    drawChart() {
      const chartCtx = this.$refs.lineChart.getContext("2d");
      console.log(chartCtx, "chartCtx?");
      // context와 Chart.js객체, 데이터가 결정됐으니  그리기만 하면된다.
    },
  }
	// 	data(){
		
    //     return{
			
    //         lists : []
    //     }
    // },
	// created(){
    //         var vm=this;
    //         axios.get("http://localhost:3000/detailview/"+"1")
    //          .then(function(response){
    //        console.log(response)
    //        vm.lists=response.data

	// 	   console.log(response.data.length);
	// 	console.log(typeof(response.data[0].object));
		 
	// 	arr2=[];
	// 	   for(var i=0;i<response.data.length;i++){
	// 		   console.log("바보");
	// 		//    arr2.push(response.data[i].object);
	// 		//    console.log(arr2);
	// 	   }
	// 	   console.log(arr2);
    //    })
    //          .catch(function(){
    //             alert(error)
    //         })
    //     }
	
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