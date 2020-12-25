import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    menuCollapsed: true,
  },
  mutations: {
    toggleMenu(state) {
      state.menuCollapsed = !state.menuCollapsed;
    }
  },
  actions: {
  },
  modules: {
  }
})
