import axios from 'axios'

const request = axios.create({
  // 配置选项
  // baseURL,
  timeout: 5000
})

// 请求拦截器

// 响应拦截器

export default request