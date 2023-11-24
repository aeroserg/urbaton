import { useEffect } from "react"

export default function Nav({...props}) {
    if (props.isForLk) {
        return (
            <nav>
            <ul className="b_nav">
                <li><a href="#directions">Направления 
подготовки</a></li>
                <li><a href="order">Оставить
заявку</a></li>
                <li><a href="#teachers">Преподаватели</a></li>
                <li><a href="#news">Новости 
и объявления</a></li>
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