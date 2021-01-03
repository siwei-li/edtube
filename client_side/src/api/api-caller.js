import { httpGet, httpPost, patch, put } from './http-client'

export const getbook = (params = {}) => httpGet({ url: '/book', params })




// import { getbook } from '@/assets/callapi/api-caller'
// getbook({ id: 200 }).then(res => {
//     console.log(res)
// })