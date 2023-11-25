import { useEffect } from "react"
import Image from "next/image"

export default function Nav({...props}) {
    function displayNone() {
        
    }
   function handleMessage(){
        return(
            <>

            </>
        )
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
                <li onMouseOver={handleMessage} onMouseLeave={displayNone}><Image alt="сообщения" width={30} height={30} src={'messager_notif.svg'}/></li>
            </ul>
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