import Image from "next/image"
import Link from "next/link"
export default function News(){
    return(
        <section className="l-section">
            <div className="container-lg">
               
                <div className="newsGrid">
                <Link href='/news/1'>
                        <div className="newsItem">
                            <div className="newsPhoto">
                                <Image alt="" width={300} height={200} src={'/img/news1.png'}></Image>
                            </div>
                            <div className="newsText">
                                <div className="newsDate">
                                    15 июня
                                </div>
                                <div className="newsTitle">
                                    Музыкальный концерт “Летняя симфония”
                                </div>
                            </div>
                        </div>
                        </Link>
                        <Link href='/news/1'>
                        <div className="newsItem">
                            <div className="newsPhoto">
                                <Image alt="" width={300} height={200} src={'/img/news2.png'}></Image>
                            </div>
                            <div className="newsText">
                                <div className="newsDate">
                                    15 июня
                                </div>
                                <div className="newsTitle">
                                    Музыкальный концерт “Летняя симфония”
                                </div>
                            </div>
                        </div>
                        </Link>
                        <Link href='/news/1'>
                        <div className="newsItem">
                            <div className="newsPhoto">
                                <Image alt="" width={300} height={200} src={'/img/news3.png'}></Image>
                            </div>
                            <div className="newsText">
                                <div className="newsDate">
                                    15 июня
                                </div>
                                <div className="newsTitle">
                                    Музыкальный концерт “Летняя симфония”
                                </div>
                            </div>
                        </div>
                        </Link>
                        <Link href='/news/1'>
                        <div className="newsItem">
                            <div className="newsPhoto">
                                <Image alt="" width={300} height={200} src={'/img/news4.png'}></Image>
                            </div>
                            <div className="newsText">
                                <div className="newsDate">
                                    15 июня
                                </div>
                                <div className="newsTitle">
                                    Музыкальный концерт “Летняя симфония”
                                </div>
                            </div>
                        </div>
                        </Link>
                    </div>
               
            </div>
        </section>
    )
}