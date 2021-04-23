import Api from '@/services/Api'

export default {
    updateProfile(data) {
        return Api().put(`/user_profile`,data);
    },
    updateNickname(data) {
        return Api().patch(`/user_nickname`, data);
    },
    profilePic(data) {
        console.log(data);
      return Api().patch(`/profile_pic`,data);
    },
}

// export const test = (params = {}) => apiClient.get('/private', params)
