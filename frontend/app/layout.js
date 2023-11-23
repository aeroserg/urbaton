import { Inter } from 'next/font/google'
import './globals.css'
import './style.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Лучшая digital школа в России',
  description: 'Приходите учиться к нам учиться!',
}

export default function RootLayout({ children }) {
  return (
    <html lang="ru">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
