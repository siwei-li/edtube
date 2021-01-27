import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // token:"",
    drawer: false,
  },
  mutations: {
    // storeToken(state, token) {
    //   state.token=token;
    // },
    toggleMenu(state) {
      state.drawer = !state.drawer;
    },
  },
  actions: {

  },
  modules: {
  }
})
