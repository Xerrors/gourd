import { message } from 'ant-design-vue'
import axios from 'axios'
import Cookies from 'js-cookie'

axios.defaults.timeout = 50000 // 请求超时时间

// 请求拦截器
axios.interceptors.request.use(
  config => {
    return config
  },
  error => {
    // Do something with request error
    Promise.reject(error)
  }
)

// 响应拦截器
axios.interceptors.response.use(
  response => {
    return response
  },
  error => {
    if (error.code === 1001) {
      Cookies.remove('logged');
      return Promise.reject(new Error('error'))
    }
    // 当请求连接不通的时候
    // cosole.log('error' + error) // for debug
    return Promise.reject(error)
  }
)


export default axios