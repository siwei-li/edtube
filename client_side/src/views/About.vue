<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div v-if="!$auth.loading">
    <button @click="callApi">Call API</button>
    </div>
    <p>{{ apiMessage }}</p>
  </div> 
</template>

<script>
import axios from "axios";

export default {
  name: "About",
  data() {
    return {
      apiMessage: ""
    };
  },
  methods: {
    async callApi() {
      // Get the access token from the auth wrapper
      const token = await this.$auth.getTokenSilently();
      console.log(token)

      // Use Axios to make a call to the API
      const { data } = await axios.get('/api/private', {  
        headers: {
          Authorization: `Bearer ${token}`    // send the access token through the 'Authorization' header
        }
      });

      this.apiMessage = data;
      // console.log("API called and fetched.");

    // catch (e) {
    //     console.log(e);
    //     this.apiMessage = `Error: the server responded with '${e.response.status}: ${e.response.statusText}'`;
    //   }
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