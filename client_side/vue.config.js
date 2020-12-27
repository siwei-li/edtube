module.exports = {
    devServer: {
      proxy: {
        "^/api": {
          target: "http://localhost:8000",
            // changeOrigin: true
        },
          "^/login/auth0": {
              target: "http://localhost:8000",
              // changeOrigin: true
          }
      }
    }
  };