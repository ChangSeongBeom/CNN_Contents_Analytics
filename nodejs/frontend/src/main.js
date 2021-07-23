// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import Donut from 'vue-css-donut-chart';
import 'vue-css-donut-chart/dist/vcdonut.css';

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import BootstrapVue from 'bootstrap-vue';
import "chart.js";
import "hchs-vue-charts";

Vue.use(Donut);
Vue.use(window.VueCharts);
Vue.use(BootstrapVue)
Vue.prototype.$http  = axios
Vue.config.productionTip=false
/* eslint-disable no-new */
new Vue({
  
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
