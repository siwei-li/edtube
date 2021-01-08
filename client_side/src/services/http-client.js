import axios from 'axios'

axios.defaults.baseURL = '/api'
axios.defaults.headers['Content-Type'] = 'Access-Control-Allow-Origin'

const getToken = async function () {
    const token = await this.$auth.getTokenSilently();
    return token;
}

axios.interceptors.request.use(
    (config) => {
        if (this.$auth.isAuthenticated === true) {
            getToken().then(token => {
                    config.headers.Authorization = `Bearer ${token}`;
                }
            ).catch(err => {
                console.log(err);
            });
        }
        // console.log("send request", config)
        return config
    },
    (error) => {
        console.log("Failed to send request")
        return Promise.reject(error)
    })

// axios.interceptors.response.use(
//     response => {
//         //If the returned status code is 200, the interface request is successful and the data can be obtained normally.
//         //Otherwise, an error will be thrown.
//         if (response.status === 200) {
//             if (response.data.code === 511) {
//                 //Unauthorized access to authorized interface
//             } else if (response.data.code === 510) {
//                 //No login to jump to login page
//             } else {
//                 return Promise.resolve(response)
//             }
//         } else {
//             return Promise.reject(response)
//         }
//     }, error => {
//         // if (error.response.status) {
//         if (error.response) {
//             //Failure to process request
//             //Corresponding processing for different return codes
//             return Promise.reject(error.response)
//         }
//     }
// );

//Get request
export function httpGet({
                            url,
                            params = {}
                        }) {
    return new Promise((resolve, reject) => {
        axios.get(url, {
            params
        }).then((res) => {
            // resolve(res)
            resolve(res.data)
        }).catch(err => {
            reject(err)
        })
    })
}

export function httpPost({
                             url,
                             data = {},
                             params = {}
                         }) {
    return new Promise((resolve, reject) => {
        axios({
            url,
            method: 'post',
            transformRequest: [function (data) {
                let ret = ''
                for (let it in data) {
                    ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
                }
                return ret
            }],
            //Data sent
            data,
            // url parameter
            params

        }).then(res => {
            resolve(res.data)
        })
    })
}

export function patch(url, data = {}) {
    return new Promise((resolve, reject) => {
        axios.patch(url, data)
            .then(response => {
                resolve(response);
            }, err => {
                reject(err);
            })
    })
}

export function put(url, data = {}) {
    return new Promise((resolve, reject) => {
        axios.put(url, data)
            .then(response => {
                resolve(response);
            }, err => {
                reject(err);
            })
    })
}



