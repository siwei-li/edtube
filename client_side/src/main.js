import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

//=============Auth0======================
// Import the Auth0 configuration
import { domain, clientId, audience } from "../auth_config.json";

// Import the plugin here
import { Auth0Plugin } from "./auth";

// Install the authentication plugin here
Vue.use(Auth0Plugin, {
  domain,
  clientId,
  audience,
  onRedirectCallback: appState => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    );
  }
});

//===============ElementUI===========
// import { Button, Select } from 'element-ui';
// Vue.component(Button.name, Button);
// Vue.component(Select.name, Select);

import ElementUI from 'element-ui'
// import 'element-ui/lib/theme-chalk/index.css';
import '@/assets/et_theme/theme/index.css'

// import lang from 'element-ui/lib/locale/lang/en'
import locale from 'element-ui/lib/locale/lang/en'
// import './plugins/element.js'
// locale.use(lang)


Vue.use(ElementUI, { locale ,size: 'large', zIndex: 3000 })


//===================================
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
