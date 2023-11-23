import { Inter } from 'next/font/google'
import '../globals.css'
import '../style.css'


const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Вход в личный кабинет',
  description: 'Войдите в личный кабинет лучшей школы России',
}

export default function RootLayout({ children }) {
  return (
    <html lang="ru">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
