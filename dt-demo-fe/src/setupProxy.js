const { createProxyMiddleware } = require('http-proxy-middleware');

const BASE_API_URL = 'http://127.0.0.1:5001/api'
const endpoints = ['/filter', '/converter', '/statistics'];

module.exports = function(app) {
    endpoints.forEach(endpoint => {
        app.use(
            endpoint,
            createProxyMiddleware({
                target: BASE_API_URL,
                changeOrigin: true,
            })
        );
    });
};