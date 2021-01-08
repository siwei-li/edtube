import { httpGet, httpPost, patch, put } from './http-client'

export const test = (params = {}) => httpGet({ url: '/private', params })




// import { getbook } from '@/services/api-caller'
// getbook({ id: 200 }).then(res => {
//     console.log(res)
// })