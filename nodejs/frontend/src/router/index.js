import Vue from 'vue'
import Router from 'vue-router'
import Read from '@/components/Read'
// import View from '@/components/View'
import Detailview from '@/components/Detailview'
import STT from '@/components/STT'
import OCR from '@/components/OCR'


Vue.use(Router)

export default new Router({
  routes: [{
      path: '/',
      name: 'Read',
      component: Read
    },
    {
      path: '/STT',
      name: 'STT',
      component: STT
    },
    {
      path: '/OCR',
      name: 'OCR',
      component: OCR
    },
    // {
    //   path:'/view'  //상세페이지 추가
		// 	,name:'View' 
		// 	,component:View
    // },
    {
      path:'/detailview/:contentid'  //상세페이지 추가
			,name:'Detailview'
			,component:Detailview
    }
    // {
    //   path: '/:id',
    //   name: 'detailmovie',
    //   component: DetailMoviePage
    // }
  ]
})


