<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div v-if="!$auth.loading">
    <button @click="testApi">Call API</button>
    </div>
    <p>{{ apiMessage }}</p>
  </div> 
</template>

<script>
// import axios from "axios";
import {test} from "@/services/ProfileService";

export default {
  name: "About",
  data() {
    return {
      apiMessage: ""
    };
  },
  methods: {
    async testApi() {
      test().then(res=>console.log(res));
    },
    async callApi() {
      // Get the access token from the auth wrapper
      const token = await this.$auth.getTokenSilently();
      console.log(token)

      const { data } = await axios.get('/private', {  
        headers: {
          Authorization: `Bearer ${token}`
        }
      });
      this.apiMessage = data;
    }
  }
// promise
//   document.getElementById('call-api').addEventListener('click', () => {
//   auth0
//     .getTokenSilently()
//     .then(accessToken =>
//       fetch('https://localhost:8000/api/private', {
//         method: 'GET',
//         headers: {
//           Authorization: `Bearer ${accessToken}`
//         }
//       })
//     )
//     .then(result => result.json())
//     .then(data => {
//       console.log(data);
//     });
// })

}
</script>