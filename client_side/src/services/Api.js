import axios from 'axios'
import {getInstance} from '@/auth/index.js'


export default () => {
    const axiosInstance = axios.create({
        // baseURL: "https://edtube-server.herokuapp.com/api",
        baseURL: process.env.VUE_APP_API_ENDPOINT,
        Timeout: 1000 * 5,
        headers :{
            common:{
                'Content-Type': 'application/json; charset=UTF-8',
                 'X-Requested-With': 'XMLHttpRequest',
                'Accept': 'application/json',
                'WithCredentials': true,
                // 'Access-Control-Allow-Origin': '*'
            }
        },
    });

    // axiosInstance.defaults.headers['Access-Control-Allow-Headers'] = 'Authorization'
    // axiosInstance.defaults.headers['Access-Control-Allow-Methods'] = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']

    axiosInstance.interceptors.request.use(async config => {
        const auth0 = getInstance();
        if (auth0.isAuthenticated){
        const token = await auth0.getTokenSilently();
        config.headers = {'Authorization':`Bearer ${token}`}}
        return config;
    }, error => {
        console.log(error)
        return Promise.reject(error)
    })

    axiosInstance.interceptors.response.use(
        response => {
            //If the returned status code is 200, the interface request is successful and the data can be obtained normally.
            //Otherwise, an error will be thrown.
            if (response.status === 200) {
                // if (response.data.code === 511) {
                //     //Unauthorized access to authorized interface
                // } else if (response.data.code === 510) {
                //     //No login to jump to login page
                // } else {
                return Promise.resolve(response)
                // }
            } else {
                return Promise.reject(response)
            }
        }, error => {
            // if (error.response.status === 401) {}
            return Promise.reject(error)
        }
    )

    return axiosInstance;
}
;


// //Get request
// export function httpGet({
//                             url,
//                             params = {}
//                         }) {
//     return new Promise((resolve, reject) => {
//         axios.get(url, {
//             params
//         }).then((res) => {
//             resolve(res)
//             // resolve(res.data)
//         }).catch(err => {
//             reject(err)
//         })
//     })
// }

// export function httpPost({
//                              url,
//                              data = {},
//                              params = {}
//                          }) {
//     return new Promise((resolve, reject) => {
//         axios({
//             url,
//             method: 'post',
//             transformRequest: [function (data) {
//                 let ret = ''
//                 for (let it in data) {
//                     ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
//                 }
//                 return ret
//             }],
//             //Data sent
//             data,
//             // url parameter
//             params

//         }).then(res => {
//             resolve(res.data)
//         })
//     })
// }

// export function patch(url, data = {}) {
//     return new Promise((resolve, reject) => {
//         axios.patch(url, data)
//             .then(response => {
//                 resolve(response);
//             }, err => {
//                 reject(err);
//             })
//     })
// }

// export function put(url, data = {}) {
//     return new Promise((resolve, reject) => {
//         axios.put(url, data)
//             .then(response => {
//                 resolve(response);
//             }, err => {
//                 reject(err);
//             })
//     })
// }



