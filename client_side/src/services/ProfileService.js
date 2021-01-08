import {apiClient} from './apiClient.js'
import {httpGet} from "@/services/http-client";

export default {
    getProfile() {
        return apiClient.get('/profile')
    },
    // test() {
    //     return apiClient.get('/private')
    // }
}

export const test = (params = {}) => apiClient.get('/private', params)
