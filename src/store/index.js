import { store } from "quasar/wrappers";
import { createStore } from "vuex";
import state from './mainstore/state'
import * as getters from './mainstore/getters'
import * as mutations from './mainstore/mutations'
import * as actions from './mainstore/actions'
import createPersistedState from "vuex-persistedstate";
// import example from './module-example'

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */


export default store(function (/* { ssrContext } */) {
  const Store = createStore({
    modules: {
      cyto: () => import('./cytostore/index.js')
    },
    getters,
    mutations,
    actions,
    state,
    plugins: [createPersistedState()],
  });

  return Store;
});