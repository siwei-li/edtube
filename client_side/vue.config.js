module.exports = {
    devServer: {
      proxy: {
        "^/api": {
          // target: "http://edtube.netlify.app:8000",
          // target: "http://192.168.52.20:8000"
          target: "http://127.0.0.1:8000"

        }
      }
    }
  };