'use client'
import Header from './components/header'
import Image from 'next/image'
import Link from 'next/link'
import Slider from "react-slick";
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";

export default function Home() {
  const settings = {
    className: "photo_grid",
    centerMode: true,
    infinite: true,
    slidesToShow: 3,
    speed: 500,
    
  };
  return (
    <>
    <Header />
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
          <div className="container-lg">
            <h2 className='mb-4 text-center'>Мы подготовили разнообразные <strong>направления обучения</strong>, чтобы вы выбрали для себя самое подходящее</h2>
              <div className="photo_grid d-grid">
                <div className="b_dirPhoto"><Image src="/img/arts.png" alt="" width={500} height={650} /></div>
                <div className="b_dirPhoto"><Image src="/img/drums.png" alt=""  width={500} height={650} /></div>
                <div className="b_dirPhoto"><Image src="/img/choir.png" alt=""  width={500} height={650} /></div>
                <div className="b_dirPhoto"><Image src="/img/vokal.png" alt=""  width={500} height={650} /></div>
                <div className="b_dirPhoto"><Image src="/img/piano.png" alt=""  width={500} height={650} /></div>
                <div className="b_dirPhoto"><Image src="/img/actors.png" alt=""  width={500} height={650} /></div>
              </div>
              <div className="btn_wrapper text-center">
                <Link className="main_btn mt-5 width_constrained" href="/order">Подать заявку</Link>
              </div>
          </div>
        </section>
        <section className="l-section teachers">
          <div className="container-lg">
            <Slider {...settings}>
            <div className="sliderItem">
              <div className="sliderPhoto">
                <Image src="/img/teacher_photo.png" alt="" width={350} height={400}></Image>
                <div className="itemBody">
                  <div className="itemName">Анастасия Кан</div>
                  <div className="itemSubtitle">Хип-хоп, кавер-дэнс</div>
                  <div className="itemText">Привет! Меня зовут Анастасия и я преподаватель танцев. Танец - моя страсть, и я счастлива делиться своими знаниями и опытом с другими людьми.</div>
                </div>
              </div>
            </div>
            <div className="sliderItem">
              <div className="sliderPhoto">
                <Image src="/img/teacher_photo.png" alt="" width={350} height={400}></Image>
                <div className="itemBody">
                  <div className="itemName">Анастасия Кан</div>
                  <div className="itemSubtitle">Хип-хоп, кавер-дэнс</div>
                  <div className="itemText">Привет! Меня зовут Анастасия и я преподаватель танцев. Танец - моя страсть, и я счастлива делиться своими знаниями и опытом с другими людьми.</div>
                </div>
              </div>
            </div>
            <div className="sliderItem">
              <div className="sliderPhoto">
                <Image src="/img/teacher_photo.png" alt="" width={350} height={400}></Image>
                <div className="itemBody">
                  <div className="itemName">Анастасия Кан</div>
                  <div className="itemSubtitle">Хип-хоп, кавер-дэнс</div>
                  <div className="itemText">Привет! Меня зовут Анастасия и я преподаватель танцев. Танец - моя страсть, и я счастлива делиться своими знаниями и опытом с другими людьми.</div>
                </div>
              </div>
            </div>
            <div className="sliderItem">
              <div className="sliderPhoto">
                <Image src="/img/teacher_photo.png" alt="" width={350} height={400}></Image>
                <div className="itemBody">
                  <div className="itemName">Анастасия Кан</div>
                  <div className="itemSubtitle">Хип-хоп, кавер-дэнс</div>
                  <div className="itemText">Привет! Меня зовут Анастасия и я преподаватель танцев. Танец - моя страсть, и я счастлива делиться своими знаниями и опытом с другими людьми.</div>
                </div>
              </div>
            </div>
            </Slider>
           
          </div>
        </section>
      </main>
    </>
  )
}
