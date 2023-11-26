'use client'

import Link from "next/link"
import Image from "next/image"
import Nav from "./nav"
import { useEffect, useState } from "react"
import { getCookie } from "cookies-next"

export default function Header({...props}) {
    const [userName, setName] = useState(undefined);
     useEffect(() => {
        const HOST = location.protocol + '//' + location.host

        if (getCookie('XToken')) {
            fetch(`${HOST}/api/header`, {
                method: "GET",
                headers: {
                    'Authorization': `Bearer ${getCookie('XToken')}`
                  }
            })
            .then(response => response.json())
            .then(data =>{
                setName(data.user_name)
            })  

        } 
    }, [])
   
    return (
        <header>
            <div className="container-lg">
                <div className="header_inner d-flex">
                    <div className="logo"><Image alt="" width={75} height={75} style={{marginRight: "2rem"}} src="/logo.svg" /></div>
                    <div className="header_centerText"><Nav lk={props.isForLk}/></div>
                    {/* <div className="header_authLink"><Link href="/auth" >Войдите</Link></div> */}
                    <div className="b_rigthSide_wrapper">
                        <div className="b_right_name">
                            {userName ? <Link href="/lk/">{userName }</Link>  : <Link href="/auth">Вход </Link>}
                        </div>
                        <div className="b_right_surname">
                            {userName? <Link href="/signout">Выйти</Link> : ''}
                        </div>
                    </div>
                </div>
            </div>
        </header>
    )
}