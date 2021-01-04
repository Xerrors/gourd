import { defineConfig } from 'vite'
const {resolve} = require('path')

import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  alias: {
    // 键必须以斜线开始和结束
    '/@/': resolve(__dirname, './src')
    // '/@components/': path.resolve(__dirname, './src/components')
  },
})

