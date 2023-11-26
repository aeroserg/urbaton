'use client'

import { useEffect,useState } from "react"
import Image from "next/image"

export default function Nav({...props}) {
    const [showToolTip, setShowToolTip] = useState(false);
   
   function handleMessage(){
        setShowToolTip(!showToolTip)
    }
    if (props.lk === 'school') {
        return (
            <nav>
            <ul className="b_nav">
                <li><a href="/">Главная</a></li>
                <li><a href="/lk/elec">Электронный журнал</a></li>
                <li><a href="/lk/teachers/">Преподаватели</a></li>
                <li><a href="#news">Новости и объявления</a></li>
                <li><a href="#sendNotifiaction">Отправить сообщение</a></li>
                <li onClick={handleMessage} ><Image alt="сообщения" width={30} height={30} src={'messager_notif.svg'}/></li>
            </ul>
            {showToolTip &&
            <div className="messages">
                <div className="messageItem">
                    <Image alt="" width={50} height={50} src={'/img/photo_icon.svg'}></Image>
                    <div className="messageDesc">
                        <div className="messageName">Ананстасия Кан</div>
                        <div className="messageText">Перенос занятия. Занятие по хип-хопу 10.08 в 15.30 перенесено на 12.08 в 17.00 </div>
                    </div>
                </div>
                <div className="messageItem">
                    <Image alt="" width={50} height={50} src={'/img/photo_icon.svg'}></Image>
                    <div className="messageDesc">
                        <div className="messageName">Ананстасия Кан</div>
                        <div className="messageText">Перенос занятия. Занятие по хип-хопу 10.08 в 15.30 перенесено на 12.08 в 17.00 </div>
                    </div>
                </div>
                <div className="messageItem">
                    <Image alt="" width={50} height={50} src={'/img/photo_icon.svg'}></Image>
                    <div className="messageDesc">
                        <div className="messageName">Ананстасия Кан</div>
                        <div className="messageText">Перенос занятия. Занятие по хип-хопу 10.08 в 15.30 перенесено на 12.08 в 17.00 </div>
                    </div>
                </div>
                <div className="messageItem">
                    <Image alt="" width={50} height={50} src={'/img/photo_icon.svg'}></Image>
                    <div className="messageDesc">
                        <div className="messageName">Ананстасия Кан</div>
                        <div className="messageText">Перенос занятия. Занятие по хип-хопу 10.08 в 15.30 перенесено на 12.08 в 17.00 </div>
                    </div>
                </div>
                
            </div>}
        </nav>
        )
    } else if (props.lk === 'stud'){
        return (
            <nav>
            <ul className="b_nav">
                <li><a href="/">Главная</a></li>
                <li><a href="/lk/elec">Электронный журнал</a></li>
                <li><a href="/lk/teachers/">Преподаватели</a></li>
                <li><a href="#news">Новости и объявления</a></li>
            </ul>
            {showToolTip &&
            <div className="messages">
                <div className="messageItem">
                    <Image alt="" width={50} height={50} src={'/img/photo_icon.svg'}></Image>
                    <div className="messageDesc">
                        <div className="messageName">Ананстасия Кан</div>
                        <div className="messageText">Перенос занятия. Занятие по хип-хопу 10.08 в 15.30 перенесено на 12.08 в 17.00 </div>
                    </div>
                </div>
                <div className="messageItem">
                    <Image alt="" width={50} height={50} src={'/img/photo_icon.svg'}></Image>
                    <div className="messageDesc">
                        <div className="messageName">Ананстасия Кан</div>
                        <div className="messageText">Перенос занятия. Занятие по хип-хопу 10.08 в 15.30 перенесено на 12.08 в 17.00 </div>
                    </div>
                </div>
                <div className="messageItem">
                    <Image alt="" width={50} height={50} src={'/img/photo_icon.svg'}></Image>
                    <div className="messageDesc">
                        <div className="messageName">Ананстасия Кан</div>
                        <div className="messageText">Перенос занятия. Занятие по хип-хопу 10.08 в 15.30 перенесено на 12.08 в 17.00 </div>
                    </div>
                </div>
                <div className="messageItem">
                    <Image alt="" width={50} height={50} src={'/img/photo_icon.svg'}></Image>
                    <div className="messageDesc">
                        <div className="messageName">Ананстасия Кан</div>
                        <div className="messageText">Перенос занятия. Занятие по хип-хопу 10.08 в 15.30 перенесено на 12.08 в 17.00 </div>
                    </div>
                </div>
                
            </div>}
        </nav>
        )
    }
    else {
        return (
            <nav>
                <ul className="b_nav">
                    <li><a href="/#directions">Направления подготовки</a></li>
                    <li><a href="order">Оставить заявку</a></li>
                    <li><a href="/#teachers">Преподаватели</a></li>
                    <li><a href="/#news">Новости и объявления</a></li>
                </ul>
            </nav>
        )
    }
   
}