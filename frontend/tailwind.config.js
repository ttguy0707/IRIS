/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        // 现代无衬线字体栈：优先系统默认，保证清晰
        sans: [
          'Inter', 
          'system-ui', 
          '-apple-system', 
          'BlinkMacSystemFont', 
          '"Segoe UI"', 
          'Roboto', 
          '"Helvetica Neue"', 
          'Arial', 
          '"Noto Sans"', 
          '"PingFang SC"',    // Mac 中文
          '"Hiragino Sans GB"', // Mac 中文
          '"Microsoft YaHei"',  // Win 中文
          '"WenQuanYi Micro Hei"', 
          'sans-serif'
        ],
        // 标题字体 (Orbitron 用于 Logo)
        display: ['Orbitron', 'sans-serif'],
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: 'none',
            color: '#374151', // Gray-700，比纯黑柔和
            // 基础行高设置
            p: {
              marginTop: '1.2em',
              marginBottom: '1.2em',
              lineHeight: '1.75', 
              letterSpacing: '0.01em', // 稍微加一点字间距提升呼吸感
            },
            // 标题设置
            h1: {
              color: '#111827', // Gray-900
              fontWeight: '800',
              marginTop: '0',
              marginBottom: '0.8em',
              lineHeight: '1.2',
            },
            h2: {
              color: '#1f2937', // Gray-800
              fontWeight: '700',
              marginTop: '2em',
              marginBottom: '1em',
              lineHeight: '1.3',
            },
            h3: {
              color: '#1f2937',
              fontWeight: '600',
              marginTop: '1.5em',
              marginBottom: '0.6em',
            },
            // 列表
            li: {
              marginTop: '0.5em',
              marginBottom: '0.5em',
            },
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}