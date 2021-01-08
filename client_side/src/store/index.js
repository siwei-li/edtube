import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // token:"",
    menuCollapsed: true,
  },
  mutations: {
    // storeToken(state, token) {
    //   state.token=token;
    // },
    toggleMenu(state) {
      state.menuCollapsed = !state.menuCollapsed;
    },
  },
  actions: {

  },
  modules: {
  }
})
