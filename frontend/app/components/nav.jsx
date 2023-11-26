'use client'

import { useEffect,useState } from "react"
import { getCookie } from "cookies-next"
import Image from "next/image"

export default function Nav({...props}) {
    const [messages, setMessages] = useState({
        messages:[]
    })
    const [showToolTip, setShowToolTip] = useState(false);
    useEffect(() => {
        if (getCookie('XToken')) {
            fetch('http://localhost/api/get_messages', {
                method: "GET",
                headers: {
                    'Authorization': `Bearer ${getCookie('XToken')}`
                  }
            })
            .then(response => response.json())
            .then(data =>{
                setMessages(data)
                console.log(data)
            })
        } 
    },[showToolTip])
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
            {showToolTip && messages.messages.length ? 
            <div className="messages">
            { messages.messages.map((item,index) => (
                <div key={index} className="messageItem">
                    <Image alt="" width={50} height={50} src={'/img/photo_icon.svg'}></Image>
                    <div className="messageDesc">
                        <div className="messageName">{item.sender_first_name} {item.sender_last_name}</div>
                        <div className="messageText">{item.text} </div>
                    </div>
                </div>
            ))}               
            </div>: showToolTip && !messages.messages.length ? <div className="messages"><div className="messageItem">
                   
                    <div className="messageDesc">
                        <div className="messageName">Новых сообщений нет</div>
                        <div className="messageText"></div>
                    </div>
                </div></div>: <></> }
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
            {messages.length ? messages.map((item,index) => (
                <div key={index} className="messageItem">
                    <Image alt="" width={50} height={50} src={'/img/photo_icon.svg'}></Image>
                    <div className="messageDesc">
                        <div className="messageName">{item.sender_first_name} {item.sender_last_name}</div>
                        <div className="messageText">{item.text} </div>
                    </div>
                </div>
            )) :<></>}               
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