import { createStore } from "vuex";

export default createStore({
  state() {
    return {
      cur_view: 0,
    };
  },
  mutations: {
    increment(state) {
      state.count++;
    },
  },
  actions: {
    increment(context) {
      context.commit("increment");
    },
  },
});