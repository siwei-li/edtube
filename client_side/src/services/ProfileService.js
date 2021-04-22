import Api from '@/services/Api'

export default {
    updateProfile(data) {
        return Api().put(`/user_profile`,data);
    },
    updateNickname(data,config={}) {
        return Api().patch(`/user_nickname`, data,config);
    },
    profilePic(file) {
      return Api().post(`/profile_pic`,file);
    },
}

// export const test = (params = {}) => apiClient.get('/private', params)
