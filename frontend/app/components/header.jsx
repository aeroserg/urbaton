'use client'

import Link from "next/link"
import Image from "next/image"

export default function Header({...props}) {
    return (
        <header>
            <div className="container-lg">
                <div className="header_inner d-flex">
                    <div className="logo"><Image alt="" width={100} height={50} src="logo.svg" /></div>
                    <div className="header_centerText">{props.headerText}</div>
                    <div className="header_authLink"><Link href="/auth" >Войдите</Link></div>
                </div>
            </div>
        </header>
    )
}