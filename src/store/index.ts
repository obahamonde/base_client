import { defineStore, acceptHMRUpdate } from 'pinia'

export const useStore = defineStore("store",()=>{
    const state  = reactive({})

    const dispatch = (newState: any)=>{
       Object.assign(state, {...state, ...newState})
    }

    return {
        state,
        dispatch,
    }
})

if(import.meta.hot)
    acceptHMRUpdate(useStore, import.meta.hot)