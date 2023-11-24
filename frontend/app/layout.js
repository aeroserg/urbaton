import './globals.css'
import './style.css'
import { Roboto } from 'next/font/google'
import { Rubik } from 'next/font/google'

const roboto = Roboto({ weight: ['100', '300', '400', '500', '700', '900'],
    style: ['normal', 'italic'],
    subsets: ['latin'],
    display: 'swap',
    variable: '--font-roboto'
})
const rubik = Rubik({
    weight: ['300', '400', '500', '700', '900'],
    style: ['normal', 'italic'],
    subsets: ['latin'],
    display: 'swap',
    variable: '--font-rubik'
})

export const metadata = {
  title: 'Лучшая digital школа в России',
  description: 'Приходите учиться к нам учиться!',
}

export default function RootLayout({ children }) {
  return (
    <html lang="ru">
      <body className={`${roboto.variable} ${rubik.variable}`}>{children}</body>
    </html>
  )
}
