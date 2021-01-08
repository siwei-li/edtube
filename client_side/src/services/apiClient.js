import myApp from "../main";
import axios from "axios";

export const apiClient = axios.create({
    // baseURL: process.env.VUE_APP_API_BASE,
    baseURL: '/api',
    headers: {
        Accept: 'application/json',
        // 'Content-Type': 'application/json',
        'Content-Type': 'Access-Control-Allow-Origin'
    }
});

apiClient.interceptors.request.use(async (config) => {
    const token = await myApp.$auth.getTokenSilently();
    config.headers['Authorization'] = `Bearer ${token}`;
    return config;
}, (error) => {
    return Promise.reject(error);
});