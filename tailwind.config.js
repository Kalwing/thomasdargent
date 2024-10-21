const plugin = require('tailwindcss/plugin')
module.exports = {
  content: ['./public/*.html', "./public/*/*.html", "./flask_templates/*/*.html"],
  theme: {
    colors: {
      'gray': {
        '100': '#F7F6F3',
        '200': '#DFDBCBff',
        '700': '#5E6C6A',
        '900': '#1D343Aff',
      },
      'pacific-blue': {
          '100': '#e1f6f9',
          '300': '#73d8ed',
          '500': '#17a1c5',
          '600': '#1680a4',
          '900': '#1c475d',
      },
      'pink': {
        '400': '#db8bc3',
        '600': '#b9498e',
        '800': '#843061',
        '950': '#42152f',
      },
      'transparent': '#00000000'
    },
    extend: {
      animation: {
        'spin-slow': 'spin 10s linear infinite',
      },
      keyframes: {
        spin: {
          from: { transform: 'rotate(0deg)' },
          to: { transform: 'rotate(360deg)' },
        },
      },
      fontSize: {
        sm: '0.750rem',
        base: '1rem',
        xl: '1.333rem',
        '2xl': '1.777rem',
        '3xl': '2.369rem',
        '4xl': '3.158rem',
        '5xl': '4.210rem',
      },
      fontFamily: {
        heading: 'Le Murmure, serif',
        body: 'Josefin Sans',
      },
      textShadow: {
        white: '3px 0 0 #FFF, -3px 0 0 #FFF, 0 3px 0 #FFF,  0 -3px 0 #FFF, 1.5px 1.5px 0 #FFF, -1.5px 1.5px 0 #FFF, -1.5px -1.5px 0 #FFF, -1.5px 1.5px 0 #FFF',
        DEFAULT: '3px 0 0  var(--tw-shadow-color), -3px 0 0  var(--tw-shadow-color), 0 3px 0  var(--tw-shadow-color),  0 -3px 0  var(--tw-shadow-color), 1.5px 1.5px 0  var(--tw-shadow-color), -1.5px 1.5px 0  var(--tw-shadow-color), -1.5px -1.5px 0  var(--tw-shadow-color), -1.5px 1.5px 0  var(--tw-shadow-color)',
      },
    }
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    plugin(function ({ matchUtilities, theme }) {
      matchUtilities(
        {
          'text-shadow': (value) => ({
            textShadow: value,
          }),
        },
        { values: theme('textShadow') }
      )
    }),

  ],
  variants: [],

}