import { defineConfig } from 'vite'
import { resolve } from 'path'

import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  alias: {
    // 键必须以斜线开始和结束
    '/@/': resolve(__dirname, './src')
    // '/@components/': path.resolve(__dirname, './src/components')
  },
  optimizeDeps: {
    include: ["axios"]
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://116.62.110.131:5000/',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  },
})
