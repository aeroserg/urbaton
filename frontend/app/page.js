
import Header from './components/header'
import Image from 'next/image'
import Link from 'next/link'
export default function Home() {
  return (
    <>
    <Header headerText={"Главная страница"}/>
      <main className="page ">
      <section className='l_section_mainPage'>
        <div className="container-lg">
          <div className="main_page  row">
            <div className="mainSec_photo col-lg-6 col-12">
              <Image 
                alt='Счастливый ребенок, поттому что он ходит к нам на зантия'
                width={600}
                height={600}
                src='/img/boy.png'
                className='b_mainPhoto'
                style={{position: "static"}}
              />
            </div>
            <div className="mainSec_text col-lg-6 col-12"> 
              <h1 className='b_h1'>Художественное образование для детей в Екатеринбурге</h1>
              <p>Мы раскрываем таланты каждого ребенка</p>
              <Link className="main_btn width_constrained" href="/order">Подать заявку</Link>
            </div>
          </div>
        </div>
        </section>
        <section className="l-section">
          <h2>Мы подготовили разнообразные <strong>направления обучения</strong>, чтобы вы выбрали для себя самое подходящее</h2>
          <div className="photo_grid d-grid">

          </div>
        </section>
      </main>
    </>
  )
}
